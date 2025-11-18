import os
import sys

# Nouvelle structure cible
structure = {
    "TomNook/fundamentals": [
        "calculator.c",
        "digits_manipulation.c",
        "main.c",
        "operations.c",
        "operations.h",
        "simulated_dichotomy.c",
    ],
    "TomNook/proficiencies": [
        "digits_manip_advanced.c",
        "nook_bells.c",
        "nook_bells.h",
    ]
}

# Fichiers à la racine
root_files = [".gitignore", "README"]

# Contenu du .gitignore
gitignore_content = """*.a
*.lib
*.o
*.obj
*.out

.idea/
*~
*.DotSettings.user
"""

def structure_exists_completely(base_path):
    """Vérifie si toute la structure attendue est déjà présente."""
    if not os.path.isdir(base_path):
        return False

    for subfolder, files in structure.items():
        subfolder_path = os.path.join(base_path, subfolder)
        if not os.path.isdir(subfolder_path):
            return False
        for file in files:
            if not os.path.isfile(os.path.join(subfolder_path, file)):
                return False

    for file in root_files:
        if not os.path.isfile(os.path.join(base_path, file)):
            return False

    return True


def create_structure(base_path, prenom, nom):
    """Crée la structure complète et remplit .gitignore et README."""
    if structure_exists_completely(base_path):
        print(f"✅ L’architecture du dossier '{base_path}' est déjà complète. Aucune action nécessaire.")
        return

    os.makedirs(base_path, exist_ok=True)

    for subfolder, files in structure.items():
        folder_path = os.path.join(base_path, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8'):
                    pass

    # Fichiers à la racine
    gitignore_path = os.path.join(base_path, ".gitignore")
    readme_path = os.path.join(base_path, "README")

    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w', encoding='utf-8') as f:
            f.write(gitignore_content)

    if not os.path.exists(readme_path):
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(f"{prenom} {nom}\n")

    print(f"📁 Structure créée ou complétée avec succès dans '{os.path.abspath(base_path)}'.")


if __name__ == "__main__":
    print("=== Script de création de structure EPITA (Prog 102 - P02) ===")

    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    print(f"\n📂 Dossier actuel : {current_dir}")
    print(f"📂 Dossier parent : {parent_dir}")

    confirmation = input("Le dossier du TP se trouve-t-il bien dans le dossier parent ? (y/n) : ").strip().lower()
    if confirmation != "y":
        print("❌ Merci de placer ce script dans le bon répertoire avant de continuer.")
        sys.exit(1)

    git_clone = input("As-tu bien cloné le dépôt via 'git clone' ? (y/n) : ").strip().lower()
    if git_clone != "y":
        print("❌ Merci de cloner le dépôt avant d’exécuter ce script.")
        sys.exit(1)

    prenom = input("Prénom (en minuscule) : ").strip().lower()
    nom = input("Nom (en minuscule) : ").strip().lower()

    folder_name = f"prog-102-p-02-2030-{prenom}.{nom}"

    create_structure(folder_name, prenom, nom)
