:: # --- Virtual Python environment
:: echo "Installing project dependendencies into virtual Python environment."
:: set PYTHON_VERSION=3.6
:: set PRJ_ROOT=%1
:: set VENV_DIR=%PRJ_ROOT%\venv

:: echo %PRJ_ROOT%
:: echo %VENV_DIR%

:: IF NOT EXIST %VENV_DIR% (
::   virtualenv -p python%PYTHON_VERSION% %VENV_DIR%
::)
:: source %VENV_DIR%\Scripts\activate
:: pip install -r %PRJ_ROOT%\requirements.txt

:: # --- PYTHONPATH environment variable
SET PRJ_ROOT=%~dp0
echo %PRJ_ROOT%
set PYTHONPATH=%PYTHONPATH%;
%PRJ_ROOT%\backend%PRJ_ROOT%\backend\api;^
%PRJ_ROOT%\backend\api\swagger_client;^
%PRJ_ROOT%\backend\api\swagger_client\api;^
%PRJ_ROOT%\backend\api\swagger_client\models;^
%PRJ_ROOT%\backend\snippets;^
