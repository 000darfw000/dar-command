#!/usr/bin/env python

from ..common import DARCommandCommon

from .startproject import DARCommandCommandsStartproject
from .bower_dependencies import DARCommandCommandsBower
from .os_dependencies import DARCommandCommandsOS
from .pip_dependencies import DARCommandCommandsPIP
from .update_package import DARCommandCommandsUpdatePackage
from .migrations import DARCommandCommandsMigrations
from .liveserver import DARCommandCommandsLive
from .create_system_users import DARCommandCommandsSystemUsers


class DARCommandCommands(DARCommandCommon):
    def __init__(self, subparsers):
        """ Constructor
        """
        self.subparsers = subparsers
        self.commands_list = self.get_commands_list()
        self.setup()

    @staticmethod
    def get_commands_list():
        """ Get commands lists of classes
        """
        return [
            DARCommandCommandsStartproject,
            DARCommandCommandsBower,
            DARCommandCommandsOS,
            DARCommandCommandsPIP,
            DARCommandCommandsUpdatePackage,
            DARCommandCommandsMigrations,
            DARCommandCommandsLive,
            DARCommandCommandsSystemUsers,
        ]

    def setup(self):
        """ Setup parsers
        """
        for command_class in self.commands_list:
            definition = command_class.get_definition()

            subparser = self.subparsers.add_parser(
                definition.get("name"),
                description=definition.get("description")
            )

            for argument in definition.get("arguments"):
                if argument.get("type"):
                    parameters = {
                        "type": argument.get("type"),
                    }
                else:
                    parameters = {
                        "action": "store_true",
                    }

                subparser.add_argument(
                    argument.get("short_flag"),
                    argument.get("long_flag"),
                    help=argument.get("help"),
                    **parameters
                )

    def identify_command(self, args):
        """ Get command class instance
        """
        subparser_name = args.subparser_name

        for command_class in self.commands_list:
            definition = command_class.get_definition()
            name = definition.get("name")

            if subparser_name == name:
                return command_class(args)

        return None
