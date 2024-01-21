#!/usr/bin/env python3
"""
Definition_of_class_Auth
"""
import os
from flask import request
from typing import (
    List,
    TypeVar
)


class Auth:
    """
    Manages_the_API_authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether_given_path_requires_authentication or_not
        Args:
            - path(str): Url_path_to_be_checked
            - excluded_paths(List of str): List_of_paths_that_do_not_require
              authentication
        Return:
            - True_if_path_is_not in_excluded_paths, else_False
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns_the_authorization_heade_ from_a_request_object
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User_instance _rom_information_from a_request_object
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie_from_request
        Args:
            request : request_object
        Return:
            value of _my_session_id cookie from_request_object
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
