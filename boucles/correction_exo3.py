


#Ecrivez un programme permettant de calculer le factorial d'un nombre entier
# rappel factorial de 4 = 1*2*3*4 = 24



def factorial(n):
    resultat = 1
    for i in range(1, n+1):
        resultat = resultat * i
    return resultat



print "Factorial de 4 est ", factorial(4)
print "Factorial de 5 est ", factorial(5)



