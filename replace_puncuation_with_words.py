dic = {'.' :'DOT','!':'EXCLAMATION MARK',',':'COMMA'}
def ReplacePancuation(inputString):
	orginalLength = len(inputString)
	extraSpace = 0
	for i in range(0,orginalLength):
		if inputString[i] in dic:
			extraSpace += (len(dic[inputString[i]]) - 1)

	while(extraSpace>0):
		inputString.append('')
		extraSpace-=1		

	j = 0
	orginalLength = orginalLength-1
	while j <= orginalLength:
		if inputString[j] in dic:
			chr = inputString[j]
			n = orginalLength
			a = len(dic[inputString[j]])
			while j < n:
				inputString[n+a-1] = inputString[n]
				n = n-1
			for k in range(0,a):
				inputString[j+k] = dic[chr][k]

			j = j + a-1
			orginalLength = orginalLength + a-1
		else:
			j=j+1	

	print(''.join(inputString))

inputString = list(input())
ReplacePancuation(inputString)		
