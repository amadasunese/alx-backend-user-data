#!/usr/bin/env python3
"""Regex-ing"""
import re


def filter_datum(fields, redaction, message, separator):
    return re.sub('|'.join([f'(?<={f}{separator})[^{separator}]*']) for f in fields, redaction, message)

