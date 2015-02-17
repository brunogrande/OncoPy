#!/usr/bin/env python


class CancerApiException(Exception):
    """Base class for Cancer_API exceptions"""
    pass


class NotConnectedToDatabase(CancerApiException):
    """A database connection is needed for running
    this method.
    """
    pass


class IllegalVariableDefinition(CancerApiException):
    """A variable was attempted to be defined in a non-canonical way."""
    pass
