#Crée en septembre 2022
#Crée par Samuel Munoz
#But:Jeu de devinnete

from random import randint

game = 1 #cette varaible verifie c'est le joue devrait continuer ou non
print("Salut joueur,bienvenu au jeu de devinette\npour commencer le jeu vous auriez à deviner un nombre entre 0 , et un nombre maximal que vous auriez choisie.\nDe plus,vous pouvez chosir le nbr des essais que vous avez.\ncommencons!")

def guess(nbr_aleatoire):  # on crée une fonction pour verifier et interpreter la reponse donne par le joueur

    guess_player = int(input("Selon vous quel est le nombre que je viens de choisir?\n"))
    if nbr_aleatoire == guess_player:  # on verifie la reponse et si le nombre que le jouer a chossis et le nombre que l'ordinateur, on return true
        print(f"En effect le nombre que je choisis c'est:{nbr_aleatoire}")
        return True
    elif guess_player < 0: #on verifie la reponse du joueur et si la reponse est dehors des nbr possibles, on print le message suivant le jeu continue
        print(f"le nbr que vous venez de chosir n'est pas dans listes de nbr possibles\nIl vous reste {nbr_essais - 1} essais\n")
    elif guess_player > borne_maximal:
        print(f"le nbr que vous venez de chosir n'est pas dans listes de nbr possibles\nIl vous reste {nbr_essais - 1} essais\n")
    elif nbr_aleatoire < guess_player:  # on verifie la reponse de joueur, et si la reponse est est plus petit que le nbr que l'ordinateur a chossi, le jeu continue
        print(f"Non, le nombre que j'ai choisi est plus petit que le nombre que vous avez choisi\nIl vous reste {nbr_essais - 1} essais\n")
    elif nbr_aleatoire > guess_player:  # on verifie la reponse de joueur, et si la reponse est est grand petit que le nbr que l'ordinateur a chossi, le jeu continue
        print(f"Non, le nombre que j'ai choisi est plus grand que le nombre que vous avez choisi\nIl vous reste {nbr_essais - 1} essais\n")

while game == 1: #tandis que game = 1 , le jeu il continue

    borne_maximal = int(input("Choisisez une borne maximal"))
    nbr_essais = int(input("Choissisez le nbr de essais que vous avez"))
    nbr_aleatoire = randint(0,borne_maximal)
    boucle = 1


    print(f"je viens de choisir un nombre entre 0 et {borne_maximal}, à vous de le deviner, vous avez {nbr_essais} essais\n")
    while boucle == 1:
        if nbr_essais == 0:
            print("dommage vous avez perdue\n")
            autre_partie_perdue = int(input("voulez-vous faire une autre partie?\nrepondez 1 pour oui et 2 pour non"))
            if autre_partie_perdue == 1:
                boucle = 2
            elif autre_partie_perdue == 2:
                print("D'accord aurevoir")
                boucle = 2
                game = 2
            else:
                print("je vais prendre votre reponse comme un non, aurevoir")
                game = 2
                boucle = 2
       
        elif guess(nbr_aleatoire): #si la valeur returner de la fonction guess est "true" la partie fini
            print("Bravo vous avez reussi en",nbr_essais,"essais\n")
            autre_partie = int(input("voulez-vous faire une autre partie?\nrepondez 1 pour oui et 2 pour non"))
            if autre_partie == 1:
                boucle = 2  #on sort de la boucle
            elif autre_partie == 2:
                print("D'accord aurevoir")
                game = 2 #on change la variable pour arreter le jeu
            else:
                print("je vais prendre votre reponse comme un non, aurevoir")
                game = 2
        nbr_essais = nbr_essais - 1







