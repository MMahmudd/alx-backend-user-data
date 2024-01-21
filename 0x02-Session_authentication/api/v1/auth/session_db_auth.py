#!/usr/bin/env python3
"""
Define_class_SessionDButh
"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Definition_of_SessionDBAuth _lass_that_persists_session_data
    in_a_database
    """

    def create_session(self, user_id=None):
        """
        Create a Session_ID_for_a_user_id
        Args:
           user_id (str):_user_id
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        kw = {
            "user_id": user_id,
            "session_id": session_id
        }
        user = UserSession(**kw)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a user_ID_based_on a_session _D
        Args:
            session_id (str): session_ID
        Return:
            user_id_or None_if_session_id is_None_or_not_a_string
        """
        user_id = UserSession.search({"session_id": session_id})
        if user_id:
            return user_id
        return None

    def destroy_session(self, request=None):
        """
        Destroy_a_UserSession_instance_based_on a
        Session ID_from_a_request_cookie
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            user_session[0].remove()
            return True
        return False
