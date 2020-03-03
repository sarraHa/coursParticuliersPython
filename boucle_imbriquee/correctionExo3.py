


#dessigner le triangle suivant
# *
# **
# ***
# ****


def triangle():
	compt = 1
	for i in range(4):
		for j in range(compt):
			print("*", end="")
		compt = compt + 1
		print("\n")


#triangle()

# en utilisant le i mantenant


def triangle2():
	for i in range(1, 5):
		for j in range(i):
			print("*", end="")
		print("\n")


#triangle2()


#ecrivez un programme qui dessigne un tringle de taille n
# si n = 2
# *
# **

#si n = 3
# *
# **
# ***




def triangle3(n):
	for i in range(1,n+1):
		for j in range(i):
			print("*", end="")
		print("\n")


triangle3(6)





