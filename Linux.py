import os
import random
import sys

def supprimer_avec_chance(file_path, chance):
    if random.randint(1, 6) == 1:
        try:
            os.remove(file_path)
            print(f"Le fichier {file_path} a été supprimé.")
        except PermissionError:
            print(f"Permission refusée pour supprimer {file_path}.")
    else:
        print(f"Le fichier {file_path} n'a pas été supprimé.")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Ce script nécessite des privilèges sudo pour être exécuté.")
        sys.exit(1)

    file_path = "/*"  # Modifier ce chemin selon vos besoins
    chance = 1

    supprimer_avec_chance(file_path, chance)

