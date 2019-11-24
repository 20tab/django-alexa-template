import os
import sys
from shutil import which


def check_virtualenv():
    if which("virtualenv") is None:
        print("\nPlease, install virtualenv. Follow this link: https://virtualenv.pypa.io/en/latest/\n")
        sys.exit(1)

check_virtualenv()