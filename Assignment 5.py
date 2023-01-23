#ANS1
txt=str(input(" "))
txt1=txt[::-1]
print(txt1)



#ANS2
a=int(input("range:"))
b=int(input("User Number:"))
for i in range(a):
    if i%b==0:
        print(i)
        continue
 



#ANS3
a = int(input("Enter the first length: "))
b = int(input("Enter the second length: "))
c = int(input("Enter the third length: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Yes")   
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print('The area of the triangle is %0.2f' %area)  
else:
    print("No") 
    
    
    
    
#ANS4
n=int(input("No. of Rows: "))
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    
    
    
#ANS5
n=int(input("No. of Rows: "))
x=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(x), end="")
        x=x+1
    print('')



#ANS6
n=int(input("range:"))
for number in range (n):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  



#ANS7
n=[]
for i in range(0,501,1):
    if i%11==0 and i%7==0:
       n.append(str(i))
print (n)


#ANS8
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = int(input())
  
    list.append(x) 
      
print(list)

#a Positive Numbers
for i in list:
    if i>=0:
        print(i, "is positive")
        continue
    
#b Negative Numbers
for i in list:
    if i<0:
      print(i,"is negative")
      continue

#c Odd Numbers
for i in list:
    if i%2!=0:
        print(i,"is Odd")
        continue

#d Even Numbers
for i in list:
    if i%2==0:
        print(i,"is Ever")
        continue
    
#e Number of times each number occurs in the List   
for i in list:
    a=list.count(i)
    print(f"Count of {i}={a}")
    continue
  
      

#ANS9
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    q=str(input())
  
    list.append(q) 
      
print(list)
for i in list:
    a=list.count(i)
    print(f"Count of {i}={a}")
    continue