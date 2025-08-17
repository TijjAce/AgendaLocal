@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

echo === Vérification de Python ===
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installé. Téléchargement...
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe -OutFile python_installer.exe"
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
)

echo === Création de l'environnement virtuel ===
IF NOT EXIST venv (
    python -m venv venv
)

echo === Activation du venv ===
CALL venv\Scripts\activate.bat

echo === Mise à jour de pip ===
python -m pip install --upgrade pip

echo === Installation des dépendances ===
IF NOT EXIST requirements.txt (
    echo requirements.txt introuvable !
    exit /b 1
)
pip install -r requirements.txt
pip install xhtml2pdf

echo === Migrations Django ===
python manage.py makemigrations
python manage.py migrate

echo === Importation des pages ===
python import_pages.py

echo === Création du raccourci sur le bureau ===
set DESKTOP=%USERPROFILE%\Desktop
set SHORTCUT=%DESKTOP%\AgendaLocal.lnk

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$WshShell = New-Object -ComObject WScript.Shell; `
   $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); `
   $Shortcut.TargetPath = 'cmd.exe'; `
   $Shortcut.Arguments = '/k cd /d \"%cd%\" && venv\Scripts\activate && python manage.py runserver'; `
   $Shortcut.IconLocation = '%cd%\agenda.ico'; `
   $Shortcut.Save()"

echo ✅ Installation terminée ! Lancez l'application via le raccourci sur le bureau.
pause

