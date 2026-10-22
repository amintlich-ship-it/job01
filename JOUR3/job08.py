# Job 08: Analyse de triangle
print("Entrez les trois longueurs du triangle :")
a = float(input("Longueur a : "))
b = float(input("Longueur b : "))
c = float(input("Longueur c : "))

# Vérifier si un triangle peut être construit
if a + b > c and a + c > b and b + c > a:
    print("Il est possible de construire un triangle.")

    # Vérifier le type de triangle
    # Équilatéral : tous les côtés égaux
    if a == b and b == c:
        print("Le triangle est équilatéral.")
    # Rectangle : vérification du théorème de Pythagore
    # On vérifie toutes les possibilités car on ne sait pas lequel est l'hypoténuse
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        # Vérifier si c'est aussi isocèle
        if a == b or b == c or a == c:
            print("Le triangle est rectangle et isocèle.")
        else:
            print("Le triangle est rectangle.")
    # Isocèle : exactement deux côtés égaux (on sait qu'il n'est pas équilatéral ici)
    elif a == b or b == c or a == c:
        print("Le triangle est isocèle.")
    # Quelconque : aucun côté égal et pas rectangle
    else:
        print("Le triangle est quelconque.")
else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")