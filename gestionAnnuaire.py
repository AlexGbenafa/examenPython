annuaire = []
critere = " "

def saisir_tab():
    personne = {}
    personne['nom'] = input('Nom: ')
    personne['prenom'] = input('Prénom: ')
    personne['numDeRue'] = input('Numéro de rue: ')
    personne['nomRue'] = input('Nom de la rue: ')
    personne['numeroTelephone'] = input('Numéro de téléphone: ')
    personne['codePostal'] = input('Code postal: ')
    personne['ville'] = input('Ville: ')
    return personne

def critere_recherche():
    print("1-Nom")
    print("2-Prenom")
    print("3-Numero de la rue")
    print("4-Nom de la rue")
    print("5-Numero de telephone")
    print("6-CodePostal")
    print("7-Ville")

    choix = int(input("Entrez le critere de recherche: "))

    if choix == 1:
        critere = "nom"
    elif choix == 2:
        critere = "prenom"
    elif choix == 3:
        critere = "numDeRue"
    elif choix == 4:
        critere = "nomRue"
    elif choix == 5:
        critere = "numeroTelephone"
    elif choix == 6:
        critere = "codePostal"
    elif choix == 7:
        critere = "ville"
    else:
        print("Choix invalide.")
        critere = ""
    
    return critere

def recherche(annuaire, critere):
    correspondances = []
    valeurRecherche = input("Entrez la valeur de recherche: ")
    for personne in annuaire:
        if personne[critere] == valeurRecherche:
            correspondances.append(True)
        else:
            correspondances.append(False)
    return correspondances

#Critere en surcharge pour une quesion d'afffichage
def affiche_tab(annuaire, critere, correspondances):
    if any(correspondances):
        print(f'Recherche effectuée (critère: {critere}):')
        for personne, correspondance in zip(annuaire, correspondances):
            if correspondance:
                print(personne)

nombrePersonnes = int(input("Entrez le nombre de personnes à saisir: "))
for i in range(nombrePersonnes):
    personne = saisir_tab()
    annuaire.append(personne)

critere = critere_recherche()
correspondances = recherche(annuaire, critere)
affiche_tab(annuaire, critere, correspondances)
