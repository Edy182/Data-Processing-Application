# The `import hashlib` statement is importing the `hashlib` module in Python. The `hashlib` module
# provides various hashing algorithms, such as MD5, SHA1, and SHA256, which can be used to securely
# hash data. In this code, the `hashlib` module is used to hash sensitive fields in the data.
import hashlib


def version_to_int(version_str):
    """
    The function `version_to_int` converts a version string into an integer by removing the dots and
    converting the resulting string into an integer.

    :param version_str: A string representing a version number in the format "x.y.z"
    :return: an integer representation of the input version string.
    """
    return int("".join(version_str.split(".")))


def hash_pii(data):
    """
    The function `hash_pii` takes a list of records and hashes the device ID and IP address, and
    converts the app version to an integer.

    :param data: The `data` parameter is a list of dictionaries. Each dictionary represents a record and
    contains the following keys:
    :return: the modified data with hashed PII (Personally Identifiable Information) values.
    """
    for record in data:
        record["masked_device_id"] = hashlib.sha256(
            record["device_id"].encode()
        ).hexdigest()
        record["masked_ip"] = hashlib.sha256(record["ip"].encode()).hexdigest()
        record["app_version"] = version_to_int(record["app_version"])
    return data
