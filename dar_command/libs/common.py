#!/usr/bin/env python

import argparse


class DARCommandCommon(object):
    DAR_COMMAND_PACKAGE = "git+https://github.com/000darfw000/dar-command.git"
    DEFAULT_PORT = 9500

    def __init__(self):
        self.args = None
        self.parser = argparse.ArgumentParser(
            "DAR command line interface"
        )
        self.subparsers = self.parser.add_subparsers(
            dest='subparser_name'
        )