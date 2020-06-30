'''
Ugly numbers are those number whose prime factors are 2, 3 or 5. 
From 1 to 15, there are 11 ugly numbers 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15. 
The numbers 7, 11, 13 are not ugly because they are prime. 
The number 14 is not ugly because in its prime factor the 7 will come.
'''


def pf(n):
	a=[]
	while n > 1:
		for i in range(2,n+1):
			# print(f'debug_outer : i: {i} ** n : {n}')
			if n%i == 0:
				# print(f'output : {i}')
				a.append(i)
				# print(f'debug_inner : n : {n} ** n/i : {n/i}')
				n = n//i
				break
	return a
	
def isugly(n):
	if n < 5:
		return True
	return False
	
	

a = pf(int(input("Number : ")))

print(f'factors : {a}')
b = [isugly(x) for x in a]
print(f'Ugly Number : {all(b)}')
