#Ecrivez un programme, on lui donnant un nombre  
#le programme nous dit si le nombre est positif, negative ou nul



nombre = 8

if( nombre > 0 ):
    print("Ce nombre est positif")
elif( nombre < 0 ):
    print("Ce nombre est negatif")
else :
    print("Ce nombre est nul")




#Mettez le programme dans une fonction 


def positifNegtifNul( nombre ):

    if( nombre > 0 ):
        print("Ce nombre est positif")
    elif( nombre < 0 ):
        print("Ce nombre est negatif")
    else :
        print("Ce nombre est nul")





#Appelez la fonction

nombre = -5
positifNegtifNul( nombre )





#Modifiez le programme pour qui il revoit -1 si le nombre est negatif, 1 si le nombre est positif, O si le nombre est nul

def positifNegtifNul2( nombre ):

    if( nombre > 0 ):
        return 1
    elif( nombre < 0 ):
        return -1
    else :
       return 0



nombre = 1222
print(positifNegtifNul2( nombre ))



