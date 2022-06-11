
#Question1

m=int(input("enter marks"))
if(m<25):
    print(" Grade F")
elif(m>=25 and m<45):
    print(" Grade E")
elif(m>=45 and m<50):
    print(" Grade D")
elif(m>=50 and m<60):
    print(" Grade C")
elif(m>=60 and m<80):
    print(" Grade B")
elif(m>=80):   #else:
    print(" Grade A")





#Question2

year = int(input("Year = "))

if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
	print(year, " is a leap year")
else:
	print(year, " is not a leap year")