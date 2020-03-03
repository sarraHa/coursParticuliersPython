




#ecrivez un programme qui dessigne un tringle de taille n
# si n = 2
# **
# *

#si n = 3
# ***
# **
# *



def tringle(n):
	nb_lignes = n
	for i in range(n):
		for j in range(nb_lignes):
			print("*", end="")
		print("\n")
		nb_lignes -= 1

tringle(5)
