"""
Pseudo Code:
Prompt the user for a string input "str"
Read str

Initialise a cat and a dog counter
for i in the range 0 to (length of str - 3) do:
    if str[i:i+3] == "cat" then:
        increment cat counter
    
    else if str[i:i+3] == "dog" then:
        increment dog counter

if cat counter is equal to dog counter then:
    print that the words cat and dog both appear the same number of times
    print out how frequently the words appear in the string

else:
    print that the words cat and dog do not appear the same number of times

Terminate the program
"""

user_string = input("Please type a string: ")
print("You have entered:", user_string)

cat_count, dog_count = 0, 0

for i in range(0, len(user_string) - 2):
    string_slice = user_string[i:i+3]
    if string_slice == "cat":
        cat_count += 1

    elif string_slice == "dog":
        dog_count += 1

if cat_count == dog_count:
    print("The words \"cat\" and \"dog\" both appear the same number of times in the string:", user_string)
    print("They both appear", cat_count, "number of times")

else:
    print("The words \"cat\" and \"dog\" do not appear the same number of times in the string:", user_string)

print("Finished!")