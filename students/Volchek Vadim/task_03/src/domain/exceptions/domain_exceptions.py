"""
Domain exceptions for bug tracker.
"""


class DomainException(Exception):
    pass


class InvalidBugStateException(DomainException):
    pass


class InvalidAssigneeGroupException(DomainException):
    pass
