import sys
from pathlib import Path

SYSPATH = str(Path(__file__).parent.parent)


def set_path():
    if SYSPATH not in sys.path:
        sys.path.append(SYSPATH)


set_path()
