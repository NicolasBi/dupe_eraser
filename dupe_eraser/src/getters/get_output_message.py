import json
import os
from enum import IntEnum, Enum

import dupe_eraser.src.getters.environment as env


_PATH_OUTPUT_MESSAGES = "../../res/default_values.json"
VERBOSE_KEY_PREFIX = "verbose_"


class Verbosity(IntEnum):
    QUIET = 0
    NORMAL = 1
    VERBOSE = 2


def string_to_verbosity(string: str) -> Verbosity:
    string = string.lower()
    if string == "quiet":
        return Verbosity.QUIET
    elif string == "normal":
        return Verbosity.NORMAL
    elif string == "verbose":
        return Verbosity.VERBOSE
    else:
        raise UnknownVerbosity(string)


class UnknownVerbosity(Exception):
    def __init__(self, verbosity):
        Exception.__init__(self, "The verbosity level \"{verbosity}\" is unknown "
                                 "to the software.".format(verbosity=verbosity))


class Message(Enum):
    # Verbose messages
    WELCOME_MESSAGE = VERBOSE_KEY_PREFIX + "welcome_message"
    GOODBYE_MESSAGE = VERBOSE_KEY_PREFIX + "goodbye_message"
    PARSING_ARGUMENTS = VERBOSE_KEY_PREFIX + "parsing_arguments"
    CLEANING_ARGUMENTS = VERBOSE_KEY_PREFIX + "cleaning_arguments"
    EXAMINING_FILE = VERBOSE_KEY_PREFIX + "examining_file"

    # Normal messages
    DELETING_FILE = "deleting_file"
    MOVING_FILE = "moving_file"


def _is_a_normal_message(message_key: str) -> bool:
    global VERBOSE_KEY_PREFIX

    return message_key[:len(VERBOSE_KEY_PREFIX)] != VERBOSE_KEY_PREFIX


def _get_message_from_file(value):
    global _PATH_OUTPUT_MESSAGES

    path = os.path.join(os.path.dirname(__file__),
                        _PATH_OUTPUT_MESSAGES)
    with open(path) as file:
        return json.load(file)[value]


def vprint(message: Message) -> None:
    message_key = message.value

    if env.verbosity == Verbosity.QUIET:
        return None
    elif env.verbosity == Verbosity.NORMAL:
        if _is_a_normal_message(message_key):
            message = _get_message_from_file(message_key)
        else:
            message = ""
    elif env.verbosity == Verbosity.VERBOSE:
        message = _get_message_from_file(message_key)
    else:
        raise UnknownVerbosity(env.verbosity)

    print(message, end="", sep="")


if __name__ == '__main__':
    pass
