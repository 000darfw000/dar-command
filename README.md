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

* Install bower dependencies:
    ```bash
    dar-command.py install_bower_dependencies
    ```

* Install Operating System dependencies:
    ```bash
    dar-command.py install_os_dependencies
    ```

* Install pip dependencies:
    ```bash
    dar-command.py install_pip_dependencies
    ```

* Update dar-command package:
    ```bash
    dar-command.py update
    ```
    
* Run migrations:
    ```bash
    # This runs makemigrations and migrate
     
    dar-command.py migrate
    ```

* Run live server port 9500:
    ```bash
    # This runs liverserver at port 9500
     
    dar-command.py liveserver
    ```

* Create system users (admin, system, prueba):
    ```bash
    # This command create system users
     
    dar-command.py create_system_users
    ```
