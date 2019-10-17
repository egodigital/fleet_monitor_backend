"""
Module contains global project definitions.
"""

from pathlib import Path
import platform


def get_prj_root():
    return Path(__file__).parent.parent.resolve()


def get_docs_dir():
    return get_prj_root() / "docs"


def get_scripts_dir():
    return get_prj_root() / "scripts"


def get_out_dir():
    return get_prj_root() / "out"


def get_platform():
    platform_ = platform.system().lower()
    if platform_ == "darwin":
        return "mac"
    return platform_


def get_os_native_script_file_extensions():
    return {
        'windows': '.bat',
        'linux': '.sh',
    }


def get_home_directory():
    return str(Path.home())
