# coding: utf-8
from subprocess import run
import pathlib
import os

ROOT_PATH = pathlib.Path(__file__).parent.parent.parent
ENV_NAME = 'env'
ENV_PATH = ROOT_PATH / ENV_NAME
YML_FILE = 'environment.yml'

def main():
    os.chdir(str(ROOT_PATH))
    cmd_str = f"conda env update --prefix '{ENV_PATH}' --file {YML_FILE} --prune"
    res = run(cmd_str.split(' '))
    if res and res.returncode != 0:
        print(res)


if __name__ == '__main__':
    main()

