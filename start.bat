@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: Vérifie si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installé. Téléchargement...
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe -OutFile python_installer.exe"
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
)

:: Crée un venv si absent
IF NOT EXIST venv (
    python -m venv venv
)

:: Active le venv
CALL venv\Scripts\activate.bat

:: Installe les dépendances
pip install --upgrade pip
pip install -r requirements.txt

:: Migration base
python manage.py migrate

:: Importation des pages
python import_pages.py

:: Création d'un raccourci sur le bureau
set DESKTOP=%USERPROFILE%\Desktop
set SHORTCUT=%DESKTOP%\MonProjet.lnk
set TARGET=python manage.py runserver

:: Utilisation de PowerShell pour créer le raccourci avec icône
powershell -Command ^
    "$WshShell = New-Object -ComObject WScript.Shell; ^
    $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); ^
    $Shortcut.TargetPath = 'cmd.exe'; ^
    $Shortcut.Arguments = '/k cd /d \"$(pwd)\" ^&^& venv\Scripts\activate ^&^& python manage.py runserver'; ^
    $Shortcut.IconLocation = '$(pwd)\agenda.ico'; ^
    $Shortcut.Save()"

echo ✅ Installation terminée ! Lancez l'application via le raccourci sur le bureau.

