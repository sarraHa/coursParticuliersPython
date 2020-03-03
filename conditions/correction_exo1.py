


#Ecrivez un programme, on lui donnant l'age d'une personne 
#le programme nous dit si la personne est majeure ou mineure



#1er methode
age = 18


if( age >= 18 ):
	print("Vous etes majeur :)")
else :
	print("Vous etes mineur ")



#2eme methode
#Mettez le programme dans une fonction 


def majeurOUmineur( age ):

	ageDeMajorite = 18
	if( age >= ageDeMajorite ):
		print("Vous etes majeur :)")
	else :
		print("Vous etes mineur ")



#Appelez la fonction

age = 2
majeurOUmineur( age )


# 3eme methode



def majeurOUmineur2( age ):

	ageDeMajorite = 18
	if( age >= ageDeMajorite ):
		return "Vous etes majeur :)"
	else :
		return "Vous etes mineur "



age = 15
print( majeurOUmineur2( age ) )