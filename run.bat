@ECHO OFF
"%CD%\venv\Scripts\python.exe" "%CD%\core_util\Update.py" "%CD%"
"%CD%\venv\Scripts\pip.exe" "install" "-r" "%CD%\install_assets\requirements.txt"
"%CD%\venv\Scripts\python.exe" "%CD%\Main.py"
EXIT /B