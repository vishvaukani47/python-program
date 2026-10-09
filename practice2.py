from datetime import datetime,date,time

from unit1_1p import expression, result

now=datetime.now()
formatted=now.strftime("%d/%m/%Y %H:%M:%S")
print(formatted)

dt1=datetime(2025,11,13,10,0)
dt2=datetime(2025,11,13,15,0)
print("dt1<dt2:",dt1<dt2)
print("dt2<dt1:",dt2<dt1)

exam_date=date(2025,8,10)
today=date(2025,8,5)
if today<exam_date:
    print("Exam is coming...")
elif today==exam_date:
    print("Exam is today...")
else:
    print("Exam is not today...")

dates=[
    date(2025,8,10),
    date(2025,5,15),
    date(2025,7,1),
]
dates.sort(reverse=True)
print(dates)

expression="1+2*10/2"
print(eval(expression))

expression="*x*(x+2)*(x+5)"
x=2
print(eval(expression))

expression="*x*(x+2)*(x+5)"
x=2
print(eval(expression,{"x":3}))

expression="*x*(x+2)*(x+5)"
x=2
print(eval(expression,{"x":3},{"x":4}))

x=10
y=20
result=eval("x+y",{},{"x":100,"y":200})
print(result)
print(eval("x",{"x":10},{"x":20}))

chars=('a','b','c')
print("'d' in chars:",eval("x",{"'d'in chars"}))