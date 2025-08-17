import json

# Charger l'arborescence JSON
with open("arborescence.json", "r", encoding="utf-8") as f:
    tree = json.load(f)

def to_slug(text):
    return (
        text.lower()
        .replace("’", "")
        .replace("'", "")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .replace("œ", "oe")
        .replace("–", "-")
        .replace("—", "-")
        .replace(" ", "-")
    )

existing_slugs = set()

def unique_slug(base_slug):
    slug = base_slug
    i = 1
    while slug in existing_slugs:
        slug = f"{base_slug}-{i}"
        i += 1
    existing_slugs.add(slug)
    return slug

disciplines = []
competences = []

def collect_nodes(node, discipline_var=None, cycle=None, objectifs=None, competence_generale=None):
    rang = node.get("rang")
    nom = node["name"]

    if rang == 1:
        cycle = nom
    elif rang == 2:
        base_slug = to_slug(nom)
        slug = unique_slug(base_slug)
        discipline_var = f"domaineDiscipline{len(disciplines) + 1}"
        disciplines.append({
            "name": nom,
            "slug": slug,
            "var": discipline_var
        })
    elif rang == 3:
        objectifs = nom
    elif rang == 4 and node.get("children"):  # Ne retenir comme compétence générale que si ce n’est pas une feuille
        competence_generale = nom

    children = node.get("children", [])

    if not children:
        base_slug = to_slug(nom)
        slug = unique_slug(base_slug)
        comp_var = f"competence{len(competences) + 1}"
        competences.append({
            "name": nom,
            "slug": slug,
            "var": comp_var,
            "parent_var": discipline_var,
            "cycle_enseignement": cycle,
            "objectifs_generaux": objectifs,
            "competence_generale": competence_generale,
        })

    for child in children:
        collect_nodes(
            child,
            discipline_var=discipline_var,
            cycle=cycle,
            objectifs=objectifs,
            competence_generale=competence_generale
        )

collect_nodes(tree)

def dump_str(s):
    return json.dumps(s)

# Générer le fichier import_pages.py
with open("import_pages.py", "w", encoding="utf-8") as f:
    f.write("import os\nimport django\n\n")
    f.write("os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')\n")
    f.write("django.setup()\n\n")
    f.write("from pages.models import Page\n\n")

    for disc in disciplines:
        f.write(f"# Discipline : {disc['name']}\n")
        f.write(f"{disc['var']}, created = Page.objects.get_or_create(\n")
        f.write(f"    slug={dump_str(disc['slug'])},\n")
        f.write(f"    defaults={{\n")
        f.write(f"        'title': {dump_str(disc['name'])},\n")
        f.write(f"        'content': {dump_str(f'<p>Contenu par défaut pour la discipline {disc['name']}</p>')},\n")
        f.write(f"        'published': True,\n")
        f.write(f"    }}\n")
        f.write(")\n\n")

    for comp in competences:
        f.write(f"# Compétence : {comp['name']}\n")
        f.write(f"{comp['var']}, created = Page.objects.get_or_create(\n")
        f.write(f"    slug={dump_str(comp['slug'])},\n")
        f.write(f"    defaults={{\n")
        f.write(f"        'title': {dump_str(comp['name'])},\n")
        f.write(f"        'content': {dump_str(f'<p>Contenu par défaut pour la compétence {comp['name']}</p>')},\n")
        f.write(f"        'published': True,\n")
        f.write(f"        'parent': {comp['parent_var']},\n")

        if comp["cycle_enseignement"]:
            f.write(f"        'cycle_enseignement': {dump_str(comp['cycle_enseignement'])},\n")
        if comp["objectifs_generaux"]:
            f.write(f"        'objectifs_generaux': {dump_str(comp['objectifs_generaux'])},\n")
        if comp["competence_generale"]:
            f.write(f"        'competence_generale': {dump_str(comp['competence_generale'])},\n")

        f.write(f"    }}\n")
        f.write(")\n\n")

print("✅ Fichier 'import_pages.py' généré avec succès.")
