#!/usr/bin/env python

import os

from ..common import DARCommandCommon


class DARCommandCommandsUpdatePackage(DARCommandCommon):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Install Operating System dependencies:
            ```bash
            dar-command.py install_os_dependencies
            ```
        """
        return {
            "name": "install_os_dependencies",
            "description": """Install Operating System dependencies""",
            "arguments": [],
        }

    def execute(self):
        """ Execute
        """
        command_arguments = [
            "pip",
            "install",
            "-U",
            self.DAR_COMMAND_PACKAGE,
        ]
        self.run_command(command_arguments)