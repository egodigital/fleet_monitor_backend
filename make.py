import os
from pathlib import Path
import subprocess
import sys

from backend.definitions import get_docs_dir
from backend.definitions import get_platform
from backend.definitions import get_prj_root
from backend.definitions import get_scripts_dir
from backend.definitions import get_os_native_script_file_extensions


_TARGET_INSTALL = "install"
_TARGETS = [
    _TARGET_INSTALL,
]


def print_help():
    print("Usage: make.py <target> [OPTIONS]")
    print(f"Targets: {', '.join(_TARGETS)}.")
    print(f"### {'install':20} | No options.")


def run_target_install(platform, ext):
    if platform == "linux":
        subprocess.call(["bash", get_scripts_dir() /
                         get_platform().lower() / str(_TARGET_INSTALL + ext), get_prj_root()])
    elif platform == "windows":
        # TODO: Make this work
        # subprocess.call(["start", get_scripts_dir() /
        #                  get_platform().lower() / str
        #                  (_TARGET_INSTALL + ext), get_prj_root()
        #                  ])
        raise NotImplementedError(
            "TODO: Implement installation creation for Windows")
    elif platform == "mac":
        raise NotImplementedError(
            "TODO: Implement installation creation for Mac")


def run(args):
    if len(args) < 2:
        print_help()
        return
    target = args[1]
    platform = get_platform()
    ext = get_os_native_script_file_extensions()[platform]
    if target == _TARGET_INSTALL:
        run_target_install(platform, ext)
    else:
        print_help()


def main():
    run(sys.argv)


if __name__ == "__main__":
    main()
