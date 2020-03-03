


#Ecrivez un programme qui prend un nombre est indique si ce nombre et pair ou impair

n = 7

if( n%2 == 0):
    print(n, "est un nombre pair")
else :
    print(n, "est un nombre impair")



#Mettez le programme dans une fonction 

def paiImpair (n ):

    if( n%2 == 0):
        print(n, "est un nombre pair")
    else :
        print(n, "est un nombre impair")





#Appelez la fonction

#paiImpair ( 15 )


#Cette fois ci c est l utilisateur qui saisit le nombre

def paiImpair2():

    print "Saisissez un nombre"
    n = input()
    if( n < 0 ):
        print "merci de saisir un nombre positif"
        return
    if( n%2 == 0):
        print n, "est un nombre pair"
    else :
        print n, "est un nombre impair"


#paiImpair2()





#L'utilisateur donne un entier positif n et le programme affiche tous les nombre pair de 0 a n et dire si ils sont pair ou impair
# 0 est un nombre pair
# 1 est un nombre impair



def paiImpair3():

    print "Saisissez un nombre"
    n = input()
    if( n < 0 ):
        print "merci de saisir un nombre positif"
        return
    
    for i in range (0, n+1):
        if( i%2 == 0):
            print i, "est un nombre pair"
        else :
            print i, "est un nombre impair"


#paiImpair3()


# avec un while mnt


def paiImpair4():

    n = 0
    while( n >= 0):
    
        print "\nSaisissez un nombre positif\n"
        n = input()
    
        if( n%2 == 0):
            print n, "est un nombre pair"
        else :
            print n, "est un nombre impair"

    print "je vous ai dit de saisir un nombre positif :("
  


paiImpair4()