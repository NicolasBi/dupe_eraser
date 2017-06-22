import dupe_eraser.src.getters.get_parameter_name as gpn
from dupe_eraser.src.getters.get_output_message import string_to_verbosity
import dupe_eraser.src.getters.environment as env


class CheckAndSafeOptionsActivated(Exception):
    def __init__(self):
        Exception.__init__(self, "Check mode and Safe mode are incompatibles.")


_KEY_CHECK = gpn.check().split()[-1]
_KEY_LOW_MEMORY = gpn.low_memory().split()[-1]
_KEY_RECURSIVE = gpn.recursive().split()[-1]
_KEY_SAFE = gpn.safe().split()[-1]
_KEY_SAFE_DIRECTORY = gpn.safe_directory().split()[-1]
_KEY_VERBOSITY = gpn.verbosity().split()[-1]
_KEY_HASHING_ALGORITM = gpn.hashing_algorithm().split()[-1]


def clean_arguments(args: dict) -> None:
    env.check = args[_KEY_CHECK]
    env.low_memory = args[_KEY_LOW_MEMORY]
    env.recursive = args[_KEY_RECURSIVE]
    env.safe = args[_KEY_SAFE]
    env.safe_directory = args[_KEY_SAFE_DIRECTORY]
    env.verbosity = string_to_verbosity(args[_KEY_VERBOSITY])
    env.hashing_algorithm = args[_KEY_HASHING_ALGORITM]

    if env.safe and env.check:
        raise CheckAndSafeOptionsActivated()

    check_hashing_algorithm_supported(env.hashing_algorithm)
