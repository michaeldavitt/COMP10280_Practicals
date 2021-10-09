# 2018

# Q1: A: I - 8.0, II - 8.0, III - 4, IV - abcabcabcabcabc, V - True, VI - True
# B: Total is:  35
# C: 

# total = 0
# x = 0

# for x in range(0, 70, 7):
#     print(x)
#     if x % 5 == 0:
#         total += x

# print("Total is: ", total)

# total = 0
# x = 0

# while x < 70:
#     if x % 5 == 0:
#         total = total + x

#     x = x + 7

# print("Total is: ", total)

# Q2: A
# I - Definite Iteration is when the number of iterations of a program is known before the iterations begin (EG: in the case of while loops where the user has specified a limit)
# II - Augmented Assignment is when 
# III - Function - A piece of code that takes in arguments, does some operation to those arguments, then outputs some result
# IV - Two's complement - no idea
# V - Recursion - A function calls itself

# B: 
# I - 
# II - If, If/Else, If/Elif/Else
# III - The function is invoked, Python goes to where the function has been defined, executes the code in the function, then goes back to the main program
# IV - 
# V - The range function takes in a start, stop and step argument. It will then a sequence of numbers from start to (stop - step) in steps of step

# C:
# Errors: Things that will crash program
# 1: False needs to be capitalised
# 2: false used for finished (loop will never start)
# 3: No colon after finished
# 4: Type in variable numbers, so when you use numbers variable, you will get a name error
# 5: == used to assign variable to total
# 6: Count has not been defined at the start
# 7: The block of code following the IF statement has not been indented
# 8: Used =+ instead of +=
# 9: No brackets in the print statement
# 10: No comma in the print statement between string and variable
# 11: total is used before assignment


# Others
# 12: Integer division is used to find the average (should use floating point division to get an accurate average)
# 13: Count should be used in the final print statement instead of number
# 14: Should use If total + number >= 30 for the conditional to make sure that the total is always less than 30
# 15: Count should be initialised with 1 before the while loop starts


# finished = False
# total = 0
# number = 0
# count = 0
# while not finished:
#     total += number
#     count += 1
#     number += 3
#     print("Total =", total)
#     print("Average =", total / count)
#     if (total+number) >= 30:
#         finished = True
    
# print("Total was", total)
# print("There were", count, "numbers.")

# print(0 + 3 + 6 + 9)


################################################ 2018 Q3 - Datetime Program ######################################################
# import the datetime module

# Prompt the user for a day
# Make day an integer

# if the integer is greater than 0:
#     convert the number of days into day, month and year format

# import datetime

# num = int(input("Please type an integer: "))

# strt_date = datetime.date(1970, 1, 1)
# num_days = datetime.timedelta(num - 1)
# new_date = strt_date + num_days
# new_date_formatted = new_date.strftime("%d %B %Y")
# print("Day number", num, "is", new_date_formatted)


################################################ 2018 Q4 - Fibonacci Program ####################################################
"""
Fibonacci Program
Prompt user for an integer
If the integer <= 0 then:
    print "exiting

else:
    initialise f_1 = 1 and f_2 = 0
    if n = 1:
        print f_2
    else if n = 2:
        print f_2, f_1
    else:
        print f_2, f_1
        initialise position variable = 3
        while the position is less than or equal to n:
            sum f_1 and f_2 and print the result
            then change f(n-2) to f(n-1) and change f(n-1) to f(n-1) + f(n-2)
            increment position

terminate the program
"""

# def fibonacci(n):
#     if n <= 0:
#         print("Exiting")

#     else:
#         f_1 = 1
#         f_2 = 0

#         if n == 1:
#             print("Series: ", f_2, sep="", end="")

#         elif n == 2:
#             print("Series: ", f_2, ", ", f_1, sep="", end="")

#         else:
#             print("Series: ", f_2, ", ", f_1, sep="", end="")

#             position = 3

#             while position <= n:
#                 fib_num = f_1 + f_2
#                 print(", ", fib_num, sep="", end="")
#                 f_1, f_2 = fib_num, f_1
#                 position += 1
        
#         print()


# user_num = int(input("Please enter the number of terms (enter a non-positive integer to exit): "))

# fibonacci(user_num)

# user_str = input("Please enter a string: ")
# for i in range(1000):
#     print(user_str, "", end="")

# print()
# input("Press the enter key to exit")





############################# 2017 Q1 ###################################

# Q1: A: I: 3.5, II: 3.5, III: 3.5, IV: xyzxyzxyzxyz, V: True, VI: True
# B: "Total is: 45"

