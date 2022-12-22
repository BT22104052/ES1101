#Ans 1
string = input("Enter a string: ")
words = string.split() if " " in string else list(string)
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)


#Ans 2
import datetime
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
if not (1 <= month <= 12) or not (1 <= day <= 31) or not (1800 <= year <= 2025):
  print("Invalid input date")

else:
  input_date = datetime.datetime(year, month, day)
  
  next_date = input_date + datetime.timedelta(days=1)

  print("Next date:", next_date.strftime("%Y-%m-%d"))


#Ans 3
result = []
for i in range(1,11):
  t = (i, i**2)
  result.append(t)
print(result)

#Ans 4
grade = int(input("Enter a grade between 4 and 10: "))

if grade < 4 or grade > 10:
  print("Error: grade must be between 4 and 10")
else:
  if grade >= 9:
    letter_grade = "A"
    performance = "Excellent"
  elif grade >= 8:
    letter_grade = "B"
    performance = "Very Good"
  elif grade >= 7:
    letter_grade = "C"
    performance = "Good"
  elif grade >= 6:
    letter_grade = "D"
    performance = "Average"
  else:
    letter_grade = "F"
    performance = "Below Average"
    
  print("Your Grade is {} and {} performance".format(letter_grade,performance))
  

#Ans 5
for i in range(10, 0, -1):
    for j in range(11-i):
        print(" ", end="")
    for k in range(i):
        print(chr(65+k),end=" ")
    print()

    
#Ans 6
students = {} 

while True:
    name = input("Enter the name of the student: ")
    sid = input("Enter the SID of the student: ")

    students[sid] = name

    more = input("Do you want to add more students (Y/N)? ")
    if more.upper() == 'N':
        break

print("\nStudents' Details:")
for sid, name in students.items():
    print(f"SID: {sid}, Name: {name}")

sorted_students = sorted(students.items(), key=lambda x: x[1])

print("\nSorted Students (by name):")
for sid, name in sorted_students:
    print(f"SID: {sid}, Name: {name}")

sorted_students = sorted(students.items(), key=lambda x: x[0])

print("\nSorted Students (by SID):")
for sid, name in sorted_students:
    print(f"SID: {sid}, Name: {name}")

sid = input("\nEnter the SID of the student you want to search: ")
if sid in students:
    print(f"Name of the student with SID {sid}: {students[sid]}")
else:
    print(f"No student found with SID {sid}")
    
    
#Ans 7
n = 10
a, b = 0, 1
sum = 0
print(a)
print(b)
sum = a + b
for i in range(2, n):
    c = a + b
    print(c)
    sum += c
    a, b = b, c

average = sum / n
print("Average:", average)


#Ans 8
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")

#a
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
set_sym_dif=set1.symmetric_difference(set2)
print(set_sym_dif)

#b
print("\nQ.8(b)")
print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
set_u1=set1.union(set2)
set_uf=set_u1.union(set3)
set_i1=set1.intersection(set2)
set_if=set_i1.intersection(set3)
set_12=set1.intersection(set2)
set_23=set2.intersection(set3)
set_13=set1.intersection(set3)
set_f1=set_uf-set_12-set_23-set_13
print(set_f1)

#c
print("\nQ.8(c)")
set_c1=set_12.union(set_23)
set_c2=set_c1.union(set_13)
set_final=set_c2-set_if
print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:")
print(set_final)

#d
print("\nQ.8(d)")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1
#printing final set
print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:")
print(set_new)

#e
print("\nQ.8(e)")
set_e=set_d-set_uf
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.")
print(set_e)