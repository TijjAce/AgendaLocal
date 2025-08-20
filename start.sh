#!/bin/bash
set -euo pipefail

echo "=== 🚀 Installation & Raccourci AgendaLocal (macOS) ==="

# ---- Réglages de base
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
DESKTOP="$HOME/Desktop"
APP_CMD="$PROJECT_DIR/AgendaLocal.command"
ALIAS_NAME="AgendaLocal"      # nom de l’alias sur le Bureau (sans 'alias')
ICON_1="$PROJECT_DIR/agenda.icns"
ICON_2="$PROJECT_DIR/agenda.png"
ICON_3="$PROJECT_DIR/agenda.ico"

# ---- Vérif OS
if [[ "$OSTYPE" != "darwin"* ]]; then
  echo "❌ Ce script est prévu pour macOS."
  exit 1
fi

# ---- Homebrew
if ! command -v brew >/dev/null 2>&1; then
  echo "❌ Homebrew n'est pas installé. Installe-le d'abord :"
  echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
  exit 1
fi

# ---- Python 3.10 (install si manquant)
echo "🔎 Recherche de python3.10…"
PY310_BIN="$(command -v python3.10 || true)"
if [[ -z "${PY310_BIN}" ]]; then
  echo "📦 Installation de python@3.10 via Homebrew…"
  brew list --versions python@3.10 >/dev/null 2>&1 || brew install python@3.10
  # Détermine le chemin (Apple Silicon / Intel)
  if [[ -x "/opt/homebrew/opt/python@3.10/bin/python3.10" ]]; then
    PY310_BIN="/opt/homebrew/opt/python@3.10/bin/python3.10"
  elif [[ -x "/usr/local/opt/python@3.10/bin/python3.10" ]]; then
    PY310_BIN="/usr/local/opt/python@3.10/bin/python3.10"
  else
    # Essaye à nouveau via PATH
    PY310_BIN="$(command -v python3.10 || true)"
  fi
fi

if [[ -z "${PY310_BIN}" ]]; then
  echo "❌ Impossible de localiser python3.10 après installation."
  exit 1
fi

echo "✅ Python sélectionné : $($PY310_BIN --version)"

# ---- (Re)création du venv propre
echo "📦 Création du venv…"
rm -rf "$PROJECT_DIR/venv"
"$PY310_BIN" -m venv "$PROJECT_DIR/venv"
# shellcheck disable=SC1091
source "$PROJECT_DIR/venv/bin/activate"

# ---- pip à jour
echo "⬆️  Mise à jour de pip…"
python -m pip install --upgrade pip

# ---- Dépendances
echo "📥 Installation des dépendances…"
if [[ -f "$PROJECT_DIR/requirements.txt" ]]; then
  pip install -r "$PROJECT_DIR/requirements.txt"
else
  echo "⚠️ requirements.txt introuvable — installation minimale (Django 5.2.4 + xhtml2pdf)…"
  pip install "Django==5.2.4" xhtml2pdf
fi

# Toujours installer xhtml2pdf au cas où il ne serait pas listé
pip install xhtml2pdf

# ---- Migrations Django
if [[ -f "$PROJECT_DIR/manage.py" ]]; then
  echo "🗄️  Migrations Django…"
  python "$PROJECT_DIR/manage.py" makemigrations || true
  python "$PROJECT_DIR/manage.py" migrate
else
  echo "⚠️ manage.py introuvable, étape migrations ignorée."
fi

# ---- Importation des pages si script présent
if [[ -f "$PROJECT_DIR/import_pages.py" ]]; then
  echo "📚 Importation des pages…"
  python "$PROJECT_DIR/import_pages.py" || true
fi

# ---- Création du .command LANCEUR dans le projet
echo "🛠️  Création du lanceur : $APP_CMD"
cat > "$APP_CMD" <<EOF
#!/bin/bash
cd "$PROJECT_DIR"
source "venv/bin/activate"
python manage.py runserver
EOF
chmod +x "$APP_CMD"

# ---- Création de l'alias sur le Bureau vers ce .command
echo "🔗 Création de l'alias sur le Bureau…"
osascript <<EOF || true
tell application "Finder"
  set targetFile to POSIX file "$APP_CMD" as alias
  set desktopFolder to (path to desktop folder) as alias
  set aliasName to "$ALIAS_NAME"

  -- supprime un alias existant portant ce nom
  try
    delete (alias file aliasName of desktopFolder)
  end try

  set aliasRef to make new alias file at desktopFolder to targetFile with properties {name:aliasName}

  -- tentative d'application d'une icône personnalisée
  set iconCandidates to {"$ICON_1", "$ICON_2", "$ICON_3"}
  repeat with p in iconCandidates
    try
      set iconFile to POSIX file (p as text) as alias
      set icon of aliasRef to icon of iconFile
      exit repeat
    end try
  end repeat
end tell
EOF

echo "✅ Installation terminée !"
echo "➡️  Lance l'application via l'alias sur le Bureau : \"$ALIAS_NAME\""

