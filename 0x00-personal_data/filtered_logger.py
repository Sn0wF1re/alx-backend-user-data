#!/usr/bin/env python3
"""
Write a function called filter_datum
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    returns the log message obfuscated
    """
    regex = re.compile(r'({})'.format('|'.join(map(re.escape, fields))))
    return re.sub(regex, redaction, message).split(separator, len(fields))
