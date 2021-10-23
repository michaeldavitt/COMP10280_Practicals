"""
Pseudo Code:
Prompt the user for a filename
If the filename does not exist then:
    Print an error message

Else:
    Read in the file and save it to a variable s
    Create 6 variables and assign each of them the value of s.count(string) with string being one of the six strings we are looking for.
    Close the file
        
    Create the file path for the file results.txt
    if this file exists then:
        Print an error message
        
    else:
        write the 6 variables above into the file one by one
        close the file

Terminate the program
"""
import os

webpage = input("Please enter your filename where you will read the results from: ")
if not os.path.isfile(webpage):
    print("Error, this file does not exist")

else:
    f = open(webpage, "r")
    s = f.read()
    angle_bracket_l = str(s.count("<")) 
    angle_bracket_r = str(s.count(">"))    
    newlines = str(s.count("\n"))
    low_e = str(s.count("e"))
    comment_l = str(s.count("<!--"))
    comment_r = str(s.count("-->"))

    f.close()

    filename = "Week 6\\Sheet 18\\results.txt"
    if os.path.isfile(filename):
        print("Error, this file already exists")

    else:
        fw = open(filename, "w")
        fw.write("<: " + angle_bracket_l + "\n")
        fw.write(">: " + angle_bracket_r + "\n")
        fw.write("\\n: " + newlines + "\n")
        fw.write("e: " + low_e + "\n")
        fw.write("<!--: " + comment_l + "\n")
        fw.write("-->: " + comment_r + "\n")

        fw.close()

print("Finished!")