


#ecrivez un programme qui affiche tous les tables de multiplication 
#la table de multiblication de  2
#2 * 1 = 2
#2 * 2 = 4
#2 * 3 = 6
#2 * 4 = 8
#2 * 5 = 10
#2 * 6 = 12
#2 * 7 = 14
#2 * 8 = 16
#2 * 9 = 18



def table():
    for i in range(0,11):
        print "la table de multiplication de" ,i, "est:"
        for j in range(0,11):
            print i,"*",j,"=", i*j
        print("\n")


table()