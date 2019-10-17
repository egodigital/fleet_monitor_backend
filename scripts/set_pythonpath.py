from pathlib import Path
import os
import sys

# Identify platform by command line argument
args = sys.argv
platform = args[1]

prj_root = Path(__file__).parent.parent.parent.resolve()
packages = [
    prj_root,
    prj_root / "backend",
    prj_root / "backend" / "api",
    prj_root / "backend" / "api" / "swagger_client",
    prj_root / "backend" / "api" / "swagger_client" / "api",
    prj_root / "backend" / "api" / "swagger_client" / "models",
    prj_root / "backend" / "snippets",
    prj_root / "backend" / "core",
]

home_dir = Path.home()


path_bashrc = home_dir / ".bashrc"
pythonpath = "export PYTHONPATH=\"$PYTHONPATH"
for p in packages:
    pythonpath += ":" + str(p)
pythonpath += "\""

with open(path_bashrc, "a") as f:
    f.write("\n" + pythonpath)
