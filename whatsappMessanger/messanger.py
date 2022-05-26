from datetime import datetime
from time import sleep

from whatsappMessanger.browser import Browser


class WhatsAppMessanger:
    """Class to handle WhatsApp messanges"""

    def __init__(self):
        self.__browser = Browser()
        self.connect_phone()

    def send_message(self, targed_name: str, msg: str, time: datetime = None):
        """Send a message to the targed

        Args:
            targed_name (str): Targed name
            msg (str): Message to send
        """
        if time:
            self.__sleep_until_time_reached(time)
        self.__browser.send_message(targed_name, msg)

    def connect_phone(self):
        """Connect the WhatsApp Web with your phone"""

        print("Scan the QR-Code with your phone")
        self.__browser.connect_phone()

    def __sleep_until_time_reached(self, target_time: datetime):
        current_time = datetime.now()

        timediff = abs(target_time - current_time)
        print(f"Sleeping... {timediff.seconds} seconds ...zZZ")
        sleep(timediff.total_seconds())
