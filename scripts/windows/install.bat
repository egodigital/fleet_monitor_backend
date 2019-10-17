# --- Virtual Python environment
echo "Installing project dependendencies into virtual Python environment."
set PYTHON_VERSION=3.6
set PRJ_ROOT=%1
set VENV_DIR=%PRJ_ROOT%/venv

IF NOT EXIST %VENV_DIR% (
    virtualenv -p python%PYTHON_VERSION% %VENV_DIR%
)
source %VENV_DIR%/Scripts/activate
pip install -r %PRJ_ROOT%/requirements.txt

# --- PYTHONPATH environment variable
echo "Adding PYTHONPATH to ~/.bashrc"
python %PRJ_ROOT%/scripts/set_pythonpath.py windows
