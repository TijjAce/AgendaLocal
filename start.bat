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
) ELSE (
    echo L'environnement virtuel existe déjà.
)

:: Définir le chemin du Python du venv
set VENV_PY=%CD%\venv\Scripts\python.exe

echo === Vérification du Python du venv ===
"%VENV_PY%" --version
IF %ERRORLEVEL% NEQ 0 (
    echo Erreur : Python du venv introuvable.
    exit /b 1
)

echo === Mise à jour de pip ===
"%VENV_PY%" -m pip install --upgrade pip
IF %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de la mise à jour de pip.
    exit /b 1
)

echo === Installation des dépendances ===
IF NOT EXIST requirements.txt (
    echo requirements.txt introuvable !
    exit /b 1
)
"%VENV_PY%" -m pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de l'installation des dépendances.
    exit /b 1
)

:: Installer/mettre à jour xhtml2pdf et Django
"%VENV_PY%" -m pip install --upgrade xhtml2pdf django
IF %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de l'installation de xhtml2pdf ou Django.
    exit /b 1
)

echo === Vérification des dépendances ===
"%VENV_PY%" -c "import django, xhtml2pdf; print('Dépendances OK')"
IF %ERRORLEVEL% NEQ 0 (
    echo Certaines dépendances sont manquantes.
    exit /b 1
)

echo === Migrations Django ===
"%VENV_PY%" manage.py makemigrations
IF %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de makemigrations.
    exit /b 1
)
"%VENV_PY%" manage.py migrate
IF %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de migrate.
    exit /b 1
)

echo === Importation des pages ===
IF EXIST import_pages.py (
    "%VENV_PY%" import_pages.py
    IF %ERRORLEVEL% NEQ 0 (
        echo Erreur lors de l'importation des pages.
        exit /b 1
    )
) ELSE (
    echo import_pages.py introuvable.
)




@echo off
echo === Création du raccourci sur le bureau ===
set DESKTOP=%USERPROFILE%\Desktop

(
echo Set WshShell = WScript.CreateObject("WScript.Shell"^)
echo Set Shortcut = WshShell.CreateShortcut("%DESKTOP%\AgendaLocal.lnk"^)
echo Shortcut.TargetPath = "cmd.exe"
echo Shortcut.Arguments = "/k cd /d ""%CD%"" && %VENV_PY% manage.py runserver"
echo Shortcut.WorkingDirectory = "%CD%"
echo Shortcut.IconLocation = "%CD%\agenda.ico"
echo Shortcut.Save
) > create_shortcut.vbs

cscript //nologo create_shortcut.vbs
del create_shortcut.vbs


echo ✅ Installation terminée ! Lancez l'application via le raccourci sur le bureau.
pause

