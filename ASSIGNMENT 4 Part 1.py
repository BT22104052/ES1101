#Ans 1
marks = int(input("Enter marks: "))

if marks > 80:
    letter_grade = "A"
   
elif 60<marks<=80:
    letter_grade = "B"

elif 50<marks<=60:
    letter_grade = "C"
    
elif 45<marks<=50:
    letter_grade = "D"
    
elif 25<marks<=45 : 
    letter_grade = "E"
else: 
    marks<=25 
    letter_grade = "F"
    
print("Your Marks is {}\n Grade {}".format(marks,letter_grade))


#Ans 2

year=int(input("Enter Year:"))
if year%4==0:
    print("Year {} is a leap year".format(year))
elif year%100==0:
    print("Year {} is not a leap year".format(year))
elif year%400==0:
    print("Year {} is  a leap year".format(year))
else:
    print("Year {} is not a leap year".format(year))

    
#Ans 3
import random
def play_game():
 q=int(input("No of Questions:"))
 for i in range(q):
    n1=random.randint(0,10)
    n2=random.randint(0,10)
    answer=n1*n2
    guess=int(input(f"Qus {i+1}: {n1}*{n2}="))
    if answer==guess:
        print("Right!")
    else: 
        print(f"Wrong! Correct answer is {answer}")
play_game()

#Ans 4
for i in range(200):
    if i%5!=2: 
     continue
    if i%6!=3: 
     continue
    if i%7!=2:
     continue
    print(int(i) , " is the answer!")   
    break

     
     
