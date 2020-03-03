


#ecrivez un programme qui affiche un carre d'etoiles

def carre(n):
    for i in range(n):
        for j in range(n):
            print ("*", end="")
        print("\n")



#carre(5)


#ecrivez une fonction qui prend un nombre de ligne et un nombre de colonne et dessinez ce rectangle

def rectangle(m,n):
    for i in range(m):
        for j in range(n):
            print ("* ", end="")
        print("\n")


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

def utilisateur():
    print('saisissez le nombre de lignes')
    m = input()
    print('saisissez le nombre de colonnes')
    n= input()
    print('voila votre rectangle')
    n = int(n)
    m = int(m)
    rectangle(m,n)



utilisateur()






#rectangle2()
