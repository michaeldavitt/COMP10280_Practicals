"""
Pseudo Code:
Prompt the user for a filename
Read in the file and store it in a variable
Create a list with all bracket types
Get the count of all brackets individually and store all counts in a list
For each bracket type:
    If the variables for the left and right bracket values are the same:
        Print the brackets are balanced

Else:
    Print that the file does have balanced brackets

Close the file
Terminate the program
"""

filename = input("Please enter the filename: ")
f = open(filename, "r")
s = f.read()
brackets = ["<", ">", "(", ")", "[", "]", "{", "}"]
bracket_counts = []
for i in brackets:
    bracket_counts.append(s.count(i))

for i in range(0, len(bracket_counts), 2):
    if bracket_counts[i] == bracket_counts[i + 1]:
        print(brackets[i] + " and " + brackets[i+1] + " are balanced (" + str(bracket_counts[i]) + " vs. " + str(bracket_counts[i+1]) + ") ")

    else:
        print(brackets[i] + " and " + brackets[i+1] + " are NOT balanced (" + str(bracket_counts[i]) + " vs. " + str(bracket_counts[i+1]) + ") ")

f.close()
print("Finished!")