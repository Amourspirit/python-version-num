# coding: utf-8
from subprocess import run


def main():
    cmd_str = 'twine upload --repository-url https://test.pypi.org/legacy/ dist/*'
    res = run(cmd_str.split(' '))
    if res and res.returncode != 0:
        print(res)

if __name__ == '__main__':
    main()
