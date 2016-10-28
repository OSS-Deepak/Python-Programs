import math
def cubeRoot(n):
	start = 0
	end = n
	e = 0.0000000000001
	mid = 0
	diff = 0
	while True:
		mid = (start + end) / 2
		temp = mid*mid*mid
		if n > temp:
			diff = n - temp
		else:
			diff = temp - n

		if diff <= e:
			return mid 

		if temp > n:
			end = mid
		else:
			start = mid

number = int(input())
print(cubeRoot(number))
