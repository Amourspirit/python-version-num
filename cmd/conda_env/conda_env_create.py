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
    # res = run(['conda', 'deactivate'])
    # if res and res.returncode != 0:
    #     print(res)
    #     return None
    cmd_str = f"conda env create --prefix {ENV_NAME} --file {YML_FILE}"
    res = run(cmd_str.split())
    if res and res.returncode != 0:
        print(res)


if __name__ == '__main__':
    main()

