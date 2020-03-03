

#Ecrivez un programme qui calcule la somme des 10 premiers nombres ( de 0 a 10)
def sommenombres():
    somme = 0
    for i in range(0,11):
        somme += i
    return somme 

#a=sommenombres()
#print (a)




# la somme de nombre pair



def sommenombres2():
    somme=0
    for i in range(0,11,2):
        somme=somme+i
    return somme


#b=sommenombres2()
#print(b)



def sommenombres3():
    somme=0
    for i in range(0,11):
        if i%2 == 0:
            somme=somme+i
            
    return somme


print( sommenombres3() )