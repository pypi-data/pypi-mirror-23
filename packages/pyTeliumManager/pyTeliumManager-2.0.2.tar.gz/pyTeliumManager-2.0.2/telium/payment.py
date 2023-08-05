import json
from functools import reduce
from operator import xor
import curses.ascii
from pycountry import currencies
from telium.constant import TERMINAL_PAYMENT_SUCCESS, TERMINAL_ANSWER_COMPLETE_SIZE, TERMINAL_ANSWER_LIMITED_SIZE


class TeliumData:

    def __init__(self, pos_number, amount, payment_mode, currency_numeric, private):
        """
        :param str pos_number: Checkout ID, min 1, max 99.
        :param float amount: Payment amount, min 0.01, max 99999.99.
        :param str payment_mode: Type of payment support, please refers to provided constants.
        :param str currency_numeric: Type of currency ISO format, please use specific setter.
        :param str private:
        """
        self._pos_number = pos_number
        self._payment_mode = payment_mode
        self._currency_numeric = currency_numeric
        self._amount = amount
        self._private = private

    @property
    def pos_number(self):
        """
        Indicate your checkout id
        :return: Checkout id
        :rtype: str
        """
        return self._pos_number

    @property
    def payment_mode(self):
        return self._payment_mode

    @property
    def currency_numeric(self):
        return self._currency_numeric

    @currency_numeric.setter
    def currency_numeric(self, currency):
        self._currency_numeric = str(currencies.get(alpha_3=currency.upper()).numeric).zfill(3)

    @property
    def private(self):
        return self._private

    @property
    def amount(self):
        return self._amount

    @staticmethod
    def lrc(data):
        """
        Calc. LRC from data. Checksum
        :param data: Data from which LRC checksum should be computed
        :return: 0x00 < Result < 0xFF
        :rtype: int
        """
        if isinstance(data, str):
            data = data.encode('ascii')
        return reduce(xor, [c for c in data])

    def toProtoE(self):
        return bytes()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class TeliumAsk(TeliumData):

    def __init__(self, pos_number, answer_flag, transaction_type, payment_mode, currency_numeric, delay, authorization, amount):
        super(TeliumAsk, self).__init__(pos_number, amount, payment_mode, currency_numeric, ' ' * 10)
        self._answer_flag = answer_flag
        self._transaction_type = transaction_type
        self._payment_mode = payment_mode
        self._delay = delay
        self._authorization = authorization

    @property
    def answer_flag(self):
        """
        Whenever ask for extended data in answer.
        Should correspond to one of the provided constants.
        :return: '1' or '0'
        :rtype: str
        """
        return self._answer_flag

    @property
    def transaction_type(self):
        return self._transaction_type

    @property
    def delay(self):
        """
        Describe if answer should be immediate (without valid status) or after transaction.
        :return: 'A010' | 'A011'
        :rtype: str
        """
        return self._delay

    @property
    def authorization(self):
        """
        Describe if the terminal has to manually authorize payment.
        TERMINAL_FORCE_AUTHORIZATION_ENABLE: 'B011'
        TERMINAL_FORCE_AUTHORIZATION_DISABLE: 'B010'
        :return: 'B011' | 'B010'
        :rtype: str
        """
        return self._authorization

    def toProtoE(self):
        """
        Transform current object so it could be transfered to device (Protocol E)
        :return: Bytes array with payment information
        :rtype: bytes
        """
        packet = (

            str(self.pos_number).zfill(2) +

            ('%.0f' % (self.amount * 100)).zfill(8) +

            self.answer_flag +

            self.payment_mode +

            self.transaction_type +

            self.currency_numeric +

            self.private +

            self.delay +

            self.authorization)

        if len(packet) != 34:
            raise Exception('Le paquet cible ne respecte pas la taille du protocol E Telium (!=34)')

        packet += chr(curses.ascii.controlnames.index('ETX'))

        return chr(curses.ascii.controlnames.index('STX')) + packet + chr(TeliumData.lrc(packet))


class TeliumResponse(TeliumData):

    def __init__(self, pos_number, transaction_result, amount, payment_mode, repport, currency_numeric, private):
        super(TeliumResponse, self).__init__(pos_number, amount, payment_mode, currency_numeric, private)
        self._transaction_result = transaction_result
        self._repport = repport

    @property
    def transaction_result(self):
        """
        TERMINAL_PAYMENT_SUCCESS: 0
        TERMINAL_PAYMENT_REJECTED: 7
        TERMINAL_PAYMENT_TIMEOUT: 9
        :return: Result provided after transaction. Should'nt be different than 0, 7 or 9.
        :rtype: int
        """
        return self._transaction_result

    @property
    def repport(self):
        """
        Contain data like the card numbers for instance.
        Should be handled wisely.
        :return: RAW Repport
        :rtype: str
        """
        return self._repport

    @property
    def has_succeeded(self):
        """
        Verify if payment has been succesfuly processed.
        :return: True if payment has been approved
        :rtype: bool
        """
        return self.transaction_result == TERMINAL_PAYMENT_SUCCESS

    @property
    def card_id(self):
        """
        Read card numbers if available
        :return: Card numbers
        :rtype: str
        """
        return self._repport[0:16]

    @property
    def transaction_id(self):
        """
        Return transaction id generated by device if available.
        This method is an alias of self.private
        :return: Transaction unique id.
        :rtype: str
        """
        return self.private

    @staticmethod
    def decode(data, expected_size=83):
        """
        Create TeliumResponse from raw bytes array
        :param bytes data: Raw bytes answer from terminal
        :param int expected_size: Size of answer from Terminal
        :return: TeliumResponse
        :rtype: telium.TeliumResponse
        """
        if expected_size == TERMINAL_ANSWER_COMPLETE_SIZE:
            return TeliumResponse(
                str(data[0:2], 'ascii'),
                int(chr(data[2])),
                str(data[3:11], 'ascii'),
                chr(data[11]),
                str(data[12:67], 'ascii'),
                str(data[68:71], 'ascii'),
                str(data[72:82], 'ascii')
            )
        elif expected_size == TERMINAL_ANSWER_LIMITED_SIZE:
            return TeliumResponse(
                str(data[0:2], 'ascii'),
                int(chr(data[2])),
                str(data[3:11], 'ascii'),
                chr(data[11]),
                '',
                str(data[12:15], 'ascii'),
                str(data[16:26], 'ascii')
            )
        return None
