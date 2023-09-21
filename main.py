# These lines of code are importing specific functions or modules from different files.
from datetime import datetime
from aws_helpers import read_from_queue
from postgres_helpers import get_db_connection, write_to_postgres
from utils import hash_pii

# Configuration
AWS_ENDPOINT_URL = "http://localhost:4566/_aws/sqs/messages"
QUEUE_URL = "http://queue.localhost.localstack.cloud:4566/000000000000/login-queue"
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "host": "localhost",
    "password": "postgres",
    "port": "5432",
}

# The `if __name__ == "__main__":` block is a common idiom in Python that allows a script to be
# executed directly as the main program, but not when it is imported as a module.
if __name__ == "__main__":
    print("Connecting to the Queue")
    print("Reading from Queue")
    raw_data = read_from_queue(AWS_ENDPOINT_URL, QUEUE_URL)
    print("Queue Data : ", raw_data)

    if raw_data:
        print("Masking the Queue Data")
        masked_data = hash_pii(raw_data)
        print(f"Masked Data is {masked_data}")

        print("Connecting to PostgreSQL Database")
        conn = get_db_connection(DB_CONFIG)
        print("Writing to Postgres")
        write_to_postgres(conn, masked_data)
        print("Data Written to PostgreSQL")
