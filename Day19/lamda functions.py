'''
sysntax:                 lamda functions
var = lambda agr :exp

add =lambda a,b : a + b

print(add(12,13))
print(add(10,25))
============================================
wish = lambda name:f"Welcome to the python course {name}"

print(wish("Vamsi"))
print(wish("Jaswanth"))
============================================
Gst = lambda price: price + price*0.18
print(Gst(1000))
print(Gst(600))
print(Gst(89000))
=============================================
greatest = lambda a,b: a if a>b else b
print(greatest(10,20))
print(greatest(21,21))
print(greatest(234,220))
=============================================
iseven = lambda a: f"{a} is Even Number" if a%2 == 0 else f"{a} is Odd Number"

print(iseven(0))
print(iseven(24))
print(iseven(71))
=============================================
bill = lambda charge:charge if charge>99 else charge+30
print(bill(100))
print(bill(56))
print(bill(45))
=============================================

tag = lambda sales : if sales >999 "BEST SELLER"
print(tag(12345))
=============================================
login = True
instock = True
status = lambda login,instock:("You can Buy Product " if instock
else "product is out of stock") if login else "Login to buy a product"

print(status(login,instock))
=============================================
d ={'sugar':40,'
gst = dict(map(lambda i :,d.items()))
print(gst)
=============================================
l = [1,2,3,4,5,6,7]
res = list(map(lambda i:i**3,l))
print(res)
=============================================
names = ['subbu','nagndra','saith']
t = list(map(lambda i: ))
=============================================
l=[1,2,3,4,5,6,7,8,9,10,11,12]
res = list(filter(lambda i:i%2 == 0,l))
print(res)

l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i>5,l))
print(res)

l = [1,2,3,4,5,6,7]
res = list(filter(lambda i:i%3 == 0,l))
print(res)
=============================================
from functools import reduce
l = [1,2,3,4,5]
s = reduce(lambda sum,i:sum+i,l)
p = reduce(lambda pro,i:pro*i,l)
m = reduce(lambda max,i: max if max > i else i,l)
mi = reduce(lambda max,i:max if max < i else i,l)
print(s,p,m,mi)
============================================='''
d = {'vamsi':50,'pradeep':40,'naresh':60,'dinesh':80,'sahith':70}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse = True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))




































