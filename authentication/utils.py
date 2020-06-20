from django.conf import settings
from base.utils import generate_string_random_id


def get_full_user_path(instance):
    """return the full user path including the user id"""
    return f"{settings.DEFAULT_USER_PATH}/{instance.user.id}"


def get_avatar_path(instance, filename):
    """upload the avatar image and put the user name in the bath of the image """
    random_id = generate_string_random_id()
    user_path = get_full_user_path()
    return f'{user_path}/avatar/{random_id}/{filename}'
