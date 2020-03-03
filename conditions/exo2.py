
#Ecrivez un programme, on lui donnant un nombre  
#le programme nous dit si le nombre est positif, negative ou nul

nombre = 5

if (nombre<0) :
    print("le nombre est negatif")
elif (nombre==0) :
    print("le nombre est nul")
else :
    print("le nombre est positif")
#Mettez le programme dans une fonction 



def nombresigne ( nombre ):
    nul = 0
    if (nombre<nul) :
        print("le nombre est negatif")
    elif (nombre==nul) :
        print("le nombre est nul")
    else :
        print("le nombre est positif") 






#Appelez la fonction



nombresigne(4)
nombresigne(-4)
nombresigne(0)

print("Notre 3eme fonction")

#Modifiez le programme pour qui il revoit -1 si le nombre est negatif, 1 si le nombre est positif, O si le nombre est nul
def renvoinombre ( nombre ):
    nul = 0
    if (nombre<nul) :
        return -1
    elif (nombre==nul) :
        return 0
    else :
        return 1

print renvoinombre(5)
a = renvoinombre(5)
print(a)