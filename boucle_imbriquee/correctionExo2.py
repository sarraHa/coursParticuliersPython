



#ecrivez un programme qui affiche un carre d'etoiles



def carre(nb_lignes):

    for i in range(nb_lignes):
        for j in range(nb_lignes):
            print("*", end ="") 
        print()

carre(5)


#ecrivez une fonction qui prend un nombre de ligne et un nombre de colonne et dessinez ce rectangle




#def rectangle(nb_lignes, nb_colonnes):

#    for i in range(nb_lignes):
#        for j in range(nb_colonnes):
#            print("*", end ="") 
#        print()

#rectangle(3, 7)




#ecrivez un programme qui demande a l'utilisateur un nombre de lignes et un nombre de colonnes pour dessigner le rectangle qui correspond
# saisissez un nombre de ligne 
# 3
# saisissez maintenant un nombre de colonnes
# 4
# voila votre rectangle
# ****
# ****
# ****


# rappel : input(), print("*", end=""), int()

def rectangle2():
    print("saisissez un nombre de ligne")
    nb_lignes = input()
    print("saisissez maintenant un nombre de colonnes")
    nb_colones = input()
    print("voila votre rectangle\n")

    for i in range( int(nb_lignes)):
        for j in range( int(nb_colones)):
            print("*", end="")
        print("\n")



rectangle2()
