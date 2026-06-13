'''
s = 'pyhton'
for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=" ")
''
l = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in l:
    for j in i:
        sum += j
print(sum9)
''
d = {
    '1234':{'pin':'4567','balance':23000},
    '2345':{'pin':'9876','balance':53000},
    '3456':{'pin':'5678','balance':63000},
    '4567':{'pin':'9876','balance':73000},
    }
for i in d:
    print("account number:",i)
    print("pin:",d[i]['pin'])
    print("balance:",d[i]['balance'])
    print("---------------------------------------------------")
''
n = int(input("enter the n : "))
for row in range(n):
    for col in range(n):
        print( col % 2,end ='')
    print()
''
n =  int(input("Enter the size :"))
for row in range(n):
    for col in range(row+1):
        print("*",end='')
    print()
    ''
n = int(input())
for i in range(n):
    for sp in range(n-1-i):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()
    ''
n = int(input())
for row in range(n):
    for sp in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()
''
n = int(input("enter the n : "))
for row in range(n):
    for col in range(n):
        print((row+col) % 2,end ='')
    print()
'''
n = int(input())
c = 1
for row in range(n):
    for col in range(row+1):
        print(c, end=" ")
        c += 1
    print()
