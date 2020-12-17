# planka-setup
A python interface to setup a Planka board and import files into tasks. 

## Server Startup ##

This docker-composition will run 3 containers: Planka, Postgres, and pgAdmin. The first two provide the functionally of the system while the third allows for easy administration of Postgres if needed. 

**Step 1:** Set up the data folders for all three containers to mount. This is done by running `./setup.sh` to automatically create the needed folders. If the data folder or subfolders are found the script will error and the user needs to remove the folders.

**Step 2:** Run `docker-compose up -d` from this directory to start all three containers in the background. If you want to run them in the foreground remove the `-d` to have all log displayed to standard out. 

**Step 3:** Connect to Planka at `http://localhost:3000` using the username `demo@demo.demo` and password of `demo`. 

**Note:** If pgAdmin can be found at `http://localhost:8080` with the username is `admin@localhost` and password `planka`. The postgres server info is host `host.docker.internal`, port `5432`, maintenance database `postgres`, and username `postgres`.

## Build Instructions ##

Running the `./planka-setup.py` script with `-n` argument followed by a project name will build out a Planka server with the following items:

Projects:

* 'Project Name'
   * Tasks Board
      * To-do List
         * NMAP Scans Card
            * Discovery Scan
            * Full Port Scan
         * Eyewitness Scan Card
            * Start Scan
            * Review Findings
         * Nessus Scan Card
            * Uncredentialed
            * Credentialed
            * Review Critical/High Findings
         * Web App Card
         * WiFi Assessment Card
            * War-drive
            * Check host isolation
         * Database Scan Card
            * Nessus Credentialed Scan
         * OSSA Card
            * Review Baseline
   * Working List
      * All cards that are currently being worked.
   * Done List
      * All Cards that have been completed.
   * Deadend List
      * Any checks of a host, exploit, etc that only one person has checked. This will allow for a second person to check as time is available. 

Running the `./planka-setup.py` script with `-i` argument followed by a file name will import NMAP findings. These findings will be imported into a Hold Board that has a NMAP list with a card for each IP and subtasks for each port. 
                
