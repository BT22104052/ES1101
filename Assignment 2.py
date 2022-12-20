#Ans 1
name='Python is a case sensitive language'

#a
print(len(name))

#b
print(name[::-1])

#c
print(name[10:26])

#d
newname=name.replace("a case sensitive","object oriented")
print(newname)

#e
x=name.index("a")
print(x)

#f
y=name.replace(" ","")
print(y) 
y1=newname.replace(" ","")
print(y1)

#Ans 2
name = "Arool Bhatia"
sid = "22104052"
department = "Electrical Engineering"
cgpa = 9.9

output = "Hey, {} Here!\nMy SID is {}\nI am from {} department and my CGPA is {}".format(name, sid, department, cgpa)
print(output)


#Ans 3
a=56
b=10

#a
i=a&b
print(i,bin(i))

#b
j=a|b
print(j,bin(j))

#c
k=a^b
print(k,bin(k))

#d
l=a<<2
m=b<<2
print(l,bin(l))
print(m,bin(m))

#e
n=a>>2
p=b>>4
print(n,bin(n))
print(p,bin(p))

#Ans 4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if (num1 >= num2) and (num1 >= num3):
   greatest = num1
elif (num2 >= num1) and (num2 >= num3):
   greatest = num2
else:
   greatest = num3
print("The greatest of the three numbers is", greatest)


#Ans 5
string = input("Enter a string: ")
if "name" in string:
    print("Yes")
else:
    print("No")


#Ans 6
length1 = int(input("Enter the first length: "))
length2 = int(input("Enter the second length: "))
length3 = int(input("Enter the third length: "))

if (length1 + length2 > length3) and (length1 + length3 > length2) and (length2 + length3 > length1):
    print("Yes")
else:
    print("No")
