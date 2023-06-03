#!/usr/bin/env python3
"""
Create class SessionExpAuth
"""
from .session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    inherits from SessionAuth
    """
    def __init__(self) -> None:
        """
        Initialize class
        """
        super().__init__
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        create a session Id for a user Id
        """
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        return user id based on session id
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None

        data = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return data['user_id']
        if 'created_at' not in data:
            return None
        now = datetime.now()
        duration = timedelta(seconds=self.session_duration)
        if data['created_at'] + duration < now:
            return None
        return data['user_id']
