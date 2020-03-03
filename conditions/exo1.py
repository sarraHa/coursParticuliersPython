


#Ecrivez un programme, on lui donnant l'age d'une personne 
#le programme nous dit si la personne est majeure ou mineure





#Mettez le programme dans une fonction 
def agedelapersonne(age):
    if age >= 18 :
        print("la personne est majeure")
    else :
        print("la personne est mineure")

#Appelez la fonction
agedelapersonne(23)



# 3eme methode



def majeurOUmineur2( age ):

	ageDeMajorite = 18
	if( age >= ageDeMajorite ):
		return "Vous etes majeur :)"
	else :
		return "Vous etes mineur "



age = 15
chaine = majeurOUmineur2( age )


print( chaine )