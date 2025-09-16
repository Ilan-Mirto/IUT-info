def depassement_vitesse(limitation, vitesse, recidive):
    """renvoie les consequences d'un excès de vitesse d'un conducteur

    Args:
        limitation (Integer): Limitation de vitesse en km/h
        vitesse (Integer): Vitesse du conducteur en km/h
        recidive (Boolean): Vrai si le conducteur a déjà depasser la limitation de vitesse de plus de 50km/h

    Returns:
        String: Conséquences de l'excès de vitesse
    """    

   
    amende = 0
    nb_point = 0
    annee_suspension = 0
    depassement = vitesse - limitation

    if depassement < 0:
        rep = "Aucune conséquence"
    else:
        if depassement <= 20:
            if limitation < 50:
                amende = 135
                nb_point = 1
                annee_suspension = "aucune"

            else:
                amende = 68
                nb_point = 1
                annee_suspension = "aucune"

        elif depassement <= 30:
            amende = 135
            nb_point = 2
            annee_suspension = "aucune"

        elif depassement <= 40:
            amende = 135
            nb_point = 3
            annee_suspension = 3

        elif depassement <= 50:
            amende = 135
            nb_point = 4
            annee_suspension = 3

        else:
            if recidive == True:
                amende = 3750
                nb_point = 6
                annee_suspension = 3
            else:
                amende = 1500
                nb_point = 6
                annee_suspension = 3

        rep = "amende : " + str(amende) + "€, nombre de points perdus : " + str(nb_point) + ", année(s) de suspension de permis : " + str(annee_suspension)
    
    return rep


def test_depassement_vitesse():
    assert depassement_vitesse(80, 120, False) == "amende : 135€, nombre de points perdus : 3, année(s) de suspension de permis : 3"
    assert depassement_vitesse(80, 150, True) == "amende : 3750€, nombre de points perdus : 6, année(s) de suspension de permis : 3"
    assert depassement_vitesse(40, 50, True) == "amende : 135€, nombre de points perdus : 1, année(s) de suspension de permis : aucune"
    assert depassement_vitesse(80, 98, False) == "amende : 68€, nombre de points perdus : 1, année(s) de suspension de permis : aucune"
    assert depassement_vitesse(80, 75, False) == "Aucune conséquence"