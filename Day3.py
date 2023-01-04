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

# for the photo charge
#
# height = int(input("What is your height? \n"))
# bill = 0
#
# if height >= 120:
#     age = int(input("How old are you? \n"))
#     if age >= 18:
#         bill = 12
#         print(f"you bill is ${bill}")
#     elif age >= 12:
#         bill = 7
#         print(f"you bill is ${bill}")
#     else:
#         bill = 5
#         print(f"you bill is ${bill}")
#     wants_photos = input("Would you like your photos taken? Yes or No? ")
#     wants_photos = wants_photos.lower()
#     if wants_photos == "yes":
#         bill += 3
#         #now need to check the age
#     print(f"therefore you will be charged ${bill}")
#
# else:
#     print("sorry, you must grow taller to be able to ride")




## Ticket charging with photo

#
# print("welcome to pizaa delieveries!")
# size = input("what size pizza do you like? s m l? \n").lower()
# add_pepperorni = input("do you like to add peperoni as toppings? yes or no \n").lower()
# extra_cheese = input("do you like extra cheese? yes or no \n")
# bill = 0
# if size == "l":
#     bill += 25
#     if add_pepperorni == "yes":
#         bill += 3
#     else:
#         bill = 25
#     if extra_cheese == "yes":
#         bill += 1
#     else:
#         bill = 25
#
#     print(f"your final bill will be {bill}")
#
# elif size == "m":
#     bill += 20
#     if add_pepperorni == "yes":
#         bill += 3
#     else:
#         bill = 20
#     if extra_cheese == "yes":
#         bill += 1
#     else:
#         bill = 20
#     print(f"your final bill will be {bill}")
# else:
#     bill += 15
#     if add_pepperorni == "yes":
#         bill += 2
#     else:
#         bill = 15
#     if extra_cheese == "yes":
#         bill += 1
#     else:
#         bill = 15
#
#     print(f"your final bill will be {bill}")
#
# print("thank you very much for your business!")

#
#
# height = int(input("What is your height? \n"))
# bill = 0
#
# if height >= 120:
#     age = int(input("How old are you? \n"))
#     if 55 >= age >= 45:
#         print("your bill is free!")
#     else:
#         if age > 55 or age >= 18:
#             bill = 12
#             print(f"you bill is ${bill}")
#         elif 12 >= age > 5:
#             bill = 7
#             print(f"you bill is ${bill}")
#         else:
#             bill = 5
#             print(f"you bill is ${bill}")
#         wants_photos = input("Would you like your photos taken? Yes or No? ")
#         wants_photos = wants_photos.lower()
#         if wants_photos == "yes":
#             #now need to check the age
#             #whatever it is the bill doesn't work.
#             bill = bill + 3
#         print(f"therefore you will be charged ${bill}")
#
# else:
#     print("sorry, you must grow taller to be able to ride")
#
# pOne_name = input("what is your name? \n").lower()
# pTwo_name = input("what is your name? \n").lower()
#
# pair_name = pOne_name + pTwo_name
#
# print(pair_name)
# t_occureance = pair_name.count("t")
# r_occureance = pair_name.count("r")
# u_occureance = pair_name.count("u")
# e_occureance = pair_name.count("i")
# total_true = t_occureance + r_occureance + u_occureance + e_occureance
# print(f"accurance of True {t_occureance} + {r_occureance} + {u_occureance} + {e_occureance} and therefore the total is {total_true}")
#
# l_occureance = pair_name.count("l")
# o_occureance = pair_name.count("o")
# v_occureance = pair_name.count("v")
# total_love = l_occureance + o_occureance + v_occureance
#
# print(f"accurance of lov {l_occureance} + {o_occureance} + {v_occureance} and therefore total lov {total_love}")
#
# love_score = str(total_true) + str(total_love)
# print(f"your love score is {love_score}")

# I may come back for the final challenge some later time.

print("welcome ")
print("welcome corso")
input(f"you are in a croos {left}"" or "right "choose.")