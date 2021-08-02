# coding: utf-8
from pathlib import Path
import sys
import os


def set_import_paths():
    script_path = Path(os.path.dirname(__file__)).parent
    test_path = script_path / "tests"
    version_path = script_path / "src"

    _paths = (test_path, script_path, version_path)
    i = 0
    for p in _paths:
        if not p in sys.path:
            sys.path.insert(i, str(p))
            i += 1


set_import_paths()
