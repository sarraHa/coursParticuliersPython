

#par exemple 153 est un nombre de Armstrong, en effet on a : 153 = 1^3 + 5^3 + 3^3 .
#Ecrire un algorithme, puis un programme qui permet de determiner les quatre nombres de Armstrong.
#Indication : Les nombres d'Armstrong sont des nombres a 3 chiffres.



#ecrivez une fonction armstrong(n) qui dit si n est nombre armstrong ou pas
# indication : %


def armstrong(n):
    # pour prendre le dernier chiffre
    u = n % 10
    #pour prendre le 2eme nombre
    d = n % 100 / 10
    #pour prendre le 3 chiffre
    c = n / 100

    # on regarde mnt si c'est un nombre armstrong ou pas

    nombre = c**3 + d**3+ u**3 
    if( n == nombre ):
        print n, "est un nombre armstrong"
    else :
        print n, "n'est pas un nombre armstrong"

        

armstrong(153)


def tousLesNombresArmstrong():
    print("\nles nombres d'Armstrong sont: ")

    for nombre in range(100, 1000):
        u = nombre % 10
        d = nombre % 100 / 10
        c = nombre / 100
        #print(u)
        #print(d)
        #print(c)

        n = c**3 + d**3+ u**3 
        if( n == nombre):
            print(n)

#tousLesNombresArmstrong()

#ecrivrez un programme  que demande un nombre a l'utlisateur lui dit si c'est un nombre Armstrong ou pas
# assurez vous de prendre que des nombre a 3 chiffre  ( pas de caractere)
# indications vous pouvez utiliser: isdigit(), len(), %

def estUnNombreArmstrong():
    print("Saisissez un nombre a 3 chiffre\n")
    nombre = raw_input()
    
    #on regarde d'abore si c'est nombre
    if( nombre.isdigit() == False):
        print("Je vous ai dit de saisire un nombre pas un text :(")
        return
    #on regarde si c'est il a bien saisi un nombre a trois chiffres
    if( len(nombre) < 3 ):
        print("Je vous ai dit de saisire un nombre a trois chiffres pas plus ni moins :(")
        return
    # si le programme est arrive ici c'est a dire que notre nombre respecte toutes les regles
    # on regarde mnt si c'est nombre Armstrong ou pas

    u = int(nombre) % 10
    d = int(nombre) % 100 / 10
    c = int(nombre) / 100

    n = c**3 + d**3+ u**3 
    if( n == int(nombre)):
        
        print("Le nombre que vous avez saisi est un nombre Armstrong")
    else :
        print("Le nombre que vous avez saisi n'est pas un nombre Armstrong")
    

#estUnNombreArmstrong()


