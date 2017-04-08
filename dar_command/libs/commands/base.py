#!/usr/bin/env python

from .startproject import DARCommandCommandsStartproject


class DARCommandCommands(object):
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