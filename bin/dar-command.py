#!/usr/bin/env python

from dar_command import DARCommand


def main():
    """ DAR Command line interface
    """
    dar_command = DARCommand()
    dar_command.parse()

if __name__ == "__main__":
    main()