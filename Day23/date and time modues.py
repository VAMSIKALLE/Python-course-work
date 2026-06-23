'''
from datetime import date,time,datetime,time
t = date.today()

print(t)
print("YEAR:",t.year)
print("MONTH:",t.month)
print("DAY:",t.day)M 0:",t.weekday())
print("WEEKDAY FROM 1:",t.isoweekday())
=================================================
from datetime import date,time,datetime,time
t = date(2026,12,30)
print(t)
=================================================
from datetime import date,time,datetime,time
t = time(23,59,0)
print(t)
=================================================
from datetime import date,time,datetime,time
n = datetime.now()

print(n)
print("Year:",n.year)
print("Month:",n.month)
print("Day:",n.day)
print("Hour:",n.hour)
print("Minute:",n.minute)
print("Second:",n.second)
=================================================
from datetime import date,time,datetime,time
n = datetime.now()

print(n.strftime(   '%d/%m/%y'))
print(n.strftime(   '%d/%m/%y %H:%M:%S'))
print(n.strftime(   '%d/%m/%y %I:%M:%S %p'))
print(n.strftime(   '%d-%b-%y %I:%M:%S %p'))
print(n.strftime(   '%d %B %y %I:%M:%S %p'))
print(n.strftime('%a %d %B,%Y %I:%M:%S %p'))
print(n.strftime('%A %d %B,%Y %I:%M:%S %p'))
================================================='''
from datetime import date,time,datetime,timedelta
n = datetime.now()

n15 = n + timedelta(minutes = 15)
n2 = n + timedelta(hours=2)
n7 = n + timedelta(days = 60)

print(n15,n2,n7,sep = '\n')


