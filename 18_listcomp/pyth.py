# Soojin Choi
# SoftDev1 pd08
# K18 -- Getting Clever with List Comprehensions
# 2019-04-15

def triple(num):
    return [(c, b, a) for a in range(num) for b in range(a) for c in range(b) if a*a == b*b + c*c]

print(triple(19))