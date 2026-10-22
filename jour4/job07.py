def produits_de_saison(type, saison):
    """Affiche les fruits ou légumes correspondant au type et à la saison."""
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine,navet")
    else:
        print("combinaison inconnue")