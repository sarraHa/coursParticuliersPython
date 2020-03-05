

#par exemple 153 est un nombre de Armstrong, en effet on a : 153 = 1^3 + 5^3 + 3^3 .
#Ecrire un algorithme, puis un programme qui permet de determiner les quatre nombres de Armstrong.
#Indication : Les nombres d'Armstrong sont des nombres a 3 chiffres.

def affichechiffre(nombre):
    u = nombre%10
    print(u)
    d = nombre%100 / 10
    print(d)
    c = nombre / 100
    print(c)

#affichechiffre(124)


#ecrivez une fonction armstrong(n) qui dit si n est nombre armstrong ou pas
# indication : %


def armstrong(nombre):
    # pour prendre le dernier chiffre
    u = nombre%10
    #pour prendre le 2eme nombre
    d = nombre%100 / 10
    #pour prendre le 3 chiffre
    c = nombre / 100

    # on regarde mnt si c'est un nombre armstrong ou pas
    a =  (u**3 + d**3 + c**3)
    if a == nombre :
        print nombre," est un nombre d'armstrong"
    else:
        print("ce nest pas un nombre d'armstrong")
        

#armstrong(153)
#armstrong(435)


# ecrivez un programme qui affiche tous les nombres Armstrong
def tousLesNombresArmstrong():

    for nombre in range(100,1000):
        armstrong(nombre)

#tousLesNombresArmstrong()

#ecrivrez un programme  que demande un nombre a l'utlisateur lui dit si c'est un nombre Armstrong ou pas
# assurez vous de prendre que des nombre a 3 chiffre  ( pas de caractere)
# indications vous pouvez utiliser: isdigit(), len(), %


def estUnNombreArmstrong():
	#on demande a l'utilisateur de saisir un nombre 

    print("donnez un nombre a trois chiffres")
    nombre = raw_input()

    
    #on regarde d'abore si c'est nombre
    if nombre.isdigit() == False:
        print("cela doit etre un nombre!")
        return 

    #on regarde si c'est il a bien saisi un nombre a trois chiffres
    if len(nombre) !=  3:
        print("cela doit etre un nombre a trois chiffres!")
        return

    # si le programme est arrive ici c'est a dire que notre nombre respecte toutes les regles
    
    # on regarde mnt si c'est nombre Armstrong ou pas

    nombre = int(nombre)
    u = nombre%10
    d = nombre%100 / 10
    c = nombre / 100

    i = (u**3 + d**3 + c**3)
    if i == nombre:
        print nombre," est un nombre d'armstrong"
    else :
        print nombre," ce nes pas un nombre d'armstrong"
    
    
	

estUnNombreArmstrong()

