#!/usr/bin/env python3
"""
Create a class to manage API authentication
that inheritsfrom Auth
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded value
        of a Base64 string base64_authorization_header
        """
        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None

        try:
            data = base64.b64decode(base64_authorization_header)
            return data.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password
        from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None \
                or not isinstance(decoded_base64_authorization_header, str) \
                or ':' not in decoded_base64_authorization_header:
            return (None, None)
        data = decoded_base64_authorization_header.split(':')
        return (data[0], data[1])
