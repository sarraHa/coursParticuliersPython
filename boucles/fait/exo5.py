


#Ecrivez un programme qui prend un nombre est indique si ce nombre et pair ou impair

#n = 9
#if n%2 == 0:
#    print n," est pair"
#else :
#    print n," est impair"


#Mettez le programme dans une fonction 
def pairimpair(n):

    if n%2 == 0:
        print n," est pair"
    else :
        print n," est impair"



#Appelez la fonction
#pairimpair(11)



#Cette fois-ci c'est l'utilisateur qui saisit le nombre

def pairimpair2():
    print("saisissez un nombre")
    n = input()
    if n%2 == 0:
            print n," est pair"
    else :
        print n," est impair"


#pairimpair2()

#L'utilisateur donne un entier positif n et le programme affiche tous les nombre pair de 0 a n et dire si ils sont pair ou impair
# 0 est un nombre pair
# 1 est un nombre impair

def pairimpair3():

    print("saisissez un nombre positif")
    n = input()
    for i in range(0,n+1):
        if i%2 == 0:
            print i," est pair"
        else :
            print i," est impair"

#pairimpair3()

def pairaimpair4():

    print('saisissez un nombre positif')
    i=input()

    while i>=0:
        if i%2==0 :
            print  (i, ' est pair')
        else :
            print(i, ' est impair')

        print('saisissez a nouveau un nombre positif')
        i=input()


pairaimpair4()



