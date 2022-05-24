import argparse
from typing import List

from whatsappMessanger.messanger import WhatsAppMessanger


def main():
    my_parser = MyArgparser("WhatsApp Bot", "Send messages to your friends")

    messanger = WhatsAppMessanger()

    for target in my_parser.get_names():
        messanger.send_message(target, my_parser.get_message)


class MyArgparser(argparse.ArgumentParser):
    def __init__(self, prog: str, description: str, **kwargs):
        super().__init__(prog=prog, description=description, **kwargs)

        self.add_argument(
            "-n",
            "--names",
            dest="names",
            nargs="+",
            type=str,
            required=True,
            help="The Name of the Users to send the message. At least one required",
        )

        self.add_argument(
            "-m",
            "--message",
            dest="message",
            type=str,
            required=True,
            help="The message to send",
        )

        self.parse_args()

    def get_names(self) -> List[str]:
        """Get all target Names

        Returns:
            List[str]: List of names
        """
        names = [name.strip() for name in self.parse_args().names]
        return names

    def get_message(self) -> str:
        """Get the message to send

        Returns:
            str: Message
        """
        return self.parse_args().message.strip()


if __name__ == "__main__":
    main()
