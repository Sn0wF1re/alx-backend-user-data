#!/usr/bin/env python3
"""
Create a class to manage API authentication
that inheritsfrom Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Uses Basic Authentication
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Returns the Base64 part
        of the Authorization header for a Basic Authentication
        """
        if authorization_header is None \
                or not isinstance(authorization_header, str) \
                or not authorization_header.startswith('Basic '):
            return None

        val = authorization_header.split()
        return val[1]
