from unittest import TestCase, main

import os, pty
import curses.ascii
import threading

from faker import Faker
from telium.payment import TeliumData
from telium import *


class FakeTeliumDevice:

    def __init__(self):
        self._master, self._slave = pty.openpty()
        self._s_name = os.ttyname(self._slave)

        self._fake = Faker()

        self._fake_device = threading.Thread(target=self.__run)
        self._fake_device.start()

    @property
    def s_name(self):
        return self._s_name

    @staticmethod
    def _has_signal(data, signal):
        return data[0] == curses.ascii.controlnames.index(signal)

    @staticmethod
    def _create_signal(signal):
        return bytes([curses.ascii.controlnames.index(signal)])

    def _wait_signal(self, signal):
        return FakeTeliumDevice._has_signal(os.read(self._master, 1), signal)

    def _send_signal(self, signal):
        os.write(self._master, FakeTeliumDevice._create_signal(signal))

    def __run(self):

        if self._wait_signal('ENQ'):

            self._send_signal('ACK')

            raw_data = os.read(self._master, TERMINAL_ANSWER_COMPLETE_SIZE)

            if TeliumData.lrc_check(raw_data) is True:

                payment_pending = TeliumAsk.decode(raw_data)

                print('from slave : ', payment_pending.__dict__)

                self._send_signal('ACK')  # Accept data from master

                if not self._wait_signal('EOT'):
                    self._send_signal('NAK')
                    exit(1)

                my_response = TeliumResponse(
                    payment_pending.pos_number,
                    TERMINAL_PAYMENT_SUCCESS,
                    payment_pending.amount,
                    payment_pending.payment_mode,
                    (self._fake.credit_card_number(card_type='visa16') + '0' * 39),
                    payment_pending.currency_numeric,
                    '0' * 10
                )

                self._send_signal('ENQ')

                if self._wait_signal('ACK'):
                    os.write(self._master, bytes(my_response.encode(), 'ascii'))

                    if self._wait_signal('ACK'):
                        self._send_signal('EOT')
                        exit(0)

                    self._send_signal('NAK')

                else:

                    self._send_signal('NAK')
                    exit(1)

            else:
                self._send_signal('NAK')
                exit(1)


class TestTPE(TestCase):

    def setUp(self):
        self._fake_device = FakeTeliumDevice()

    def test_demande_paiement(self):

        my_telium_instance = Telium(self._fake_device.s_name)

        # Construct our payment infos
        my_payment = TeliumAsk(
            '1',  # Checkout ID 1
            TERMINAL_ANSWER_SET_FULLSIZED,  # Ask for fullsized repport
            TERMINAL_MODE_PAYMENT_DEBIT,  # Ask for debit
            TERMINAL_TYPE_PAYMENT_CARD,  # Using a card
            TERMINAL_NUMERIC_CURRENCY_EUR,  # Set currency to EUR
            TERMINAL_REQUEST_ANSWER_WAIT_FOR_TRANSACTION,  # Do not wait for transaction end for terminal answer
            TERMINAL_FORCE_AUTHORIZATION_DISABLE,  # Let device choose if we should ask for authorization
            12.5  # Ask for 12.5 EUR
        )

        # Send payment infos to device
        self.assertTrue(my_telium_instance.ask(my_payment))

        my_answer = my_telium_instance.verify(my_payment)

        print('from master : ', my_answer.__dict__)

        self.assertEqual(my_answer.transaction_result, 0)
        self.assertEqual(my_answer.currency_numeric, TERMINAL_NUMERIC_CURRENCY_EUR)
        self.assertEqual(my_answer.private, '0' * 10)


if __name__ == '__main__':
    main()
