# coding: utf-8
from subprocess import run
import pathlib
import os

TEST_DIR = 'tests'
ROOT_PATH = pathlib.Path(__file__).parent.parent
TEST_MODULES = ['verr']

def get_modules():
    global TEST_MODULES
    result = ''
    if len(TEST_MODULES) > 0:
        result = ' --cov=' + ' --cov='.join(TEST_MODULES)
    return result

def main():
    global ROOT_PATH
    global TEST_DIR
    os.chdir(str(ROOT_PATH))
    # print(ROOT_PATH)
    cov_mod = get_modules()
    # see: https://stackoverflow.com/questions/41748464/pytest-cannot-import-module-while-python-can
    cmd_str = f"python -m pytest {TEST_DIR}{os.sep}{cov_mod} --cov-report=html"
    print(cmd_str)
    res = run(cmd_str.split(' '))
    if res and res.returncode != 0:
        print(res)
    # print(cmd_str)

if __name__ == '__main__':
    main()
