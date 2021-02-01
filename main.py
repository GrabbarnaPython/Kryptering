from encrypt import *

what=input("main or encrypt? ")

if what=="main":
	coords = []
	xPos = 0
	yPos = 0
	xIncrease = 1
	yIncrease = 1
	t = 0
	v = 0
	x = int(input("x? "))
	y = int(input("y? "))

	lista = []
	text = input("Krypterad text: ")

	for i in range(len(text)):
		lista.append(0)

	for i in range(x):
			coords.append([])
			for k in range(y):
					coords[i].append('*')
			#print(coords[x])


	for p in range(len(text)):
		if coords[xPos][yPos] == '*':
			coords[xPos][yPos] = t
			t+=1
		xPos += xIncrease
		yPos += yIncrease
		
		if xPos == x-1:
			xIncrease = -1
		elif xPos == 0:
			xIncrease = 1
		
		if yPos == y-1:
			yIncrease = -1
		elif yPos == 0:
			yIncrease = 1

	for j in range(len(coords)):
		print(coords[j])
	code=[]
	realcode=""
	for q in range(x):
			for r in range(y):
					if coords[q][r] != '*':
						code.append(coords[q][r])
	print(code)
	for w in code:
		lista[w] = text[v]
		v += 1
	for g in range(len(lista)):
		realcode+=lista[g]
	print(realcode)
else:
	encrypt()