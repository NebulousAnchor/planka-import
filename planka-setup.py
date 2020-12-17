#!/usr/bin/env python3
"""Build out a Planka setup.
Usage:
  planka-setup [--log-level=LEVEL] -n PROJECT_NAME [DB_NAME | DB_USER | DB_PASSWORD | DB_HOST | DB_PORT]
  planka-setup [--log-level=LEVEL] -i FILE [DB_NAME | DB_USER | DB_PASSWORD | DB_HOST | DB_PORT]
  planka-setup (-h | --help)
  planka-setup --version
Options:
  DB_HOST                   The host IP for the postgres server. [default: 127.0.0.1]
  DB_PASSWORD               Password for the postgres server. [default: planka]
  DB_PORT                   Port fo the postgres server. [default: 5432]
  DB_NAME                   Postgres database name. [default: planka]
  DB_USER                   Username for the postgres server. [default: postgres]
  PROJECT_NAME              The name for the main project.
  -i --import               Import NMAP File.
  -n --new                  Set up a new Project.
  -h --help                 Show this message.
  --version                 Show version.
  -l --log-level=LEVEL      If specified, then the log level will be set to
                            the specified value.  Valid values are "debug", "info",
                            "warning", "error", and "critical". [default: info]
"""
# Standard Python Libraries
import logging
from typing import Dict

# Third-Party Libraries
from docopt import docopt
import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    """Create connection to postgres database.

    Args:
        db_name (string): Database Name
        db_user (string): Database Username
        db_password (string): Database password
        db_host (string): Database Hostname
        db_port (string): Database Port Number

    Raises:
        e: Connection errors.

    Returns:
        Psycopg2 Connection: A connection to the postgres database.
    """

    logging.debug("Connecting to postgres")
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        logging.info("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        raise e

    return connection


def execute_read_query(connection, query):
    """Execute a read query on the postgres database.

    Args:
        connection (Psycopg2 Connection): The connection to the postgres database.
        query (string): The SQL query to be run.

    Returns:
        list(tuples): The results of the SQL query.
    """

    logging.debug(f"Executing Read Query: {query}")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logging.debug("Query was successful.")
        return result
    except OperationalError as e:
        logging.error(f"The error '{e}' occurred")


def execute_query(connection, query):
    """Execute a query to change the database.

    Args:
        connection (Psycopg2 Connection): The connection to the postgres database.
        query (string): The SQL query to be run.
    """

    logging.debug(f"Executing Action: {query}")
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info("Query executed successfully")
    except OperationalError as e:
        logging.error(f"The error '{e}' occurred")


def main():
    """Set up logging, connect to Postgres, call requested function(s)."""
    args: Dict[str, str] = docopt(__doc__, version="0.1")

    # Set up logging
    log_level = args["--log-level"]
    try:
        logging.basicConfig(
            format="\n%(levelname)s: %(message)s", level=log_level.upper()
        )
    except ValueError:
        logging.critical(
            f'"{log_level}"is not a valid logging level. Possible values are debug, info, warning, and error.'
        )
        return 1

    # Set up database connection
    try:
        connection = create_connection(
            args["DB_NAME"],
            args["DB_USER"],
            args["DB_PASSWORD"],
            args["DB_HOST"],
            args["DB_PORT"],
        )
    except OperationalError as e:
        logging.error(f"The connection error '{e}' occurred")
        return 1

    if args["--new"]:
        print("Code Stub for new project")

    elif args["--import"]:
        print("Code stub for import.")


if __name__ == "__main__":
    main()
