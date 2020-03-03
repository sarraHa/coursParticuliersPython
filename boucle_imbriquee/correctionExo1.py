

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

for i in range(1, 10):
	print "la table de multiblication de ", i
	for j in range(1, 10):
		print i, "*", j, "=", i*j
	print("\n")
