import sys
from datetime import datetime
from typing import List

from whatsappMessanger.messanger import WhatsAppMessanger
from whatsappMessanger.myArgparser import MyArgparser


def main():
    my_parser = MyArgparser("WhatsApp Bot", "Send messages to your friends")

    if not my_parser.skip_confirm():
        confirm(
            my_parser.get_names(), my_parser.get_message(), my_parser.get_timestamp()
        )

    messanger = WhatsAppMessanger()
    for target in my_parser.get_names():
        messanger.send_message(
            target, my_parser.get_message(), my_parser.get_timestamp()
        )


def confirm(names: List[str], message: str, timestamp: datetime):
    """Confirm the values with Yes

    Args:
        names (List[str]): Destination names
        message (str): Message to send
        timestamp (datetime): When to send the message
    """
    choice = input(
        f'Sure so send messages to {names} with "{message}" at {timestamp}? [Y,N]'
    )

    if choice.lower() != "y":
        print("...exit")
        sys.exit()


if __name__ == "__main__":
    main()
