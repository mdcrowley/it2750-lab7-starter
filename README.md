# IT 2750 - Scripting Fundamentals for Cybersecurity
## Lab 7 - Exploring File Forensics

### 🗒  Description
This repository contains the Python script for Lab 7 of the course IT 2750 - Scripting Fundamentals for Cybersecurity. There is one problem in this lab.

This lab focuses on a unique task of proving an association between Bruce Wayne and Batman through file analysis. This singular problem in the lab engages students in a forensic investigation by analyzing the contents of a specified folder. The script prompts users to input the name of a folder, converts it to a path variable, and then enumerates all files within this folder, displaying the total file count. The main challenge is to perform a thorough search across all files to find instances of the word "Batman." For each file, the script reports whether the keyword was located or not. This exercise offers a hands-on experience in basic file forensics, teaching students how to explore folder contents and conduct keyword searches within files, a fundamental skill in the realm of digital forensics and cybersecurity.

#### Problem 1 - Finding Batman as a Forensic Investigator
Problem 1 allows users to analyze the contents of a specified folder. In this scenario, you received a set of files from Bruce Wayne, and it is your job to use forensics to prove that he is, at the very least, associated with Batman. To do so, you will see if the word "Batman" is contained within a set of files. The script begins by prompting the user for the name of the folder they want to examine. Upon receiving the folder name, it converts it to a path variable. The script then lists all the files in the selected folder and outputs the total number of files within it. Lastly, it conducts a search operation across all files within the folder, aiming to locate instances of the word "Batman." For each file, the script indicates whether "Batman" was found or not. Essentially, this script provides a straightforward yet practical tool for exploring folder contents and conducting keyword searches within files, making it useful for basic file forensics tasks.

### 📝  Requirements
This lab requires you to write code that adheres to the following requirements:

#### Problem 1
In Problem 1, you will edit the script template to perform the following tasks:

- Part A: The script asks the user for the name of a folder they would like to analyze and stores it in a variable called `folder_name`. By default, you should enter the name of the folder, `lab7_data_problem1`, when running the program.
- Part B: It converts the `folder_name` to a `path` variable.
- Part C: The script creates a list of all files in the folder and outputs the number of files in the folder.
- Part D: It searches for the word "Batman" in each line of every file in the folder and outputs whether "Batman" was found or not for each file.

#### Additional Requirements
In order to receive credit for this lab, you must replace `YOUR_NAME_HERE` with your name and `YOUR_EMAIL_HERE` with your Tri-C email address in the code file headers for all script files in the template. Students who do not perform this action will receive a zero score.

### 🚀  Usage
To run the script, execute the script file with Python. Each part of the lab problem is commented, and you should replace the placeholder text with your own information. From the code directory of this lab, you can run the various problems using the following commands:

- Problem 1: `python lab7_problem1.py`

### 🎯  Testing
The problems in this lab are tested using code that can be found in the corresponding `tests_*.py` file for each problem. You can use these tests to check if your code runs properly and to specifications. You can run these tests on your local machine by setting your working directory to the problem folder and running `pytest` with the `tests_*.py` file for the problem. From the code directory of this lab, you can run tests using the following commands:

- Problem 1: `pytest tests_lab7_problem1.py`

### 🏆  Grading
This lab is worth 40 points in total using the following breakdown by problem:

- Problem 1 is worth 40 points

You are awarded these points if all assertions in the test file pass successfully for a problem. There is no partial credit for lab problems.

### 💻  Academic Integrity and Copyright
This lab was created by the course professor (Matthew Crowley) and he asserts copyright over all material. You are not permitted to share the labs, tests, or solutions with anyone without express written consent. Breaches of this assertion may result in both academic and legal sanctions.