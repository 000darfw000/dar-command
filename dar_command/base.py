#!/usr/bin/env python

import argparse

from libs.common import DARCommandCommon
from libs.commands import DARCommandCommands


class DARCommand(DARCommandCommon):
    def __init__(self):
        self.args = None
        self.parser = argparse.ArgumentParser(
            "DAR command line interface"
        )
        self.subparsers = self.parser.add_subparsers(
            dest='subparser_name'
        )

    def parse(self):
        commands = DARCommandCommands(self.subparsers)

        # Get arguments
        self.args = self.parser.parse_args()

        # Identify command
        command = commands.identify_command(self.args)

        # Execute command
        command.execute()