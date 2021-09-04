"""Simplified Python scripting"""
__doc__ = "Simplified Python scripting"
import sys
from typing import List, NamedTuple, NoReturn, Union
import types
import subprocess
import os

__version__: str = "0.1.0"


class SubprocessOutput(NamedTuple):
    """The simplified output of a subprocess response"""

    stdout: str
    stderr: str


class Main(types.ModuleType):
    """The hacky main class to act as a module"""

    # pylint: disable=C0103

    ### Subprocess commands ###

    def __call__(self, command: Union[str, List[str]]) -> SubprocessOutput:
        """Run a subprocess and raise an error if the subprocess failed."""
        proc = subprocess.run(
            [command] if isinstance(command, str) else command,
            check=True,
            capture_output=True,
        )
        return SubprocessOutput(proc.stdout.decode(), proc.stderr.decode())

    @staticmethod
    def s(command: str) -> int:
        """An alias for os.system"""
        return os.system(command)

    ### Formatting commands ###

    @staticmethod
    def i(message: str) -> bool:
        """Send an info message and return a boolean indicating if colors were available."""
        if os.name == "nt" or not sys.stdout.isatty():
            print("Info: " + message)
            return False
        print("\x1b[36m" + "Info: " + message + "\x1b[0m")
        return True

    @staticmethod
    def w(message: str) -> bool:
        """Send a warning and return a boolean indicating if colors were available."""
        if os.name == "nt" or not sys.stdout.isatty():
            print("Warning: " + message)
            return False
        print("\x1b[33m" + "Warning: " + message + "\x1b[0m")
        return True

    @staticmethod
    def e(message: str, status: int = 1) -> NoReturn:
        """Send an error message and exit with the exit code `status`."""
        if os.name == "nt" or not sys.stdout.isatty():
            print("Error: " + message)
        else:
            print("\x1b[31m" + "Error: " + message + "\x1b[0m")
        sys.exit(status)


sys.modules[__name__] = Main("x", __doc__)
