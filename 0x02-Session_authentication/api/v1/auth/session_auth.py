#!/usr/bin/env python3
"""
Create class SessionAuth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    Implements session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        sessionId = str(uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        returns a User instance based on a cookie value
        """
        sessionId = self.session_cookie(request)
        user_id = self.user_id_for_session_id(sessionId)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        deletes the user session / logout
        """
        sessionId = self.session_cookie(request)
        user_id = self.user_id_for_session_id(sessionId)
        if request and sessionId and user_id:
            self.user_id_by_session_id.pop(sessionId)
            return True

        return False
