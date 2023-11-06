#!/usr/bin/env python3
""" Auth class
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if the path requires authentication """
        if path is None or not excluded_paths:
            return True


        # Add a slash at the end of path if not present for comparison
        if path[-1] != '/':
            path += '/'


        # Check if the path is in the list of excluded paths
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                if path == excluded_path:
                    return False
            else:
                if path == excluded_path + '/':
                    return False
                
        return True


    def authorization_header(self, request=None) -> str:
        """ Looks for the authorization header """
        return None


    def current_user(self, request=None) -> User:
        """ Returns the current user """
        return None
