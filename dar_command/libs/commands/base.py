#!/usr/bin/env python

from .startproject import DARCommandCommandsStartproject


class DARCommandCommands(object):
    @staticmethod
    def get_commands_list():
        return [
            DARCommandCommandsStartproject.get_definition(),
        ]

