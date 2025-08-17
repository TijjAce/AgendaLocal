import json

# Charger les données JSON d'entrée
with open("arbre.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Dictionnaire id → libellé
id_to_label = {node["id"]: node["text"] for node in data["nodes"]}

# Relations parent → enfants
parent_to_children = {}
child_to_parent = {}

for edge in data["edges"]:
    parent = edge["fromNode"]
    child = edge["toNode"]
    parent_to_children.setdefault(parent, []).append(child)
    child_to_parent[child] = parent

# Trouver la racine
all_ids = set(id_to_label.keys())
child_ids = set(child_to_parent.keys())
root_ids = list(all_ids - child_ids)
assert len(root_ids) == 1, "Il doit y avoir une seule racine"
root_id = root_ids[0]

# Fonction récursive avec rang
def build_tree(node_id, rang=0):
    node = {
        "name": id_to_label[node_id],
        "rang": rang
    }
    children = parent_to_children.get(node_id, [])
    if children:
        node["children"] = [build_tree(child_id, rang + 1) for child_id in children]
    return node

# Construire et exporter
tree = build_tree(root_id)

with open("arborescence.json", "w", encoding="utf-8") as f:
    json.dump(tree, f, ensure_ascii=False, indent=2)

print("✅ Arborescence avec rang enregistrée dans 'arborescence.json'")
