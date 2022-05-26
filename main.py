import argparse
import sys
from datetime import datetime
from typing import List

from whatsappMessanger.messanger import WhatsAppMessanger


def main():
    my_parser = MyArgparser("WhatsApp Bot", "Send messages to your friends")

    choice = input(
        f'Sure so send messages to {my_parser.get_names()} with "{my_parser.get_message()}" at {my_parser.get_timestamp()}? [Y,N]'
    )

    if choice != "Y":
        print("...exit")
        sys.exit()

    messanger = WhatsAppMessanger()
    for target in my_parser.get_names():
        messanger.send_message(
            target, my_parser.get_message(), my_parser.get_timestamp()
        )


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

        self.add_argument(
            "-t",
            "--timestamp",
            dest="time",
            type=str,
            required=False,
            help="Add a timestamp when to send the message: dd.mm.yyyy hh:mm",
        )

        self.__args = self.parse_args()

    def get_names(self) -> List[str]:
        """Get all target Names

        Returns:
            List[str]: List of names
        """
        names = [name.strip() for name in self.__args.names]
        return names

    def get_message(self) -> str:
        """Get the message to send

        Returns:
            str: Message
        """
        return self.__args.message.strip()

    def get_timestamp(self) -> datetime:
        """Get the datetime when to send the message

        Returns:
            datetime: timestamp
        """
        timestamp_str = self.__args.time.strip()
        return datetime.strptime(timestamp_str, "%d.%m.%Y %H:%M")


if __name__ == "__main__":
    main()
