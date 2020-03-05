

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


#Expliquez-moi ce que le prof attend que vous fassiez dans cet exo ???


#Ecrivez une fonction qui demande a l'ulisateur de saisir un caractere et l'affiche apres
#saisissez un caractere :
#a
#vous avez saisi : a


def afficheCaractere():
	print("saisissez un caractere")
	c = raw_input()
	print("vous avez saisi : ", c)

#afficheCaractere()



#Ecrivez une fonction qui demande  *a chaque fois* a l'utlisateur de saisir un caractere puis affiche ce dernier
#saisissez un caractere :
#a
#vous avez saisi : a
#saisissez un caractere :
#1
#vous avez saisi : 1
#saisissez un caractere :
#.
#vous avez saisi : .
# ....


def afficheCaractereS():
	#on peut faire while(1)
	while(True):
		print("saisissez un caractere")
		c = raw_input()
		print("vous avez saisi : ", c)

#afficheCaractereS()

#Ecrivez un programme qui demande de a l'utilisateur de saisir des caracteres 
# et au bout de 4 caracteres saisi le programme sort


def affiche4CaractereS():
	nbChiffre = 0
	while(nbChiffre < 4):
		print("saisissez un caractere")
		c = raw_input()
		print("vous avez saisi : ", c)
		nbChiffre = nbChiffre + 1

#affiche4CaractereS()



#Ecrivez un programme qui demande de a l'utilisateur de saisir "que" des chiffre (ou nombre) 
# et au bout de 4 chiffres saisi le programme sort

#saisissez un chiffre :
#1
#vous avez saisi : 1
#saisissez un chiffre :
#2
#vous avez saisi : 2
#saisissez un chiffre :
#a
#saisissez un chiffre :
#b
#...

def affiche4Chiffres():
	nbChiffre = 0
	while(nbChiffre < 4):
		print("saisissez un chiffre")
		c = raw_input()
		if(c.isdigit() == True):
			print("vous avez saisi : ", c)
			nbChiffre = nbChiffre + 1

#affiche4Chiffres()

#autre methode avec code ascii
#d'abord d'est quoi le code ascii ???

#petit exo ecrivez une fonction qui prend un caractere et affiche son code ascii
# indication : ord(c)

def afficheCodeAscii(c):
	codeAscii = ord(c)
	print("le code ascii de ", c, "est : ", codeAscii)


#afficheCodeAscii('1')


#petit exo ecrivez mnt une fonction qui prend un code Ascii et affiche le caractere corespondant
# indication : chr(codeAscii)


def afficheCaractereDeCodeAscii(codeAscii):
	c = chr(codeAscii)
	print("le caractere qui corespond au code ascii ", codeAscii, "est : ", c)


#afficheCaractereDeCodeAscii(60)

#ecrivez mnt la fonction avec en utilisant le code Ascii

def affiche4Chiffres2():
	nbChiffre = 0
	while(nbChiffre < 4):
		print("saisissez un chiffre")
		c = raw_input()
		if( ord(c) >= 48 and ord(c) <= 59):
			#si le programme arrive la c'est a dire l'utilisateur a bien saisi un chiffre et pas un caractere
			print("vous avez saisi : ", c)
			nbChiffre = nbChiffre + 1
		

#affiche4Chiffres2()


#Ecrivez mnt la meme fonction d'avant mais en assurant que l'utilisateur 
# a bien saisi un chiffre pas un nombre



def affiche4Chiffres3():
	nbChiffre = 0
	while(nbChiffre < 4):
		print("saisissez un chiffre")
		c = raw_input()
		if( len(c) == 1):
			if( ord(c) >= 48 and ord(c) <= 59):
				#si le programme arrive la c'est a dire l'utilisateur a bien saisi un chiffre et pas un caractere
				print("vous avez saisi : ", c)
				nbChiffre = nbChiffre + 1
			


#affiche4Chiffres3()

#Ecrivez la meme fonction d'avant, mais cette la fonction doit afficher le nombre en entier a la fin de la saisi
# exemple :
# 1
# 2
# 5
# 0
# vous avez saisi 1250


#Petit rappel des tableaux 



def afficheNombre():
	nbChiffre = 0
	tabChiffre = []
	while(nbChiffre < 4):
		print("saisissez un chiffre")
		c = input()
		if( len(c) == 1):
			if( ord(c) >= 48 and ord(c) <= 59):
				#si le programme arrive la c'est a dire l'utilisateur a bien saisi un chiffre et pas un caractere
				print("vous avez saisi : ", c)
				tabChiffre.append(c)				
				nbChiffre = nbChiffre + 1
	#on affiche mnt le nombre avec une boucle
	print("le nombre que vous avez saisi est : ")

	for i in range(len(tabChiffre)):
		print(tabChiffre[i], end="")
	print("\n")



#afficheNombre()


#Autre methode pour afficher le nombre à la fin

def afficheNombre1():
	nbChiffre = 0
	tabChiffre = []
	while(nbChiffre < 4):
		print("saisissez un chiffre")
		c = input()
		if( len(c) == 1):
			if( ord(c) >= 48 and ord(c) <= 59):
				#si le programme arrive la c'est a dire l'utilisateur a bien saisi un chiffre et pas un caractere
				print("vous avez saisi : ", c)
				tabChiffre.append(c)				
				nbChiffre = nbChiffre + 1
	nombre = int(tabChiffre[0])*1000 + int(tabChiffre[1])*100 + int(tabChiffre[2])*10 + int(tabChiffre[3])
	print("le nombre que vous avez saisi est : ", nombre)
	


#afficheNombre1()

#******Fonction finale****
#cette fonction affiche un nombre saisi par l'utlisateur ce nombre est a 4 chiffre
# affiche le nombre saisi et son double

def afficheNombre2():
	nbChiffre = 0
	tabChiffre = []
	while(nbChiffre < 4):
		print("saisissez un chiffre")
		c = input()
		if( len(c) == 1):
			if( ord(c) >= 48 and ord(c) <= 59):
				#si le programme arrive la c'est a dire l'utilisateur a bien saisi un chiffre et pas un caractere
				print("vous avez saisi : ", c)
				tabChiffre.append(c)				
				nbChiffre = nbChiffre + 1
	nombre = int(tabChiffre[0])*1000 + int(tabChiffre[1])*100 + int(tabChiffre[2])*10 + int(tabChiffre[3])
	print("le nombre que vous avez saisi est : ", nombre, "le double de ce nombre est :", nombre*2)
	



afficheNombre2()





