import uuid


def generate_string_random_id():
    """generate a random string id then convert it to string"""
    random_id = uuid.uuid4()
    return str(random_id)
