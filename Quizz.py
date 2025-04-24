import random
import time
print("------- Bienvenue au quizz des capitales ! -------")
print("Vous allez devoir me dire quel est la capitale du pays que je vais vous donner !")
continue_game = 1
score = 0
while continue_game == 1:
    question = ["Quelle est la capitale de la France ?","Quelle est la capitale de l'Angleterre ?","Quelle est la capitale du Japon ?","Quelle est la capitale de la suisse ?","Quelle est la capitale des Etats-Unis ?"]
    reponses = ["Paris","Londres","Tokyo","Berne","Washington"]
    numeros = [1,2,3,4,5]
    nombre = random.choice(numeros) - 1
    reponseAttendue = reponses[nombre]
    print(question[nombre])
    startTime = time.perf_counter()
    reponse = input("Alors ?")
    endTime = time.perf_counter()
    reponse = reponse.capitalize()
    try:
        reponse = int(reponse)
        print("C'est pas bon ! Il faut des lettres !")
        continue
    except ValueError:
        tempsMis = endTime - startTime
    if tempsMis >= 30:
        print("Trop long ! Si vous avez mis une bonne réponse, elle comptera nulle. Sinon, vous perdrez deux points !")
        score -= 1
    if reponse != reponseAttendue:
        print("C'est faux")
        if score >= 1:
            score -= 1
            print("Vous perdez un point.")
        else:
            print("Vous n'avez pas assez de points pour qu'on vous en enlève")
    else:
        score += 1
        print("C'est correct")
        print("Vous gagnez un point !")
    print(f"Vous avez {score} points")
    continue_game = int(input("Voulez-vous continuer ? Si oui, mettez 1. Si non, mettez 0"))
