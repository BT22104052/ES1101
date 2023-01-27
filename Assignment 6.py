#ANS1
n = int(input("Enter any number: "))
x = 0
for i in range(1, n):
    if(n % i == 0):
        x = x + i
if (x == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

#ANS2

string= input ("Entermstring: ") 
def isPalindrome(string): 
 if (string == string[::-1]) : 
   return("The string is a palindrome.")
 else: 
    return "The string is not a palindrome." 

print(isPalindrome(string))


#ANS3
z=int(input("No. of Rows:"))
def pascal_triangle(n):
    for i in range(n):
        x = []
        for j in range(i+1):
            if j == 0 or j == i:
                x.append(1)
            else:
                x.append(y[j-1]+y[j])
        y = x
        print(x)
pascal_triangle(z)      

#ANS4
x=str(input("String:"))
def is_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    for char in alphabet:
        if char not in string:
            return False
    return True
print(is_pangram(x))

#ANS5
n=input("enter the string: ") 
l=n.split('-') 
l.sort() 
print('-'.join(l))


#ANS6
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    
    if 'student_class' in kwargs:
            print(f"Student Class: {kwargs['student_class']}")

 
student_data(student_id='221001', student_name='Rohan Doot',student_class ='X')

student_data(student_id='221002', student_name='Rahul Dilon', student_class ='X')


#ANS7
class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))


#ANS8
class SumToZero:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_elements(self):
        result = []
        numbers = self.numbers
        numbers.sort()
        for i in range(len(numbers)-2):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            l = i+1
            r = len(numbers)-1
            while l < r:
                if numbers[i] + numbers[l] + numbers[r] == 0:
                    result.append([numbers[i], numbers[l], numbers[r]])
                    while l < r and numbers[l] == numbers[l+1]:
                        l += 1
                    while l < r and numbers[r] == numbers[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif numbers[i] + numbers[l] + numbers[r] < 0:
                    l += 1
                else:
                    r -= 1
        return result

numbers =[1,-2,3,-4,5,-6,7,-8,9,-9,8,-7,6,-5,4,-3,2,-1,0]
sum_to_zero = SumToZero(numbers)
print(sum_to_zero.find_elements())




#ANS9
class BracketChecker:
    def __init__(self, string):
        self.string = string

    def is_valid(self):
        stack = []
        for char in self.string:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                current = stack.pop()
                if current == "(" and char != ")":
                    return False
                elif current == "[" and char != "]":
                    return False
                elif current == "{" and char != "}":
                    return False
        return not stack

x=str(input(""))
checker = BracketChecker(x)
print(checker.is_valid())
















  