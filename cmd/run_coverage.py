# coding: utf-8
from subprocess import run

def main():
    cmd_str = 'coverage run --source=verr -m unittest discover tests'
    res = run(cmd_str.split(' '))
    run(['coverage', 'report'])

if __name__ == '__main__':
    main()
