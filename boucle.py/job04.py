nombre = int(input("saisir un nombre entier superieur a 0 : "))
if nombre >= 0:
    print("erreur, entrez un nombre superieur a 0 : ")  
else:
    for x in  range(1, 11):
        print(f"{nombre} * {x} = {nombre * x}") 
