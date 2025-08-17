#!/bin/bash

echo "=== Vérification de Python ==="
if ! command -v python3 &> /dev/null
then
    echo "Python3 n'est pas installé."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Installation avec Homebrew..."
        if ! command -v brew &> /dev/null
        then
            echo "Homebrew n'est pas installé. Installez-le depuis https://brew.sh/"
            exit 1
        fi
        brew install python
    else
        echo "Installez Python manuellement (apt, dnf, etc.)."
        exit 1
    fi
fi

echo "=== Création de l'environnement virtuel ==="
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

echo "=== Activation du venv ==="
source venv/bin/activate

echo "=== Mise à jour de pip ==="
python -m pip install --upgrade pip

echo "=== Installation des dépendances ==="
if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt introuvable !"
    exit 1
fi
pip install -r requirements.txt
pip install xhtml2pdf

echo "=== Migrations Django ==="
python manage.py makemigrations
python manage.py migrate

echo "=== Importation des pages ==="
python import_pages.py

echo "=== Création d'un raccourci sur le bureau ==="
DESKTOP="$HOME/Desktop"
SHORTCUT="$DESKTOP/AgendaLocal.command"

cat <<EOF > "$SHORTCUT"
#!/bin/bash
cd $(pwd)
source venv/bin/activate
python manage.py runserver
EOF

chmod +x "$SHORTCUT"

# Tentative de mise d'icône sur macOS (optionnel)
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

