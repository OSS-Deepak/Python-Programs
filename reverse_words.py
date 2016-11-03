inputS = input()
inputString = list(inputS)
def reverse(start,end):
	while start <= end:
		temp = inputString[start]
		inputString[start] = inputString[end]
		inputString[end] = temp
		start = start + 1
		end = end - 1


def reverseWords():
	start = 0
	length = len(inputString)
	end = length - 1
	reverse(start,end)
	for i in range(0,length):
		if inputString[i] == ' ':
			end = i-1
			reverse(start,end)
			start = i+1
		if i == length-1:
			end=i
			reverse(start,end)
		

reverseWords()
print(''.join(inputString))