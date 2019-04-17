# Team Teal
# Angela Tom and Soojin Choi
# K19 -- Ready, Set, Math
# 2019-04-16

# Union
# 
def union(set1, set2):
    return [x for x in set1 if x not in set2] + set2    

print("Union")
print(union([1,2,3],[2,3,4]))
print(union([],[]))
print(union([3,6,8],[1,5,6]))

# Intersection
# {1,2,3} and {2,3,4} -> {2,3}
def inter(set1, set2):
    return [x for x in set1 for y in set2 if x == y]

print("Intersection")
print(inter([1,2,3],[2,3,4]))

# complement
# all members of U not in A (U/A)
def complement(set1, set2):
    return [x for x in set1 if x not in set2]

print("Complement")
print(complement([1,2,3],[2,3,4]))

#symmetric difference
#opposite of intersection (set difference)
def sym(set1, set2):
    list = [x for x in set1 if x not in set2]
    list2 = [y for y in set2 if y not in set1]
    return list + list2

print("Symmetric Difference")
print(sym([1,2,3],[2,3,4]))

# cartesian product of A and B
# {1,2} {red, white}
# {(1, red)(1, white)(2, red)(2, white)}

def cart(set1, set2):
    return [(x,y) for x in set1 for y in set2]

print("Cartesian Product")
print(cart([1,2],["red", "white"]))





def sortforset(set):
    pass

def triple(num):
    return [(a,b,c) for a in range(num) for b in range(a) for c in range(b) if a*a == b*b + c*c]

print(triple(10))
    
