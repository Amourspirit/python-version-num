# coding: utf-8
from subprocess import run

def main():
    cmd_str = 'coverage run --source=verr -m unittest discover tests'
    res = run(cmd_str.split(' '))
    if res and res.returncode != 0:
        print(res)
    res = run(['coverage', 'report'])
    if res and res.returncode != 0:
        print(res)

if __name__ == '__main__':
    main()
