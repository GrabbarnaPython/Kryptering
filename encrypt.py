
def encrypt():
	coords = []
	x = int(input("x? "))
	y = int(input("y? "))
	
	text = input("Text? ")

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
	for p in range(len(text)):
		if coords[xPos][yPos] == '*':
			t+=1
			coords[xPos][yPos] = text[p]
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
	code=""
	for q in range(x):
			for r in range(y):
					if coords[q][r] != '*':
						code+=coords[q][r]
	print(code)