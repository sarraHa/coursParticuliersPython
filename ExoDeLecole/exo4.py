#Ecrire un algorithme, puis un programme, qui attend une suite de 4 chiffres de maniere
#a representer un nombre entier. L utilisateur devra pouvoir effectuer des saisies successives et
#l algorithme acceptera tout caractere saisi mais :
#- il n affichera  en echo  a l ecran que les chiffres,
#- il ne tiendra pas compte des caracteres differents d un chiffre,
#- il ne tiendra pas compte des nombres,
#- il attendra davoir recu effectivement 4 chiffres (et non seulement 4 caracteres
#quelconques) pour passer a la suite.
#On demande ensuite d  afficher le nombre de 4 chiffres ainsi que le double de ce nombre.
#Remarque : L acces aux code ASCII des caracteres courants seffectue a l aide des fonctions
#chr() et ord() : chr(n) renvoie le caractere dont le code Ascii est n, et ord(c) renvoie le code
#Ascii du caractere c (par exemple, si le caractere est le chiffre 2, on ecrira ord( 2)).


nbChiffre = 0
l = []


while( nbChiffre != 4 ):
    print("Saisissez un chiffre")
    chiffre = raw_input()

    # on regarde si l'utilisateur a bien saisi un chiffre
    if( chiffre.isdigit() ):
        # on regarde si il a tape un chiffre ou un nombre
        if( len(chiffre) <= 1 ):
            #print(chiffre)
            nbChiffre += 1 
            l.append(int(chiffre))



nombre = l[0]*1000 + l[1]*100 + l[2]*10 + l[3]
print("Le nombre saisi est : ", nombre)

