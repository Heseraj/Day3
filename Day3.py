# conditional statement

# print("Welcome to the roller coster!")
#
# height = int(input("What is your height? \n"))
#
# if height > 120:
#     print("your can ride the roller coster")
# else:
#     print("sorry. You have to grow taller, before you can ride")

#
# yrNumber = int(input("type a number"))
# if yrNumber/2 == 0:
#     print("the number is even \n")
# else:
#     print("the number is odd")

## Ticket charging
#
# height = int(input("What is your height? \n"))
#
# if height >= 120:
#     age = int(input("How old are you? \n"))
#     if age >= 18:
#         print("you will be charged $12")
#     elif age >= 12:
#         print("you will be charged 7$")
#     else:
#         print("you will be charged $5")
# else:
#     print("sorry, you must grow taller to be able to ride")
#

# BMI 2.0

# height = float(input("What is your height? \n"))/100
# weight = int(input("What is your weight? \n"))
# yrBMI = weight / (height**2)
# yrBMI = round(yrBMI, 2)
# print(yrBMI)
#
# if yrBMI <= 18.5:
#     print(f"your bmi is {yrBMI} and your are underweight")
# elif yrBMI <= 25:
#     print("normal weight")
# elif yrBMI <= 30:
#     print("overweight")
# elif yrBMI <= 35:
#     print("obese")
# else:
#     print("clinically obese")

# year = int(input("what year do you have in mind? \n"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"the year {year} is a leap year")
#         else:
#             print(f"the year {year} is not a leap year.")
#     else:
#         print(f"the year {year} is a leap year")
# else:
#     print(f"the year {year} is not a leap year.")

## Ticket charging with photo

height = int(input("What is your height? \n"))
bill = 0

if height >= 120:
    age = int(input("How old are you? \n"))
    if age >= 18:
        bill = 12
        print(f"you bill is ${bill}")
    elif age >= 12:
        bill = 7
        print(f"you bill is ${bill}")
    else:
        bill = 5
        print(f"you bill is ${bill}")
    wants_photos = input("Would you like your photos taken? Yes or No? ")
    wants_photos = wants_photos.lower()
    if wants_photos == "yes":
        #now need to check the age
        #whatever it is the bill doesn't work. 
        bill = bill + 3
    print(f"therefore you will be charged ${bill}")

else:
    print("sorry, you must grow taller to be able to ride")
