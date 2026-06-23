'''
import sys
print(sys.argv)
print(sys.path)
print(sys.version)
print("Before Exit")
print(sys.exit())

print("After Exit")
==========================================
import platform
print(platform.system(),platform.release(),platform.processor())
=============================================
import math
print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.pow(2,5))

print(math.ceil(12.3))
print(math.ceil(12.000001))
print(math.ceil(12.999999))
print(math.ceil(12.8))

print(math.floor(12.3))
print(math.floor(12.000001))
print(math.floor(12.9999999))
print(math.round(20.8))
print(math.round(20.3))
print(math.round(20.5))
================================================
import random
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))
l = ['pyhton','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'

print(random.choice(s))
print(l)
random.shuffle(l)
print(l)
================================================
import collections
s = 'python pppprogramming'
d = collections.Counter(s)
print(d,end="")
================================================
import collections
l = collections.deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
================================================'''
from itertools import combinations,permutations
a = combinations('abcd', 2)
print([''.join(i) for i in a])
b = permutations('abcd', 2)
print([''.join(i) for i in b])






