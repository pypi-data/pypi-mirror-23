"""
This package contains the GitLab implementations of the interfaces in
server.git.Interfaces. GitLab drops the support of API version 3 as of
August 22, 2017. So, IGitt adopts v4 to stay future proof.
"""
from IGitt.Interfaces import AccessLevel
from IGitt.Interfaces import _fetch
from IGitt.Utils import CachedDataMixin

BASE_URL = 'https://gitlab.com/api/v4'


class GitLabMixin(CachedDataMixin):
    """
    Base object for things that are on GitLab.
    """

    def _get_data(self):
        return get(self._token, self._url)


def get(token: str, url: str, params: dict=None):
    """
    Queries GitLab on the given URL for data.

    :param token: An OAuth token.
    :param url: E.g. ``/repo``
    :param params: The query params to be sent.
    :return:
        A dictionary or a list of dictionary if the response contains multiple
        items (usually in case of pagination) and the HTTP status code.
    :raises RunTimeError:
        If the response indicates any problem.
    """
    return _fetch(BASE_URL, 'get', {'access_token': token},
                  url, query_params=params)


def post(token: str, url: str, data: dict):
    """
    Posts the given data onto GitLab.

    :param token: An OAuth token.
    :param url: The URL to access, e.g. ``/repo``.
    :param data: The data to post.
    :return:
        A dictionary or a list of dictionary if the response contains multiple
        items (usually in case of pagination) and the HTTP status code.
    :raises RunTimeError:
        If the response indicates any problem.
    """
    return _fetch(BASE_URL, 'post', {'access_token': token}, url, data)


def put(token: str, url: str, data: dict):
    """
    Puts the given data onto GitLab.

    :param token: An OAuth token.
    :param url: The URL to access, e.g. ``/repo``.
    :param data: The data to post.
    :return:
        A dictionary or a list of dictionary if the response contains multiple
        items (usually in case of pagination) and the HTTP status code.
    :raises RunTimeError:
        If the response indicates any problem.
    """
    return _fetch(BASE_URL, 'put', {'access_token': token}, url, data)


def delete(token: str, url: str, params: dict=None):
    """
    Sends a delete request to the given URL on GitLab.

    :param token: An OAuth token.
    :param url: The URL to access, e.g. ``/repo``.
    :param params: The query params to be sent.
    :raises RuntimeError: If the response indicates any problem.
    """
    _fetch(BASE_URL, 'delete', {'access_token': token},
           url, query_params=params)
