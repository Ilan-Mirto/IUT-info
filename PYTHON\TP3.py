# exercice 1
def nb_pair(entree):
    """[Vérifie si il y a plus de nombre pair qu'impair dans une liste donnée]

    Args:
        entree [list]: [liste de nombre]

    Returns:
        [bool]: [Vrai si la liste "entree" contient le même nombre ou plus de nombre pair qu'impair]
    """
    cpt_pair = 0 # nombre de nombres pairs dans la liste "entree"
    cpt_impair = 0 # nombre de nombres impairs dans la liste "entree"


    for nombre in entree:
        if nombre % 2 == 0:
            cpt_pair += 1
        else:
            cpt_impair += 1
    return cpt_pair >= cpt_impair

def test_nb_pair():
    assert nb_pair([1, 4, 6, -2, -5, 3, 10]) == True
    assert nb_pair([-4, 5, -11, -56, 5, -11]) == False
    assert nb_pair([35, 45, 71, -5, 48, -5, 47, 32, 48, 6, -89, 28]) == False
    assert nb_pair([14, 54, 58, 62, 54, 32, -8, -5, -4, 85]) == True

# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    res = None
    for i in liste_nombres:
        if i > valeur:
            res = i

    if res is not None:
        for elem in liste_nombres:
            if valeur < elem < res:
                res = elem

    # au début de chaque tour de boucle res est le plus petit élément
    # déjà énuméré supérieur à valeur
    
    return res


def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None
    assert min_sup([], 5) is None


# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    FLetter = False
    BSpace = False
    resultat = 0
    # au début de chaque tour de boucle
    # c1 vaut
    # c2 vaut
    # resultat vaut
    for c2 in phrase:
        
        if c2 != ' !:?':
            FLetter = True

        if FLetter == True:

            if BSpace == True and c2 not in ' !:?':
                resultat += 1

            if c2 == ' ':
                BSpace = True
            else:
                BSpace = False
    
    if FLetter == True:
        resultat += 1

    return resultat


def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus
    assert nb_mots("Jean Baptiste est hyper  U") == 5
    assert nb_mots("                                oui ") == 1
    assert nb_mots("je suis trop fort !") == 4