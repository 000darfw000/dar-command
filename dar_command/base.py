#!/usr/bin/env python

from libs.common import DARCommandCommon
from libs.commands import DARCommandCommands


class DARCommand(DARCommandCommon):
    def parse(self):
        commands = DARCommandCommands(self.subparsers)

        # Get arguments
        self.args = self.parser.parse_args()

        # Identify command
        command = commands.identify_command(self.args)

        # Execute command
        command.execute()