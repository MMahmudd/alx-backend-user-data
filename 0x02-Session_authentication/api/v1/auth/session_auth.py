#!/usr/bin/env python3
"""
Definition_of_class_SessionAuth
"""
import base64
from uuid import uuid4
from typing import TypeVar

from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Implement_Session_Authorization_protocol_methods
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session_ID_for a user_with_id_user_id
        Args:
            user_id (str): user's_user_id
        Return:
            None is_user_id_is None_or_not a_string
            Session_ID_in_string_format
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a_user_ID based_on_a_session_ID
        Args:
            session_id (str): s_ession_ID
        Return:
            user_id_or_None_if_session_id is_None_or not_a_string
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Return a_user_instance_based_on_a_cookie_value
        Args:
            request : request_object_containing_cookie
        Return:
            User_instance
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        Deletes_a_user_session
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
