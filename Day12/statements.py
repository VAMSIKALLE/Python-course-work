'''
my_pin = "vamsi"
for i in range(5):
    
    user_pin = input("Enter your pin: ")
    if user_pin == my_pin:
        print("Pin  match")
        break
    else:
        print("Pin not Match")
else:
    print("try again after  seconds")
''''''''''''''''''''''''''''''''''''''''''
l =[2,3,5,6,8,10,34,12]
c = int(input())
for i in range(len(l)):
    if l[i] == c:
        print(f'{c} is found at index-{i}')
        break
else:
    print(f'{c} is  not found')
''
a = input()
if len(a) < 8:
    print("password must contain 8 charecters")
elif a == a.lower():
    print("first letter should be upper case")
elif a not in "@#$%^&":
    print("must have special charecter")
elif a not in "0987654321":
    print("must have a number")
else:
    print("it is a correct password")
    
''
password = input("Enter the password : ")
if len( password)>=8:
    s = set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(s) == 4:
        print("Strong password")
    else:
        print("weak password")

else:
    print("Weak password")
    ''
status = None
assert status != None
print(status)
'''
name ='abc'
batch = 55
age = 45
assert (name!= None and batch!=None and age!=None),"You need to update the data"
print(name,batch,age)
