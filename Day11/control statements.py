'''
s = "vamsi is a good boy"
for var in s:
    print(var)
''
l = ['sugar','salt','oil','eggs']
for item in l:
    print(item)
   ''
t = ('1.intro','2.Tokens','3.Data types')
for i in t:
    print(i)

s = {'laptop','mouse','keyboard','phone','charger'}
for i in s :
    print(i)
    ''
d = {'name':'vamsi','batch':55,'course':'PFS','skills':['python','mysql','java']}
for i in d:
    print(i,d[i])
''


# range(start,stop+1,step) ==> (o,n,1)
''
for i in range(1,11):
    print(i)''
for i in range(2,51,2):
    print(i)''

for i in range(5,101,5):
    print(i)
    ''
for i in range(20,0,-1):
    print(i)
''
for i in range(6):
    print(6,"*",i,"=",6*i)
''
s = 'looping statements'
for i in range(len(s)):
    print(i,s[i])
''
l = [7,2,4,5,6,2,4]
for i in range(len(l)):
    print(i,l[i])
''
s ='looping'
for i in enumerate(s):
    print(i[0],i[1])
  ''
t = [7,8,9,4,5,6]
for i in enumerate(t):
    print(i)
''
for i in range(10):
    if i == 5:
        continue
    print(i)
''

s = 'looping statements'
for i in s:
    if i in 'aeiou':
        print(i)
    '''
t = (9,2,13,4,5,6)
for i in range(len(t)):
    print(i*t[i])