# total = 0
# x = 0

# for x in range(0, 33, 3):
#     if x % 5 == 0:
#         total += x

#     x += 3

# print("Total is ", total)

################################### 2017 Q2 ############################################


"""
Sum every third integer (0+3+6...) while the total is less than 40
Need to increment the number by 3 each time
Need to keep track of running total
Need an if statement to break us out of the loop when the total is greater than 40
Need a count variable to keep track of the number of iterations for the average

Set limit = 40
Set finished = False
Set count = 1
Set total = 0
Set number = 0

while the process is not finished:
    add the number to the running total
    print the total
    print the average (total divided by count)
    increment count by 1
    increment number by 3
    if the total for the next iteration is greater than or equal to the limit:
        set finished top True
"""

# limit = 40
# finished = False
# count = 1
# total = 0
# number = 0

# while not finished:
#     total += number
#     print("Total =", total)
#     print("Average =", total / count)
#     count += 1
#     number += 3
#     if total + number >= limit:
#         finished = True

# print("Final total =", total)
# print("There were", count - 1, "numbers")

# flagged errors: count is used before it has been initialised on line 6, no colon after finished on line 4, no indentation on line 8, number used before declared due to typo on line 5
# other errors: while loop will never begin because the value of the conditional expression is false initially
# the average will be inaccurate because you used integer division instead of floating point
# the total will be bigger than 40 because you don't exit the loop until after total has surpassed 40
# the running total will not be printed because you have neglected to include the print statement


################### 2017 Q3 - Revised Julian Calender ###############################
"""
Julian Leap Years:
Need to get a year from the user, check if it's a multiple of 4, then check if it's a multiple of 100, then check if it leaves a remainder of 200 or 600 when divided by 900

result = ""

if year % 4 != 0:
    result = "common"

else:
    if year % 100 == 0:
        if year % 900 == 200 or year % 600 == 0:
            result = "leap"

        else:
            result = "common"

    else:
        result = "leap"
"""

# year = int(input("Please enter a year: "))
# result = ""

# if year <= 0:
#     print("Error")

# else:
#     if year % 4 != 0:
#         print(year, "is a common year")

#     else:
#         if year % 100 == 0:
#             if year % 900 == 200 or year % 600 == 0:
#                 print(year, "is a leap year")

#             else:
#                 print(year, "is a common year")

#         else:
#             print(year, "is a leap year")


############################# 2017 Q4 - Permutation Program  ###################################################################

"""
Permutations program:
Need to get an n, check if the n is greater than or equal to 0, then get a k, then get the factorial of n and k, then divide these two results
factorial rules: fact = 1 if n = 0, fact = 1 if n = 1, fact = n * (n-1) * (n-2) ... * (1) if n > 1
for n > 1, start the position at 2, keep while loop going until the position is greater than n, then each iteration, multiply the total by the position, then increment position

Pseudocode: Factorial function

if n is 0 then:
    factorial is 1

else if n is 1 then:
    factorial is 1

else:
    initialise position = 2
    initialise total = 1
    while position is less than or equal to n:
        total = total * position
        increment position
    
"""

# def fact(n):
#     if n == 0 or n == 1:
#         fact = 1

#     else:
#         position = 2
#         fact = 1
#         while position <= n:
#             fact *= position
#             position += 1

#     return fact
        

# n = int(input("Enter number of items (enter a negative integer to exit): "))
# if n < 0:
#     print("Program Exiting")
# else:
#     k = int(input("Enter the number of possibilities: "))
#     n_fact = fact(n)
#     n_k_fact = fact(n-k)
#     print("Total number of permutations is:", int(n_fact / n_k_fact))



####################################### 2017 Q5 - Palindrome Program ################################################################

"""
Palindrome program:
want to get a string from the user, go through the string and check first if the first and last characters match, then the second and second last etc until the end

initialise a variable for passing/failing the test

for each letter in string:
    if the letter is not equal to the backwards version of the letter:
        the test is failed

return the pass/fail result
"""

# def palindrome(strng):
#     strng = strng.lower()
#     passed_test = True
#     for i in range(0, len(strng)):
#         if strng[i] != strng[len(strng) - i - 1]:
#             passed_test = False
#     return passed_test

# user_strng = input("Enter a string (enter an empty string to exit): ")
# while user_strng != "":

#     result = palindrome(user_strng)
    
#     if result:
#         print(user_strng, "is a palindrome")
#     else:
#         print(user_strng, "is not a palindrome")

#     user_strng = input("Enter a string (enter an empty string to exit): ")


# print("Program Exiting...")   