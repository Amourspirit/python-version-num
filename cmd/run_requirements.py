from subprocess import run
import pathlib
import os

ROOT_PATH = pathlib.Path(__file__).parent.parent
CONDA_ENV_NAME = 'python-verr'

def main():
    global ROOT_PATH
    global CONDA_ENV_NAME
    export_path = ROOT_PATH / "requirements" / "conda"
    os.chdir(str(export_path))
   
    cmd_str = "conda list --explicit"
    with open('pkgs.txt', 'w') as fhandle:
        res = run(cmd_str.split(), stdout=fhandle)
        if res and res.returncode != 0:
            print(res)
    cmd_str = F"conda env export --name {CONDA_ENV_NAME}"
    with open(f"{CONDA_ENV_NAME}.yml", 'w') as fhandle:
        res = run(cmd_str.split(), stdout=fhandle)
        if res and res.returncode != 0:
            print(res)

if __name__ == '__main__':
    main()
