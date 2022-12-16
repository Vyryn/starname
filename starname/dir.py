import os
import inspect
from typing import Optional
from types import FrameType

frame: Optional[FrameType] = inspect.currentframe()
if not frame:
    raise AssertionError("Cpython is not supported.")
ROOT = os.path.abspath(os.path.dirname(inspect.getframeinfo(frame).filename))


def database_path(database):
    return os.path.join(ROOT, "database", database)
