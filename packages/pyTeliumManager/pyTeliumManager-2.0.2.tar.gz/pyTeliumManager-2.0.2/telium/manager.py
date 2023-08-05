from serial import Serial
from glob import glob
import curses.ascii
from telium.constant import *
from telium.payment import TeliumResponse


class DeviceNotFoundException(Exception):
    pass


class WrongProtocolELengthException(Exception):
    pass


class SignalDoesNotExistException(Exception):
    pass


class DataFormatUnsupportedException(Exception):
    pass


class TerminalInitializationFailedException(Exception):
    pass


class TerminalWrongUnexpectedAnswerException(Exception):
    pass


class TerminalUnrecognizedConstantException(Exception):
    pass


class TerminalUnexpectedAnswerException(Exception):
    pass


class Telium:
    def __init__(self, path='/dev/ttyACM0', baudrate=9600, timeout=DELAI_REPONSE_TERMINAL_PAIEMENT):
        """
        Create Telium device instance
        :param path: str Path to serial emulated device
        :param baud: int Set baud rate
        :param timeout: int Maximum delai before hanging out.
        """
        self._path = path
        self._baud = baudrate
        self._device = Serial(self._path, self._baud, timeout=timeout)

    @staticmethod
    def get():
        """
        Auto-create a new instance of Telium. The device path will be infered based on most commom location.
        This won't be reliable if you have more than one emulated serial device plugged-in. Won't work either on NT plateform.
        :return: Fresh new Telium instance or None
        :rtype: telium.Telium
        """
        for path in TERMINAL_PROBABLES_PATH:
            probables = glob('%s*' % ''.join(filter(lambda c: not c.isdigit(), path)))
            if len(probables) == 1:
                return Telium(probables[0])
        return None

    def __del__(self):
        if self._device.is_open:
            self._device.close()

    def close(self):
        """
        Close the device if not already closed
        :return: True if device succesfuly closed
        :rtype: bool
        """
        if self._device.is_open:
            self._device.close()
            return True
        return False

    def open(self):
        """
        Open the device if not already opened
        :return: True if device succesfuly opened
        :rtype: bool
        """
        if not self._device.is_open:
            self._device.open()
            return True
        return False

    def _send_signal(self, signal):
        """
        Send single signal to device like 'ACK', 'NAK', 'EOT', etc.. .
        :param signal: str
        :return: None
        """
        if signal not in curses.ascii.controlnames:
            raise SignalDoesNotExistException("Le signal '%s' n'existe pas." % signal)
        self._send(chr(curses.ascii.controlnames.index(signal)))

    def _wait_signal(self, signal):
        """
        Read one byte from serial device and compare to expected.
        :param signal: str
        :return: True if received signal match
        :rtype: bool
        """
        one_byte_read = self._device.read(1)
        expected_char = curses.ascii.controlnames.index(signal)
        #  print('DEBUG wait_signal_received = ', curses.ascii.controlnames[one_byte_read[0]])

        return one_byte_read == expected_char.to_bytes(1, byteorder='big')

    def _initialisation(self):
        """
        Prepare device to receive data
        :return: None
        """
        self._send_signal('ENQ')

        if not self._wait_signal('ACK'):
            # self._send_signal('EOT')
            raise TerminalInitializationFailedException(
                "Payment terminal hasn't been initialized correctly, abording..")

    def _send(self, data):
        """
        Send data to terminal
        :param data: str string representation to convert and send
        :return: Lenght of data actually sended
        :rtype: int
        """
        if not isinstance(data, str):
            raise DataFormatUnsupportedException("You should pass string to _send method, we'll convert it for you.")
        return self._device.write(bytes(data, 'ASCII'))

    def _read_answer(self, expected_size=83):
        """
        Download raw answer and convert it to TeliumResponse
        :return: TeliumResponse
        :rtype: telium.TeliumResponse
        """
        msg = self._device.read(size=expected_size)

        if len(msg) == 0:
            return None

        # assert len(msg) == full_msg_size, 'Answer has a wrong size'
        if msg[0] != curses.ascii.controlnames.index('STX'):
            raise TerminalWrongUnexpectedAnswerException(
                'The first byte of the answer from terminal should be STX.. Have %s and except %s' % (
                    msg[0], curses.ascii.controlnames.index('STX').to_bytes(1, byteorder='big')))
        if msg[-2] != curses.ascii.controlnames.index('ETX'):
            raise TerminalWrongUnexpectedAnswerException(
                'The byte before final of the answer from terminal should be ETX')

        lrc = msg[-1]
        computed_lrc = TeliumResponse.lrc(msg[1:-1])

        if computed_lrc != lrc:
            print('The LRC of the answer from terminal is wrong have %s and except %s' % (lrc, computed_lrc))

        real_msg = msg[1:-2]

        return TeliumResponse.decode(real_msg, expected_size)

    def _get_pending(self):
        """
        Method keeped for tests purposes, shouldn't use in fiable production environnement.
        Very slow computer performance can cause app to not catch data in time
        :return: True if buffer contain ENQ signal
        :rtype: bool
        """
        self._device.timeout = 0.3
        self._device.read(size=1)
        self._device.timeout = DELAI_REPONSE_TERMINAL_PAIEMENT

    def ask(self, telium_ask, raspberry=False):
        """
        Initialize payment to terminal
        :param telium.TeliumAsk telium_ask: Payment info
        :param bool raspberry: Set it to True if you'r running Raspberry PI
        :return: Should give True
        :rtype: bool
        """
        if raspberry:
            self._get_pending()

        # Send ENQ and wait for ACK
        self._initialisation()
        # Send transformed TeliumAsk packet to device
        self._send(telium_ask.toProtoE())

        # Verify if device has received everything
        if not self._wait_signal('ACK'):
            self._send_signal('EOT')
            return False

        # End this communication
        self._send_signal('EOT')

        return True

    def verify(self, telium_ask):
        """
        Wait for answer and convert it for you.
        :param telium.TeliumAsk telium_ask: Payment info
        :return: TeliumResponse or Exception
        :rtype: telium.TeliumResponse
        """
        # We wait for terminal to answer us.
        if self._wait_signal('ENQ'):

            self._send_signal('ACK')  # We're about to say that we're ready to accept data.

            if telium_ask.answer_flag == TERMINAL_ANSWER_SET_FULLSIZED:
                answer = self._read_answer(TERMINAL_ANSWER_COMPLETE_SIZE)
            elif telium_ask.answer_flag == TERMINAL_ANSWER_SET_SMALLSIZED:
                answer = self._read_answer(TERMINAL_ANSWER_LIMITED_SIZE)
            else:
                raise TerminalUnrecognizedConstantException(
                    "Cannot determine expected answer size because answer flag is unknown.")

            self._send_signal('ACK')  # Notify terminal that we've received it all.

            # The terminal should respond with EOT aka. End of Transmission.
            if not self._wait_signal('EOT'):
                raise TerminalUnexpectedAnswerException(
                    "Terminal should have ended the communication with 'EOT'. Something's obviously wrong.")

            return answer

        self._send_signal('EOT')
        return None
