fruit = ["pomme", "cerise", "orange"]
print(fruit)
for i in range(3):
    if i not in ["pomme", "cerise", "orange"]:
        print("melon")


for i in range(len(fruit)):
    print(i, fruit[i])


fruit.append("melon")
print(fruit)
#dans le job3 fallait ajouter (melon) dans la chaine de caractere (fruit)
# a l'aide de la fonction [for i in] et [if i not] 