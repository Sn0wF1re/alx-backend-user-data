#!/usr/bin/env python3
"""
define a _hash_password method
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Returns a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
