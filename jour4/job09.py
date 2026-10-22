def pair_ou_impair(nombre):
    """Affiche si un nombre entier positif est pair ou impair.
 
    Affiche un message d'erreur si la valeur n'est pas un entier positif.
    """
    # bool est un sous-type de int en Python : on l'exclut explicitement
    if not isinstance(nombre, int) or isinstance(nombre, bool):
        print(f"{nombre!r} : erreur, ce n'est pas un nombre entier")
    elif nombre < 0:
        print(f"{nombre} : erreur, le nombre doit être positif")
    elif nombre % 2 == 0:
        print(f"{nombre} est pair")
    else:
        print(f"{nombre} est impair")