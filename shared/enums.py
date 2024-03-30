from enum import Enum


class Status(Enum):
    VALID = 'valid'
    INVALID = 'invalid'
    PENDING = 'pending'


class FlowStatus(Enum):
    COMPLETE = 'complete'
    INCOMPLETE = 'incomplete'
    NOT_STARTED = 'not_started'
