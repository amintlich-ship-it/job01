# Job 03: Affichage de 0 à 100 sauf certains nombres
for i in range(101):  # 0 à 100 inclus
    if i not in [26, 37, 88]:
        print(i)