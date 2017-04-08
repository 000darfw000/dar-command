#!/usr/bin/env python

import os
import shutil
import subprocess


class DARCommandCommandsCommon(object):
    @staticmethod
    def get_instance_dir():
        return os.getcwd()

    @staticmethod
    def directory_exists(path):
        return os.path.isdir(path)

    @staticmethod
    def remove_directory(path):
        shutil.rmtree(path)

    @staticmethod
    def goto_directory(path):
        os.chdir(path)

    @staticmethod
    def run_command(arguments):
        subprocess.call(arguments)