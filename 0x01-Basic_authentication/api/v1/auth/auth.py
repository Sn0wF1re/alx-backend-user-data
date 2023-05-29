#!/usr/bin/env python3
"""
Create a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manages API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check for paths that require authentication
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != '/':
            path += '/'
        for exc in excluded_paths:
            if exc[-1] != '/':
                exc += '/'

        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """
        returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return None
        """
        return None
