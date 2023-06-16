from random import *

t = []

def Saisie():
    personne = {}
    personne['nom'] = str(input('Nom: '))
    personne['annee'] = int(input('Annee: '))
    personne['temps'] = int(input('Temps: '))
    t.append(personne)
    return t

def calculAnnee(t, annee_min, annee_max):
    for personne in t:
        print(f"Personne: {personne['nom']}")
        annee_min = input(" Dans quelle annee minimum souhaitez-vous faire un voyage dans le temps ?")
        annee_max = input(" Dans quelle annee maximun souhaitez-vous faire un voyage dans le temps ?")
        annee_voyage = randint(annee_min, annee_max)
        personne['annee'] = annee_voyage

t = Saisie()
calculAnnee(t, -10000, 10000)
