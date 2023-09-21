# The code `import psycopg2` is importing the `psycopg2` module, which is a PostgreSQL adapter for
# Python. This module allows Python programs to connect to and interact with PostgreSQL databases.
import psycopg2
from datetime import datetime


def get_db_connection(db_config):
    """
    The function `get_db_connection` establishes a connection to a PostgreSQL database using the
    provided configuration and returns the connection object.

    :param db_config: The `db_config` parameter is a dictionary that contains the configuration details
    required to establish a connection to a PostgreSQL database. It typically includes the following
    key-value pairs:
    :return: a database connection object if the connection is successful. If there is an error while
    connecting to the database, it will print an error message and return None.
    """
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None


def write_to_postgres(conn, data):
    """
    The function `write_to_postgres` inserts data into a PostgreSQL database table called `user_logins`.

    :param conn: The `conn` parameter is the connection object that represents the connection to the
    PostgreSQL database. It is used to establish a connection to the database and execute SQL queries
    :param data: The `data` parameter is a list of dictionaries. Each dictionary represents a record to
    be inserted into the `user_logins` table in the PostgreSQL database
    :return: nothing.
    """
    if conn is None:
        return
    cur = conn.cursor()
    try:
        for record in data:
            cur.execute(
                "INSERT INTO user_logins VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    record["user_id"],
                    record["device_type"],
                    record["masked_ip"],
                    record["masked_device_id"],
                    record["locale"],
                    record["app_version"],
                    datetime.now(),
                ),
            )
        conn.commit()
    except Exception as e:
        print(f"An error occurred while inserting data into the database: {e}")
    finally:
        cur.close()
        conn.close()
