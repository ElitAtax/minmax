import random
choix1 = int(input("Premier nombre de l'intervalle >"))

choix2 = int(input("Dernier nombre de l'intervalle >"))

aleatoire = random.randint(choix1, choix2)


nombre = ""

while nombre != aleatoire:
    nombre = int(input(f"Dis moi un nombre entre {choix1} et {choix2} >"))
    if nombre < aleatoire:
        print("Nombres trop petit !")

    elif nombre > aleatoire:
        print("Nombres trop grand !")

    else:
        print("C'est win gg le bro")
        exit()
