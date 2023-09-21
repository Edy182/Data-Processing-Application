# The code is importing the `boto3` library, which is the AWS SDK for Python, and the `json` library,
# which provides functions for working with JSON data.
import boto3
import json


def read_from_queue(aws_endpoint_url, queue_url):
    """
    The function reads messages from an AWS SQS queue using the provided endpoint URL and queue URL.
    
    :param aws_endpoint_url: The `aws_endpoint_url` parameter is the URL of the AWS endpoint for the SQS
    service. This is typically in the format `https://sqs.{region}.amazonaws.com`, where `{region}` is
    the AWS region where your SQS queue is located
    :param queue_url: The `queue_url` parameter is the URL of the Amazon Simple Queue Service (SQS)
    queue from which you want to read messages
    :return: the result of calling the `process_sqs_messages` function with the `messages`, `queue_url`,
    and `client` as arguments.
    """
    client = boto3.client("sqs", region_name="us-east-1", endpoint_url=aws_endpoint_url)
    try:
        messages = client.receive_message(QueueUrl=queue_url)
    except Exception as e:
        print(f"An error occurred while reading from the queue: {e}")
        return []
    return process_sqs_messages(messages,queue_url,client)


def process_sqs_messages(messages, queue_url, client):
    """
    The function processes messages from an SQS queue by extracting the message body, deleting the
    message from the queue, and returning the processed messages.
    
    :param messages: The `messages` parameter is a dictionary that contains the messages received from
    an Amazon Simple Queue Service (SQS) queue. It should have the following structure:
    :param queue_url: The `queue_url` parameter is the URL of the Amazon Simple Queue Service (SQS)
    queue from which you want to process messages. It is a string that represents the unique identifier
    of the queue
    :param client: The `client` parameter is an instance of the AWS SDK client for Amazon Simple Queue
    Service (SQS). It is used to interact with the SQS service and perform operations such as deleting
    messages from a queue
    :return: a list of processed messages.
    """
    processed_messages = []
    if "Messages" in messages:
        for msg in messages["Messages"]:
            body = json.loads(msg["Body"])
            processed_messages.append(body)
            receipt_handle = msg["ReceiptHandle"]
            client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
    return processed_messages
