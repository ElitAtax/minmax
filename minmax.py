import random
aleatoire = random.randint(0, 100)

nombre = ""

while nombre != aleatoire:
    nombre = int(input("Dis moi un nombre entre 1 et 100! >"))
    if nombre < aleatoire:
        print("Nombres trop petit !")

    elif nombre > aleatoire:
        print("Nombres trop grand !")

    else:
        print("C'est win gg le bro")
        exit()
