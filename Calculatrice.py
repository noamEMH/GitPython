from math import sqrt

def add(x, y):
    calc_str = f"{x} + {y}"
    result = x + y
    print(result)
    return calc_str, result

def sub(x, y):
    calc_str = f"{x} - {y}"
    result = x - y
    print(result)
    return calc_str, result

def div(x, y):
    calc_str = f"{x} / {y}"
    result = x / y
    print(result)
    return calc_str, result

def mult(x, y):
    calc_str = f"{x} * {y}"
    result = x * y
    print(result)
    return calc_str, result

def squar(x):
    calc_str = f"{x}²"
    result = x * x
    print(result)
    return calc_str, result

def sqr_ro(x):
    calc_str = f"√{x}"
    result = sqrt(x)
    print(result)
    return calc_str, result

def afficher_5_derniers_calculs(nom_fichier="memoire_calculate.txt"):
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        dernieres_lignes = lignes[-5:]
        print("Les 5 derniers calculs :")
        for ligne in dernieres_lignes:
            print(ligne.strip()) 

cont = 1
while cont == 1:
    print("1.Additionner ? 2.Soustraire ? 3.Diviser ? 4.Multiplier ? 5. Mettre au carré ? 6. Racine carrée ? 7. Voir les 5 derniers calculs ?")
    calcul = int(input("Quel calcul voulez vous faire ?"))
    calc_expression = ""
    resultat_final = None

    if calcul == 1:
        nombre1 = int(input("Quel est votre premier nombre ? "))
        nombre2 = int(input("Quel est votre second nombre ? "))
        calc_expression, resultat_final = add(nombre1, nombre2)
    elif calcul == 2:
        nombre1 = int(input("Quel est votre premier nombre ? "))
        nombre2 = int(input("Quel est votre second nombre ? "))
        calc_expression, resultat_final = sub(nombre1, nombre2)
    elif calcul == 3:
        nombre1 = int(input("Quel est votre premier nombre ? "))
        nombre2 = int(input("Quel est votre second nombre ? "))
        calc_expression, resultat_final = div(nombre1, nombre2)
    elif calcul == 4:
        nombre1 = int(input("Quel est votre premier nombre ? "))
        nombre2 = int(input("Quel est votre second nombre ? "))
        calc_expression, resultat_final = mult(nombre1, nombre2)
    elif calcul == 5:
        nombre = int(input("Quel nombre calculer ? "))
        calc_expression, resultat_final = squar(nombre)
    elif calcul == 6:
        nombre = int(input("Quel nombre calculer ? "))
        calc_expression, resultat_final = sqr_ro(nombre)
    elif calcul == 7:
        afficher_5_derniers_calculs()

    if calc_expression and resultat_final is not None:
        with open("memoire_calculate.txt", "a", encoding='utf_8') as f: 
            f.write(f"Calcul : {calc_expression} = {resultat_final}\n")

    cont = int(input("Si vous voulez continuer, tapez 1. Sinon, n'importe quel chiffre "))

print("Calculatrice éteinte.")