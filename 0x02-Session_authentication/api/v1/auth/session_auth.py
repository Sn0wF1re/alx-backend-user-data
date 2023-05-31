#!/usr/bin/env python3
"""
Create class SessionAuth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


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
