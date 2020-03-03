

#Afficher caractere par caractere tous les caracteres de la chaine suivante

chaine = "Bonjour tous le monde"



#for i in range(0,len(chaine)):
#    print(chaine[i])


#2eme methode

#for j in chaine :
#    print(j)



# afficher mnt que les lettre (pas les espaces)


#for i in range(0,len(chaine)):
#    if( chaine[i] == ' ' ):
#        print('*')
#    else: 
#        print(chaine[i])







#Affichez mnt que les voyelles 

#for i in range(0,len(chaine)):
#    if( chaine[i] == 'a' or chaine[i] == 'e' or chaine[i] == 'i' or chaine[i] == 'o' or chaine[i] == 'u' or chaine[i] == 'y' ):
#        print(chaine[i])



#for i in range(0,len(chaine)):
#    if( chaine[i] in "aeiouy" ):
#        print(chaine[i])





#Transformer tous lettre en majuscule

#for i in range (0,len(chaine)):
#    if (chaine[i].islower ):
#        print (chaine[i].upper())




for i in range(len(chaine)):
    if( i%2 == 0):
        
        print(chaine[i])

