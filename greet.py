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
def fib(fxn):
    val = {}
    def inner(n):
        
        return 0
    return inner


def helper():
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return helper(n-1) + helper(n-2)

helper = fib(helper)
print(helper(40))




