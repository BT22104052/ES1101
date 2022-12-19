#1
income=int(input('User Income:'))
dep=int(input('No. of Dependents:'))
a=10000
b=3000
rate=0.20
x=income-a-(b*dep)
print('Taxable Income:',x)
O=x*rate
print('Income Tax:',O)

#2
a=int(input('first number:'))
b=float(input('second number:'))
c=input('third number:')
x=a+float(b)+int(c)
print(x)

#3
a=int(input('Number 1:'))
b=int(input('Number 2:'))
c=int(input('Number 3:'))
x=(a+b+c)/3
print(x)

#4
a=int(input('Number Of Seconds:'))
x=a//60
y=a%60
q="minutes"
w="seconds"
print(x, q,"and", y, w)

#5
from math import *
#create a for loop
for x in range(0, 345,15) :
    #thenprint the sine and cosine of the angles
    print(x,'---', round(sin(x),4), round(cos(x),4))