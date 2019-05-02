# 

import random

def make_HTML_heading(f):
    txt = f()
    def inner():
        return '<h1>' + txt + '</h1>'
    return inner

# equiv to greet = make_HTML_heading(greet)
@make_HTML_heading # v1
def greet():
    greetings = ["Hello","Welcome","AYO!", "Hola", "Bonjour", "Word up"]
    return random.choice(greetings)

print(greet()) #  v1
# v0 greet_heading = make_HTML_heading(greet)
# v0 print(greet_heading())

# memoization -> process of storing previously calculated results to avoid recalculation

# fib
def memoization(fxn):
    val = {}
    def inner(n):
        if n not in val:
            print(n)
            val[n] = fxn(n)
        return val[n]
    return inner

@memoization
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #elif n in val:
    #    return val[n]
    else:
        calc = fib(n-1) + fib(n-2)
    #    val[n] = calc
        return calc

#fib = memoization(fib)
print(fib(7))




