import os
import sys

# Structure cible des fichiers
structure = {
    "RECAPTAIN/Fundamentals": [
        "coffee.py", "counting_bells.py", "counting_vowels.py", "farm.py", "fences.py",
        "greetings.py", "labels.py", "longest_word.py", "market.py",
        "repeat.py", "seaquence.py", "signs.py"
    ],
    "RECAPTAIN/Proficiencies": [
        "balanced.py", "binary.py", "christmas.py", "debts.py", "game.py",
        "is_valid.py", "multiplication.py", "palindrome.py", "secret.py"
    ]
}

# Fichiers à la racine
root_files = [".gitignore", "README"]


def structure_exists_completely(base_path):
    """Vérifie si toute la structure attendue est déjà présente."""
    # Vérifie le dossier principal
    if not os.path.isdir(base_path):
        return False

    # Vérifie les fichiers et dossiers internes
    for subfolder, files in structure.items():
        subfolder_path = os.path.join(base_path, subfolder)
        if not os.path.isdir(subfolder_path):
            return False
        for file in files:
            file_path = os.path.join(subfolder_path, file)
            if not os.path.isfile(file_path):
                return False

    # Vérifie les fichiers à la racine
    for file in root_files:
        file_path = os.path.join(base_path, file)
        if not os.path.isfile(file_path):
            return False

    return True


def create_structure(base_path):
    """
    Crée la structure complète seulement si elle n’existe pas déjà.
    Ne remplace rien et informe l’utilisateur si tout est déjà présent.
    """
    # Si tout est déjà en place, on ne touche à rien
    if structure_exists_completely(base_path):
        print(f"✅ L’architecture du dossier '{base_path}' est déjà complète. Aucune action nécessaire.")
        return

    # Création du dossier racine
    os.makedirs(base_path, exist_ok=True)

    # Création des sous-dossiers et fichiers manquants
    for subfolder, files in structure.items():
        folder_path = os.path.join(base_path, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8'):
                    pass  # Crée un fichier vide

    # Fichiers à la racine
    for file in root_files:
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8'):
                pass

    print(f"📁 Structure créée ou complétée avec succès dans '{os.path.abspath(base_path)}'.")


if __name__ == "__main__":
    print("=== Script de création de structure EPITA ===")

    # Vérifie la position du dossier
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    print(f"\n📂 Dossier actuel : {current_dir}")
    print(f"📂 Dossier parent : {parent_dir}")

    confirmation = input("Le dossier du TP se trouve-t-il bien dans le dossier parent ? (oui/non) : ").strip().lower()
    if confirmation != "oui":
        print("❌ Merci de placer ce script dans le bon répertoire avant de continuer.")
        sys.exit(1)

    # Vérifie si le dépôt a été cloné
    git_clone = input("As-tu bien cloné le dépôt via 'git clone' ? (oui/non) : ").strip().lower()
    if git_clone != "oui":
        print("❌ Merci de cloner le dépôt avant d’exécuter ce script.")
        sys.exit(1)

    # Demande prénom et nom
    prenom = input("Prénom (en minuscule) : ").strip().lower()
    nom = input("Nom (en minuscule) : ").strip().lower()

    # Nom du dossier final
    folder_name = f"epita-prepa-computer-science-prog-101-p-05-2030-{prenom}.{nom}"

    # Création / vérification de la structure
    create_structure(folder_name)