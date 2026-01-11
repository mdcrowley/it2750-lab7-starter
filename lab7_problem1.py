# ==================================================
# IT 2750 - Scripting Fundamentals for Cybersecurity
# Cuyahoga Community College
# Lab 7 – Problem 1
# ==================================================
# Student Name: YOUR_NAME_HERE
# Student Email: YOUR_EMAIL_HERE
# ==================================================

import os  # DO NOT EDIT THIS LINE
from pathlib import Path  # DO NOT EDIT THIS LINE

def main():  # DO NOT EDIT THIS LINE

    print("Welcome to the File Forensics System!")

    # PART A
    # ======
    # Create a variable that will store the name of a folder. Ask the user what folder
    # they would like to look at: "What folder would you like to analyze?". Store 
    # the folder name in a variable folder_name. When running the program, you will
    # enter the name of the folder, lab7_data_problem1

    ## YOUR CODE HERE ##

    # PART B
    # ======
    # Convert the foldername to a path variable

    ## YOUR CODE HERE ##

    # PART C
    # ======
    # Create a list of all files in the folder and save to the variable file_list. Output
    # the number of files in the folder (only the number)

    ## YOUR CODE HERE ##

    # PART D
    # ======
    # You are attempting to find the word Batman in one of the files in the folder.
    # Iterate through each line of every file in the folder. For each file, indicate
    # whether or not you found Batman. If you found Batman in the file, output:
    #
    #     Did not find Batman in FILENAME
    #
    # Where FILENAME is the name of the file (including extension.) If you found
    # Batman in a file, output the following:
    #
    #     Found Batman! It was in FILENAME
    #
    # Replacing FILENAME, again, with the file name (including extenion). Only output
    # the lines as shown above; do not add additonal information

    ## YOUR CODE HERE ##

    return  # DO NOT EDIT THIS LINE

if __name__ == "__main__":  # DO NOT EDIT THIS LINE
    main()                  # DO NOT EDIT THIS LINE