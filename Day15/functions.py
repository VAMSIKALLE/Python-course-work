'''
def function_name(arg):
        #statements
        return
function_name(para)
'''
'''
def wish(name):
    print(f'Welcome to the pyhton course {name}!')
wish("vamsi")
wish("Jaswanth")
wish("achu")
wish("ramakanath")
'''
'''
def wish(name):
    return name
print("Hello ",wish('vamsi'))
'''
'''
def iseven(num):
    if num%2 == 0:
        return f'{num} - is even number'
    else:
        return f'{num} - is odd number'

print(iseven(25))
print(iseven(42))
'''
'''
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
num = int(input("Enter a number:"))
print(factorial(num))
'''
'''
def isprime(num):
    for i in range(2,num//2):
        if num%2 == 0:
            return f"{num} - Not Prime Number"
    return f"{num} - Prime Number"

num = int(input("Enter a number:"))
print(isprime(num))
'''
'''
#positional arguments

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display("Vamsi","vamsikalle360@gmail.com","vvaammssii112233")
print("-----------------------------------------------------------------")
display("vani","vani@!@#.com","hddt112")
'''
'''
#keyword arguments
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display("Vamsi","vamsikalle360@gmail.com","vvaammssii112233")
print("-----------------------------------------------------------------")
display(email="vani",name="vani@!@#.com",pwd="hddt112")
'''
'''
#default arguments
def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display("Vamsi","vamsikalle360@gmail.com","vvaammssii112233")
print("-----------------------------------------------------------------")
display("vani","vani@!@#.com")
'''
'''
#variable Arguments
def display(*names):
    print("Names:",names)
    
display('vamsi','Ravi','rajesh')
display('raju','bharath')
'''
def display(**names):
    print("Names:",names)

display(k1="naresh",k2="akhil",k3="nagendra")
display(k1="nagendra")
