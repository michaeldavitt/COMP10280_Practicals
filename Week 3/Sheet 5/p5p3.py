# p5p3 - Program checks whether a number is positive, negative or equal to zero

user_num = float(input("Please type an integer: "))

if user_num > 0:
    print(user_num, "is positive")

elif user_num == 0:
    print(user_num, "is zero")

else:
    print(user_num, "is negative")

print("Finished")
