#!/bin/bash

# Vérifie si Python est installé
if ! command -v python3 &> /dev/null
then
    echo "Python3 n'est pas installé. Installation en cours..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS → utilise Homebrew
        if ! command -v brew &> /dev/null
        then
            echo "Homebrew n'est pas installé. Installez-le depuis https://brew.sh/"
            exit 1
        fi
        brew install python
    else
        echo "Distribution Linux détectée, veuillez installer Python manuellement."
        exit 1
    fi
fi

# Création du venv
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activation du venv
source venv/bin/activate

# Installation des dépendances
pip install --upgrade pip
pip install -r requirements.txt

# Migration de la base
python manage.py migrate

# Importation des pages
python import_pages.py

# Création du raccourci sur le bureau
DESKTOP="$HOME/Desktop"
SHORTCUT="$DESKTOP/MonProjet.command"

echo "#!/bin/bash
cd $(pwd)
source venv/bin/activate
python manage.py runserver" > "$SHORTCUT"

chmod +x "$SHORTCUT"

# Icône agenda.ico (seulement sur macOS via AppleScript)
if [[ "$OSTYPE" == "darwin"* ]]; then
    osascript <<EOF
    tell application "Finder"
        set iconFile to POSIX file "$(pwd)/agenda.ico" as alias
        set targetFile to POSIX file "$SHORTCUT" as alias
        try
            set theIcon to iconFile as alias
            set icon of targetFile to theIcon
        end try
    end tell
EOF
fi

echo "✅ Installation terminée ! Lancez l'application via le raccourci sur le bureau."

