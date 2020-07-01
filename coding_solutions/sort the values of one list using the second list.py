'''
Given two lists, sort the values of one list using the second list
'''

#l1 = [x for x in input("l1 : ").split()]
#l2 = [int(x) for x in input("l2 : ").split()]

l1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
l2 = [ 0, 1, 1, 0, 1, 2, 2, 0, 1] 

#l1 =  ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#l2 = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]

z = zip(l2,l1)

z = sorted(z)
r = [x[1] for x in z]

print(r)
