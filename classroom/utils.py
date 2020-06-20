from authentication.utils import get_full_user_path
from base.utils import generate_string_random_id


def get_classroom_logo_path(instance, filename):
    """return the avatar classroom logo image path"""
    random_id = generate_string_random_id()
    user_path = get_full_user_path(instance)
    return f'{user_path}/classroom/logos/{random_id}/{filename}'


def get_classroom_bg_path(instance, filename):
    """return the avatar classroom logo image path"""
    random_id = generate_string_random_id()
    user_path = get_full_user_path(instance)
    return f'{user_path}/classroom/backgrounds/{random_id}/{filename}'


def get_attachment_path(instance, filename):
    """return the attachment path that it should be in"""
    random_id = generate_string_random_id()
    user_path = get_full_user_path(instance)
    return f'{user_path}/attachments/{random_id}/{filename}'
