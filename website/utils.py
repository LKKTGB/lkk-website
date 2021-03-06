from functools import wraps
import re

from django.conf import settings
from django.db import close_old_connections
from urllib.parse import urlparse, parse_qs
import arrow


def handle_old_connections(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        close_old_connections()
        result = f(*args, **kwargs)
        close_old_connections()
        return result
    return wrapper


def is_valid_youtube_id(youtube_id):
    pattern = r'[A-Za-z0-9\-\_]{11}'
    return True if re.match(pattern, youtube_id) else False


def get_youtube_id_from_url(url):
    # reference
    # https://stackoverflow.com/questions/45579306/get-youtube-video-url-or-youtube-video-id-from-a-string-using-regex
    url_parsed = urlparse(url)

    # validate host
    host = url_parsed.netloc
    if host not in ['youtube.com', 'www.youtube.com', 'youtu.be']:
        return

    # get youtube id from url
    query_v = parse_qs(url_parsed.query).get('v')
    youtube_id = None
    if query_v:
        # case1: http://youtube.com/watch?v=iwGFalTRHDA
        youtube_id = query_v[0]
    else:
        # case2: http://youtu.be/t-ZRX8984sc
        paths = url_parsed.path.split('/')
        if paths:
            youtube_id = paths[-1]

    # validate youtube_id
    if youtube_id and is_valid_youtube_id(youtube_id):
        return youtube_id


def format_time(datetime, fmt):
    return arrow.Arrow.fromdatetime(datetime).to(settings.TIME_ZONE).format(fmt)
