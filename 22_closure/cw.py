# Soojin Choi
# SoftDev2 pd07
# K22 -- Closure
# 2019-04-30

def repeat(w):
    def time(t):
        return w*t
    return time
    

r1 = repeat("hello")
r2 = repeat("goodbye")

print("\nREPEAT:")

print(r1(2))
print(r2(2))

print(repeat('cool')(3))


def outer():
    x = "foo"
    def inner():
        nonlocal x #ver2 python3
        x = "bar"
    inner()
    return x

print(outer())

print("\nCOUNTER:")

def make_counter():
    x = 0
    def inner(ret = False):
        if not ret:
            nonlocal x
            x = x + 1
            return x
        else:
            return x
    return inner
    print(x)
    return x

ctr1 = make_counter()
print(ctr1())
print(ctr1())

ctr2 = make_counter()
print(ctr2())
print(ctr1(True))
print(ctr2())

print("\nCW:")

def inc(x):
    return x+1

f = inc
print(f(10))

def adder(a,b):
    return a+b

def caller(c):
    print(c(2,4))
    print(c(3,5))

caller(adder)

# A closure remembers the context in which it was created.
# Even if you obliterate the creator fxn

def outer(x):
    def contains(l):
        return x in l
    return contains

contains_15 = outer(15)
var1 = contains_15([1,2,3,4,5])
var2 = contains_15([13,14,15,16,17])
var3 = contains_15(range(1, 20))
print(var1,var2,var3)

outer(42)

del outer
#outer(42)

var4 = contains_15(range(14,20))
print(var4)

# define nested fxn
#
#
