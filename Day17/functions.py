'''
n=10
def display():
    print("Inside:",n)

display()
print("Out Side:",n)
=================================def display():
    global n------>(GLOBAL VARIABLE)
    n  = 10
    print("Inside:",n)

display()
print("Out Side:",n)
==================================
def display():
    global n
    n+=10
    print("Inside:",n)
n =  10
display()
print("outside:",n)
===================================
def outer():
    n = 10
    def inner():
        nonlocal n------------------->(LOCAL VARIABLE)
        n+=10
        print("Inside:",n)
    inner()
    print("Outside:",n)

outer()
===================================
s = "vamsi"
print(len(s))

len = 5
print(len(s))
===================================
def update(n):
    n = False
    print("Inside:",n)
n = True
update(n)
print("Outside:",n)
===================================

def func(num):
    if num == 0:
        return
    print(num,end=" ")
    func(num-1)
    print(num,end=" ")

func(5)
===================================
def sumofdigits(n):
    if n == 0:
        return 0
    return n+sumofdigits(n-1)
n=5
print(sumofdigits(n))
===================================
def productofdigits(n):
    if n == 0:
        return 1
    return n*productofdigits(n-1)
n=5
print(productofdigits(n))
===================================
def power(bas,pow):
    if pow == 0:
        return 1
    return bas*power(bas,pow-1)
print(power(2,5))
==================================='''
