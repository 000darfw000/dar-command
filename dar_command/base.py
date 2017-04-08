#!/usr/bin/env python

from libs.common import DARCommandCommon
from libs.commands import DARCommandCommands


class DARCommand(DARCommandCommon):
    def parse(self):
        # Get commands
        commands_list = DARCommandCommands.get_commands_list()

        # Get arguments
        self.args = self.parser.parse_args()
