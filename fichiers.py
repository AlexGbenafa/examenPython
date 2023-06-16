def nbMotsAvecVoyelle(nomf):
    compteur = 0

    with open(nomf, 'r') as file:
        contenu = file.read()
        mots = contenu.split()

        for mot in mots:
            if mot[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
                compteur += 1
    print(compteur)
    return compteur

def compterChaqueMot(nomf, nomf1):
    mots = {}

    with open(nomf, 'r') as file:
        contenu = file.read()
        motsNomf = contenu.split()

        for mot in motsNomf:
            mots[mot] = mots.get(mot, 0) + 1

    with open(nomf1, 'w') as file:
        for mot, occurrences in mots.items():
            file.write(f"{mot}({occurrences}) ")


compterChaqueMot('nomf.txt', 'nomf1.txt')
nbMotsAvecVoyelle('nomf.txt')