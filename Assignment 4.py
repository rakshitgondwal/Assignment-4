#Question 1
Marks=int(input("Enter your Marks: "))
if Marks<25:
    print("Your Grade is F")
elif Marks>=25 and Marks<45:
    print("Your Grade is E")
elif Marks>=45 and Marks<50:
    print("Your Grade is D")
elif Marks>=50 and Marks<60:
    print("Your Grade is C")
elif Marks>=60 and Marks<80:
    print("Your Grade is B")
else:
    print("Your Grade is A")

#Question 2
Year=int(input("Enter the Year:"))
if Year%4==0:
   if Year%100==0:
    print("This year is a leap year")
   else:
        if Year%400==0:
          print("This year is a leap year")
        
else :        
    print("This year is not a leap year")

#Question 3
import random
for i in range(1,11,1):
    m=random.randrange(1,10,1)
    n=random.randrange(1,10,1)
    ans=int(input((f"Question {i}: {m}*{n} = ")))
    if m*n==ans:
        print("Right!")
        continue
    else:
        print("Wrong. The answer is ",m*n)
        continue

#Question 4
for i in range(200):
    if i%5==2:
        if i%6==3:
            if i%7==2:
                print(i)

