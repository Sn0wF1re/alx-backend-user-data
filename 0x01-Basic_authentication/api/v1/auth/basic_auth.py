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
    pass
