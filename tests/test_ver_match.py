# coding: utf-8
if __name__ == '__main__':
    import path_imports
from os import minor
from pathlib import Path
from typing import Iterator, Union
from verr import VERSION as v_ver, __version__ as v_dunder

import unittest


class TestVersionMatch(unittest.TestCase):

    def test_version_match(self):
        setup_ver = get_setup_ver()
        self.assertEqual(setup_ver, v_ver)
        self.assertEqual(setup_ver, v_dunder)

def get_setup_ver() -> Union[str, None]:
    root = Path(__file__).parent.parent
    setup_file = root / 'setup.py'
    ver = None
    with open(setup_file, 'r') as s_file:
        ver = get_ver_num(s_file)
    return ver


def get_ver_num(file: Iterator[str]) -> Union[str, None]:
    ver_keys = ('MAJOR', 'MINOR', 'MICRO')
    ver_len = len(ver_keys)
    line_parts = ver_finder(file, *ver_keys)
    ver_dict = {}
    found_count = 0
    for line in line_parts:
        parts = line.split('=')
        if len(parts) != 2:
            continue
        key = parts[0].strip()
        value = parts[1].strip()
        ver_dict[key] = value
        found_count += 1
        if found_count >= ver_len:
            break
    for k in ver_keys:
        if not k in ver_dict:
            return None
    return f"{ver_dict[ver_keys[0]]}.{ver_dict[ver_keys[1]]}.{ver_dict[ver_keys[2]]}"

def ver_finder(file:Iterator[str], *parts:str) -> str:
    for line in file:
        for part in parts:
            if line.startswith(part):
                yield line


if __name__ == '__main__':
    unittest.main()
