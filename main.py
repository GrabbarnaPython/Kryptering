from encrypt import *

what=input("main or encrypt? ")

if what=="main":
	coords = []
	x = int(input("x? "))
	y = int(input("y? "))
	
	text = input("Krypterad text: ")
	lista = []

	for i in range(text):
		lista.append(0)

	for i in range(x):
			coords.append([])
			for k in range(y):
					coords[i].append('*')
			#print(coords[x])

	xPos = 0
	yPos = 0
	xIncrease = 1
	yIncrease = 1
	t=0
	
	code = []
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
	for q in range(x):
			for r in range(y):
					if coords[q][r] != '*':
						code.append(coords[q][r])
	print(code)
	v = 0
	for w in code:
		print(text[w])
		lista[w] = text[v]
		v += 1
	print(realcode)
else:
  encrypt()

realcode = ''

for i in range(len(list)):
	realcode += i