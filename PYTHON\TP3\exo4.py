# ----------------------- exo 4.1 ----------------------- #
def somme_pair(liste):
    """Renvoit la somme des nombres pairs de la liste "liste" 

    Args:
        liste (list): Liste de nombre entiers

    Returns:
        int : Somme des nombres pairs de la liste "liste"
    """

    res = 0 # somme des nombres pairs appartenant à la liste "liste"
    
    for nb in liste:
        if nb % 2 == 0:
            res += nb

    return res

def test_somme_pair():
    assert somme_pair([12, 13, 6, 5, 7]) == 18
    assert somme_pair([28, 2, 5, 6, 7, 11]) == 36
    assert somme_pair([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20
    assert somme_pair([64, 13, 29, 67, 45, 31, 64]) == 128
    assert somme_pair([2, 2, 2, 3, 3, 3, 3, 3, 3, -2, -2, -2, -2, -2, -2]) == -6


# ----------------------- exo 4.2 ----------------------- #
def derniere_voyelle(chaine):
    """Renvoit la dernière voyelle de la chaine de caractère "chaine"
    Args:
        chaine (str): Chaine de caractères

    Returns:
        str : Dernière voyelle de la chaine de caractère "chaine"
    """    

    res = "" # deriere voyelle de la chaine de caractères "chaine"

    for lettre in chaine:
        if lettre in "aeiouyAEIOUY":
            res = lettre

    return res

def test_derniere_voyelle():
    assert derniere_voyelle("BUT Informatique") == "e"
    assert derniere_voyelle("Je suis d'accord !!") == "o"
    assert derniere_voyelle("Test de la fonction derniere_voyelle()") == "e"
    assert derniere_voyelle("Le ciel est bleu") == "u"
    assert derniere_voyelle("Je m'appelle Ilan") == "a"
    assert derniere_voyelle("Je suis à l'IUT") == "U"


# ----------------------- exo 4.3 ----------------------- #
def proportion_neg(liste_nb):
    """Renvoit la proportion de nombres negatifs dans la liste "liste_nb"

    Args:
        liste (list): Liste de nombre

    Returns:
        float : Proportion de nombres negatifs dans la liste "liste_nb"
    """    
    
    nb_nombre_neg = 0 # Nombre de nombres négatifs dans la liste "liste_nb" 
    res = 0  # Proportion de nombres negatifs dans la liste "liste_nb"

    for nb in liste_nb:
        if nb < 0:
            nb_nombre_neg += 1
    
    res = nb_nombre_neg / len(liste_nb)

    return res

def test_proportion_neg():
    assert proportion_neg([4, -2, 8, 2, -2, -7]) == 0.5
    assert proportion_neg([8, -9, 5, -6, 7, 4, 2, -5, -3, 4]) == 0.4
    assert proportion_neg([-1, -2, -3, -3, -5, -7, -0.2, -1, -78.51, 3]) == 0.9
    assert proportion_neg([2, 8, 5.3, 4, 8, 6, 3, 4.8, 8, 2]) == 0.0
    assert proportion_neg([-1, -2.3, -4, -8, -5, -6.2, -5, -7, -1.2, -0.2]) == 1.0