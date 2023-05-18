
import random

with open("mots_pendu.txt", 'r') as f:
    mots = f.read().split('\n')

def choisir_mot(mots):
    return random.choice(mots)
def affichage_mot(solution,lettre_trouvees):

    mot_maj = ''
    for lettre in solution:
        if lettre in lettre_trouvees:
            mot_maj += lettre
        else:
            mot_maj += '_'
    return mot_maj

reponse = choisir_mot(mots)
print(reponse)

chance = 6
lettre_trouvees = ''
lettre_pas_bonnes = ''

while chance > 0:
    print('-----------------')
    proposition = str(input('Proposez une lettre : '))[0:1]
    if proposition in lettre_pas_bonnes+lettre_trouvees:
        print('Vous avez déjà essayé cette lettre')
    else:
        if proposition in reponse:
            lettre_trouvees += proposition
        else:
            chance -= 1
            lettre_pas_bonnes += proposition
            print('OUPS ! Il vous reste ' + str(chance) + ' chances')

        print('Lettre trouvées : ' + lettre_trouvees)
        print('Lettre pas dans la solution : ' + lettre_pas_bonnes)
        mot_actualise = affichage_mot(reponse,lettre_trouvees)
        print(mot_actualise)

        if '_' not in mot_actualise:
            print('VOUS AVEZ GAGNE')
            break

        if chance == 0:
            print('VOUS AVEZ PERDU ! ' + 'Le mot à trouver était : '+ reponse)

print('Appuyez sur "Entrer" pour quitter le script')

input()