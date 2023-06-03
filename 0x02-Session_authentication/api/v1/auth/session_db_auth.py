#!/usr/bin/env python3
"""
Create class SessionDBAuth
"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from flask import request


class SessionDBAuth(SessionExpAuth):
    """
    Inherits from SessionExpAuth
    """
    def create_session(self, user_id=None):
        """
        Create session id
        """
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return
        session = UserSession(**{
                'user_id': user_id,
                'session_id': session_id
        })
        session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        return user id based on session id
        """
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None

        if len(sessions) <= 0:
            return None
        return sessions[0].user_id

    def destroy_session(self, request=None) -> bool:
        """
        Destroy user session based on session id
        from request cookie
        """
        session_id = self.session_cookie(request)
        try:
            sessions = UserSession.search({'session_id': session_id})
            if len(sessions) <= 0:
                return False
            del sessions[0]
            return True
        except Exception:
            return False
