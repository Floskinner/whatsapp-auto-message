import argparse
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
            nargs="+",
            type=str,
            required=True,
            help="The Name of the Users to send the message. At least one required",
        )

    def get_names(self) -> List[str]:
        """Get all target Names

        Returns:
            List[str]: List of names
        """
        return self.parse_args().names

    def get_message(self) -> str:
        """Get the message to send

        Returns:
            str: Message
        """
        return self.parse_args().message
