from whatsappMessanger.browser import Browser


class WhatsAppMessanger:
    """Class to handle WhatsApp messanges"""

    def __init__(self):
        self.__browser = Browser()
        self.connect_phone()

    def send_message(self, targed_name: str, msg: str):
        """Send a message to the targed

        Args:
            targed_name (str): Targed name
            msg (str): Message to send
        """
        self.__browser.send_message(targed_name, msg)

    def connect_phone(self):
        """Connect the WhatsApp Web with your phone"""

        print("Scan the QR-Code with your phone")
        self.__browser.connect_phone()
