#!/usr/bin/env python3
"""
Define_SessionExpAuth_class
"""
import os
from datetime import (
    datetime,
    timedelta
)

from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    Definition_of_class_SessionExpAuth_that_adds_an
    expiration_date_to-a_Session_ID
    """
    def __init__(self):
        """
        Initialize_the_class
        """
        try:
            duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            duration = 0
        self.session_duration = duration

    def create_session(self, user_id=None):
        """
        Create_a_ Session_ID_for_a_user_id
        Args:
            user_id (str): user_id
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a_user_ID_based_on_a_session_ID
        Args:
            session_id (str): session_ID
        Return:
            user id or_None_if_session_id is_None_or not_a_string
        """
        if session_id is None:
            return None
        user_details = self.user_id_by_session_id.get(session_id)
        if user_details is None:
            return None
        if "created_at" not in user_details.keys():
            return None
        if self.session_duration <= 0:
            return user_details.get("user_id")
        created_at = user_details.get("created_at")
        allowed_window = created_at + timedelta(seconds=self.session_duration)
        if allowed_window < datetime.now():
            return None
        return user_details.get("user_id")
