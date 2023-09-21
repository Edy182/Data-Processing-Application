# Data Processing Application

## Overview

This is a Python-based data processing application that reads messages from an AWS SQS queue, hashes Personally Identifiable Information (PII), and then stores the processed records into a PostgreSQL database.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Code](#running-the-code)
- [Deployment](#deployment)
- [Next Steps](#next-steps)
- [Questions](#questions)

## Getting Started

### Prerequisites

- AWS SQS Queue
- PostgreSQL Database
- Python 3.x
- Boto3 Library
- Psycopg2 Library


### Docker Setup

Before running the application, make sure to spin up the Docker containers using the following command:

```bash
docker-compose up -d
```

### Python Virtual Environment

It's recommended to set up a Python virtual environment before running the application. Run the following commands:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Running the Code

1. Clone the repository.
2. Install the required packages.
3. Run `main.py`.

```bash
pip install boto3 psycopg2-binary
```

```bash
python main.py
```

## Deployment

### How would you deploy this application in production?

To deploy this application in production, I would use a containerization solution like Docker and orchestrate it using Kubernetes for better scalability and management.

### What other components would you add to make this production-ready?

- Error handling and logging
- Data validation
- Unit and integration tests
- CI/CD pipeline

### How can this application scale with a growing dataset?

This application can be scaled by:

1. Utilizing database sharding in PostgreSQL.
2. Increasing the number of consumer instances reading from the SQS queue.
3. Employing Kubernetes for auto-scaling based on workload.

### How can PII be recovered later on?

PII recovery can be challenging due to the one-way nature of the hashing algorithm. An alternative would be to use encryption so that the PII can be decrypted when necessary.

## Next Steps

- Improve the database schema for better query performance.
- Add monitoring and alerting.
- Implement data caching for frequent queries.

## Questions

### Assumptions Made

- All incoming messages are well-formatted JSON strings.
- The PostgreSQL database is already set up and configured.

### Development Decisions

- **Reading Messages**: Used Boto3 library to interact with AWS SQS.
- **Data Structures**: Utilized Python dictionaries for ease of use and readability.
- **Masking PII**: Used SHA256 hashing.
- **Postgres Connection**: Utilized Psycopg2 for connecting and writing to PostgreSQL.
