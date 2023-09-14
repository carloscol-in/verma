from enum import StrEnum, auto


class BumpLevel(StrEnum):
    PATCH = auto()
    MINOR = auto()
    MAJOR = auto()
