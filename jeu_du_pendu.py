#import de random qui permet la génération aléatoire d'un mot dans la liste
import random
#ouverture du fichier "mots_pendu.txt" qui contient la liste de mots
with open("mots_pendu.txt", 'r') as f:
    #on sépare chaque ligne pour séparer chaque mot et les mettre dans "mots"
    mots = f.read().split('\n')
#fonction qui permet de choisir un mot de façon aléatoire dans la liste
def choisir_mot(mots):
    return random.choice(mots)
#fonction qui permet d'afficher le mot mis à jour en fonction des lettres trouvées par l'utilisateur
def affichage_mot(solution,lettre_trouvees):
    mot_maj = ''
    for lettre in solution:
        #si la lettre a été trouvée on l'affiche
        if lettre in lettre_trouvees:
            mot_maj += lettre
        #sinon on affiche un "_"
        else:
            mot_maj += '_'
    return mot_maj
#fonction qui permet d'avancer dans le jeu
def processus_joueur(chance, lettre_pas_bonnes, lettre_trouvees):
    #tant qu'il nous reste des chances pour trouver le mot
    while chance > 0:

        #[0:1] permet de récupérer que la première lettre proposée par le joueur même s'il en rentre plusieurs
        proposition = str(input('- Proposez une lettre : '))[0:1]
        #blindé pour ne pas proposer plusieurs fois la même lettre
        if proposition in lettre_pas_bonnes+lettre_trouvees:
            print('Vous avez déjà essayé cette lettre')
        else:
            #si la proposition est bonne
            if proposition in reponse:
                lettre_trouvees += proposition
            #sinon la proposition n'est pas correcte
            else:
                chance -= 1
                lettre_pas_bonnes += proposition
                print('OUPS ! Il vous reste ' + str(chance) + ' chances')
            #print pour rappeler au joueur où il est en dans sa recherche
            print('Lettre trouvées : ' + lettre_trouvees)
            print('Lettre pas dans la solution : ' + lettre_pas_bonnes)
            mot_actualise = affichage_mot(reponse,lettre_trouvees)
            print(mot_actualise)
            #si le joueur a trouvé toutes les lettres
            if '_' not in mot_actualise:
                print('VOUS AVEZ GAGNE')
                #fin du script
                break
            #si le joueur n'a plus de chance pour proposer de nouvelles lettres alors la partie est perdu
            if chance == 0:
                print('VOUS AVEZ PERDU ! ' + 'Le mot à trouver était : '+ reponse)
    print('Appuyez sur "Entrer" pour quitter le script')
    # fermeture du script
    input()

#définition des variables qui vont nous être utile
#nombre de chance pour trouver la bonne réponse
chance = 6
#chaine de caractère comprenant les lettres bien trouvées par le joueur
lettre_trouvees = ''
#chaine de caractère comprenant les lettres proposées par le joueur ne se trouvant pas dans la solution
lettre_pas_bonnes = ''

reponse = choisir_mot(mots)
#utile pour la correction mais normalement cette ligne ne devrait
#pas etre là pour ne pas donner la solution au joueur
print('Réponse : ' + reponse)

processus_joueur(chance,lettre_pas_bonnes,lettre_trouvees)
