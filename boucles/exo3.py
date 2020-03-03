


#Ecrivez un programme permettant de calculer le factorial d'un nombre entier
# rappel factorial de 4 = 1*2*3*4 = 24

def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact = fact * i
    return fact



print "Factorial de 4 est ", factorial(4)
print "Factorial de 5 est ", factorial(5)



