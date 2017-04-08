# dar-command
DAR Command - Django Applications Robot Command

`Command line interface`


**Usage:**

* Install package:
    ```bash
    pip install -U git+https://github.com/000darfw000/dar-command.git
    ```
  
* Start a new project:
    ```bash
    # The PROJECT-NAME is the name of the project, this value is used as prefix for
    # django settings variables like STATIC_URL = PROJECT_NAME_static 
     
    # The project will be located in the INSTANCE-DIR directory
     
    dar-command.py startproject PROJECT-NAME INSTANCE-DIR
    ```
    
    ```bash
    # The PROJECT-NAME is the name of the project, this value is used as prefix for
    # django settings variables like STATIC_URL = PROJECT_NAME_static 
     
    # This will create a project in the current directory where the command is executed
     
    dar-command.py startproject PROJECT-NAME
    ```
    
    Example:
    
    ```bash
    cd ~/instances
    mkvirtualenv dartest
    pip install -U git+https://github.com/000darfw000/dar-command.git
    dar-command.py startproject dartest
    ```
