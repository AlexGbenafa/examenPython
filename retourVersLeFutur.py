from random import *

t = []

def Saisie():
    personne = {}
    personne['nom'] = str(input('Nom: '))
    personne['annee'] = int()
    personne['temps'] = int()
    t.append(personne)
    return t

def calculAnnee(t, annee_min, annee_max):
    for personne in t:
        print(f"Personne: {personne['nom']}")
        annee_min = int(input("Dans quelle année minimum souhaitez-vous faire un voyage dans le temps?"))
        annee_max = int(input("Dans quelle année maximum souhaitez-vous faire un voyage dans le temps?"))
        annee_voyage = randint(annee_min, annee_max)
        print("L'annee de voyage est: ", annee_voyage)
        personne['annee'] = annee_voyage

def calculTemps(t):
    for personne in t:
        temps_retour = abs(personne['annee'] - 2017) * 10
        print("Le temps de retour en 2017 est:", temps_retour,"sec")
        personne['temps'] = temps_retour

t = Saisie()
calculAnnee(t, -10000, 10000)
calculTemps(t)

#Oui