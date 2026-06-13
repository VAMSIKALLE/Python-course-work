'''
data = {
    'vamsi':{'status':True,'python':98,'mysql':95,'flask':94},
    'jaswanth':{'status':True,'python':78,'mysql':65,'flask':84},
    'pradeep':{'status':False,'python':None,'mysql':None,'flask':None},
    'prakash':{'status':True,'python':68,'mysql':55,'flask':64},
    'achu':{'status':True,'python':33,'mysql':25,'flask':34},
    }

name =  input("Enter the student name : ")
if name in data :
    if data[name]['status']:
        total = data[name]['python']+data[name]['mysql']+data[name]['flask']
        a = total/3
        avg = int(a)
        if avg>=90:
            print(f'Congratulations {name}!!!!!,You Got First class your avg is :',avg)
        elif avg>=70:
            print(f'Good {name} ,Keep it up for the next time!! your avg is :',avg)
        elif avg >= 35:
            print(f'Better {name},Work hard next time!!!! your avg is: ',avg)
        else:
            print(f'{name} ,You have failed in the exam Please Bring your parents   your avg is : ',avg)
    else:
        print(f"{name} didn't write the exam Bring your parents")
else:
    print(f"{name} 's Data is not found from the database!!!!!!!!!!!!")
'''
hrs,min = list(map(
    
