

#Afficher caractere par caractere tous les caracteres de la chaine suivante

chaine = "Bonjour tous le monde"

for lettre in chaine:
    print(lettre)




#2eme methode


for i in range( len( chaine ) ):
    print(chaine[i])


# affichez mnt que les lettre (pas les espaces)

for i in range( len( chaine ) ):
    if( chaine[i] != ' '):
        print(chaine[i])


# affichez mnt que les voyelles 
for i in range( len( chaine ) ):
    if( chaine[i] == 'a' or chaine[i] == 'e' or chaine[i] == 'i' or chaine[i] == 'o' or chaine[i] == 'u' or chaine[i] == 'y'  ):
        print(chaine[i])



#Une 2eme methode plus intersante


for i in range( len( chaine ) ):
    if( chaine[i] in "AEIOUYaeiouy" ):
        print(chaine[i])





#Transformer tous lettre en majuscule


for i in range(len(chaine)):
    if( chaine[i] == ' '):
        print( chaine[i] )
    else :
        if( chaine[i].islower() ):
            print( chaine[i].upper() )
        else :
            print(chaine[i])
    



