from datetime import datetime,time,date

from sqlalchemy.sql.functions import current_time

#current date
today = datetime.today()
print("current Date:",today)

print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)
#current date and time
now = datetime.now()
print("Current Date and Time:",now)
#current time
current_time=datetime.now().time()
print("Current Time:",current_time)

#using time
t = time(14,30,45)
print("Hour:",t.hour)
print("Minute:",t.minute)
print("Second:",t.second)

d=date(2025,11,13)
t=time(18,30,0,1)
combined=datetime.combine(d,t)
print("Combined DateTime:",combined)

year=int(input("Enter Year:"))
month=int(input("Enter Month:"))
day=int(input("Enter Day:"))

hour=int(input("Enter Hour:"))
minute=int(input("Enter Minute:"))
d=date(year,month,day)
t=time(hour,minute)
dt=datetime.combine(d,t)
print("Combined Date and Time:",dt)
