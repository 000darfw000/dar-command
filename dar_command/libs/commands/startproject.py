#!/usr/bin/env python

import os

from .common import DARCommandCommandsCommon
from ..exceptions import DARException


class DARCommandCommandsStartproject(DARCommandCommandsCommon):
    DEFAULT_NAME = "darproject"
    DEFAULT_BASEDIR = None
    DEFAULT_OVERWRITE = False
    DJANGO_ADMIN = "django-admin.py"

    def __init__(self, args):
        """ Constructor
        """
        self.DEFAULT_BASEDIR = self.get_instance_dir()

        self.args = args

        # Arguments
        self.name = None
        self.basedir = None
        self.overwrite = None

        self.set_arguments()

    def validate_basedir(self):
        """ Validate base directory
        """
        if not self.directory_exists(self.basedir):
            raise DARException({
                "message": "Invalid basedir",
                "path": self.basedir
            })

    def set_arguments(self):
        """ Set arguments received from command line
        """
        # name
        name = getattr(self.args, "name")
        self.name = name if name else self.DEFAULT_NAME

        # basedir
        basedir = getattr(self.args, "basedir")
        self.basedir = basedir if basedir else self.DEFAULT_BASEDIR
        self.validate_basedir()

        # overwrite
        overwrite = getattr(self.args, "overwrite")
        self.overwrite = overwrite if overwrite else self.DEFAULT_OVERWRITE

    @staticmethod
    def get_definition():
        """
        * Start a new project:
            ```bash
            # This will create a project in the current directory where the command is executed.
            # If no name is provided this will use 'darproject'
            dar-command.py startproject -n PROJECT-NAME
             
            # This will create a project in the directory PROJECT-BASE-DIR.
            dar-command.py startproject -n PROJECT-NAME -b PROJECT-BASE-DIR

            # This will create a project in the directory PROJECT-BASE-DIR and overwrite if exists
            dar-command.py startproject -n PROJECT-NAME -b PROJECT-BASE-DIR -o
            ```

            Example:
            
            ```bash
            aricalso@000rayuela000:~$ cd ~/instances
            aricalso@000rayuela000:/home/aricalso/instances$ mkvirtualenv dartest
            (dartest) aricalso@000rayuela000:/home/aricalso/instances$ pip install -U git+https://github.com/000darfw000/dar-command.git
            (dartest) aricalso@000rayuela000:/home/aricalso/instances$ dar-command.py startproject -n dartest -b ~/instances
            (dartest) aricalso@000rayuela000:/home/aricalso/instances/dartest$
            ```
        """
        return {
            "name": "startproject",
            "description": """Start a new project. This will create a project in the current directory where the command is 
                           executed. If no name is provided this will use 'darproject'""",
            "arguments": [
                {
                    "short_flag": "-n",
                    "long_flag": "--name",
                    "help": """Slug name, this is used for directory name also as a prefix for STATIC_URL, sqlite 
                            database name, ...""",
                    "type": str,
                },
                {
                    "short_flag": "-b",
                    "long_flag": "--basedir",
                    "help": """Base directory, if not specified the project will be created in the
                            current location.""",
                    "type": str,
                },
                {
                    "short_flag": "-o",
                    "long_flag": "--overwrite",
                    "help": """If project directory exists, overwrite it."""
                },
            ],
        }

    @property
    def project_directory(self):
        """ Get project directory
        """
        return os.path.join(
            self.basedir,
            self.name
        )

    def create_project_directory(self):
        """ Create the project directory
        """
        path = self.project_directory

        if self.overwrite and self.directory_exists(path):
            try:
                self.remove_directory(path)
            except Exception as e:
                raise DARException({
                    "message": "Error removing the project directory",
                    "path": path,
                    "exception_message": str(e),
                })

        try:
            os.mkdir(path)
        except Exception as e:
            raise DARException({
                "message": "Error creation the project directory",
                "path": path,
                "exception_message": str(e),
            })

    def create_django_project(self):
        """ Create django project
        """
        self.run_command([
            self.DJANGO_ADMIN,
            "startproject",
            "conf",
            self.project_directory
        ])

    def goto_project_directory(self):
        """ Go to project directory
        """
        self.goto_directory(self.project_directory)

    def execute(self):
        """ Execute
        """
        self.create_project_directory()
        self.goto_project_directory()
        self.create_django_project()