import argparse
import os
from datetime import datetime
from typing import List


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
            "-y",
            "--silent",
            dest="confirm",
            action="store_true",
            required=False,
            help="Skip the confirm of the values",
        )

        self.add_argument(
            "-t",
            "--timestamp",
            dest="time",
            type=lambda timestamp_str: datetime.strptime(
                timestamp_str.strip(), "%d.%m.%Y %H:%M"
            ),
            required=False,
            help="Add a timestamp when to send the message: dd.mm.yyyy hh:mm",
        )

        self.add_argument(
            "-g",
            "--token",
            dest="token",
            type=str,
            required=False,
            help="Set the GH_TOKEN or use the EVN",
        )

        self.__args = self.parse_args()
        if self.__args.token:
            os.environ["GH_TOKEN"] = self.__args.token.strip()

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
        return self.__args.time

    def skip_confirm(self) -> bool:
        """Check if the user want a silent excecution

        Returns:
            bool: True if skip
        """
        return self.__args.confirm
