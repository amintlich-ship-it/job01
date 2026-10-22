# Job 07: Suite pyramidale à partir de l'alphabet répété
chaine = "abcdefghijklmnopqrstuvwxyz" * 10
index = 0
ligne = 1

while index < len(chaine):
    # Calculer combien de caractères on peut prendre pour cette ligne
    # sans dépasser la longueur de la chaîne
    fin = min(index + ligne, len(chaine))
    print(chaine[index:fin])
    index = fin
    ligne += 1