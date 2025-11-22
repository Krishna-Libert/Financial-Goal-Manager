# **Financial Goal Manager**

#### 📖 Overview of the Project

###### 

###### The Financial Goal Manager is a lightweight, Command-Line Interface (CLI) application designed to help users track their personal finances, manage expenses, and monitor progress toward specific savings goals.

###### 

###### What makes this project unique is its "from-scratch" technical implementation. It avoids standard convenience methods (like json or csv libraries) and built-in string functions (like .strip() or .split()). Instead, it relies on custom-built algorithms for string parsing, file handling, and data validation. This project demonstrates a deep understanding of core Python logic, data structures, and algorithmic thinking.



#### ✨ Features

###### 

###### Goal Setting: Define a custom financial goal (e.g., "New Laptop") with a target amount and monthly income.

###### 

###### Expense Tracking: Log monthly expenses across fixed categories: Rent, Food, Transport, Fun, Bills, and Other.

###### 

###### Automated Analysis:

###### 

###### Calculates total monthly spending.

###### 

###### Computes net savings and savings rate (%).

###### 

###### Estimates the number of months required to reach the target goal.

###### 

###### Data Persistence: Automatically saves and loads data using a custom text-based file format (finance\_data.txt), allowing users to close the program and resume later.

###### 

###### Robust Input Validation: Ensures users enter valid positive numbers and handles text input errors gracefully without program crashes.

###### 

###### Custom String Engine: Uses manual logic to clean and parse text data, ensuring the program runs without external dependencies.



#### 🛠 Technologies \& Tools Used



###### Language: Python 3.x

###### 

###### Core Concepts:

###### 

###### File I/O (Read/Write/Append modes)

###### 

###### String Manipulation (Slicing, Indexing)

###### 

###### Control Flow (while loops, for loops, if/else logic)

###### 

###### Data Structures (Dictionaries, Lists)

###### 

###### Constraints Applied:

###### 

###### No Imports: No os, json, csv, or time modules used.

###### 

###### No Exception Handling: No try/except blocks; logic handles errors proactively.

###### 

###### No High-Level String Methods: No .strip() or .split() used; replaced with custom helper functions.

###### ⚙️ Steps to Install \& Run

###### Since this project relies entirely on core Python, there are no external packages to install.

###### 

###### Prerequisites: Ensure you have Python installed on your system. You can check this by typing python --version in your terminal.

###### 

###### Download: Save the project code into a file named finance\_manager.py.

###### 

###### Run the Application: Open your terminal or command prompt, navigate to the folder containing the file, and run:

###### 

###### Bash

###### 

###### python finance\_manager.py



#### 🧪 Instructions for Testing



###### Follow this workflow to verify the application works as expected:

###### 

###### Launch the App: Run the script. You should see the "FINANCE TRACKER" menu.

###### 

###### Setup a Goal (Option 1):

###### 

###### Select Option 1.

###### 

###### Enter Goal Name: Vacation.

###### 

###### Enter Target Amount: 5000.

###### 

###### Enter Monthly Income: 3000.

###### 

###### Add Expenses (Option 2):

###### 

###### Select Option 2.

###### 

###### Enter Date: 2023-11-01.

###### 

###### Enter amounts for categories (e.g., Rent: 1000, Food: 500, others: 0).

###### 

###### View Report (Option 3):

###### 

###### Select Option 3.

###### 

###### Verify the math:

###### 

###### Total Spent should be 1500.

###### 

###### Net Savings should be 1500 (3000 - 1500).

###### 

###### Time Left should be calculated based on remaining amount needed.

###### 

###### Test Persistence (Option 4):

###### 

###### Select Option 4 to Save \& Exit.

###### 

###### Check your folder for a new file named finance\_data.txt.

###### 

###### Run the program again; verify that your goal and expenses are still loaded.



### 📸 Screenshots (Mockups)

Main Menu Interface:



Plaintext



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

&nbsp;           FINANCE TRACKER

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

&nbsp;1. Setup Goal

&nbsp;2. Add Expenses

&nbsp;3. View Report

&nbsp;4. Save \& Exit



&nbsp;Select (1-4): 

Analytics Report:



Plaintext



==============================

&nbsp;        MONEY REPORT

==============================

&nbsp;Goal:         Vacation

&nbsp;Target:       5000.0

------------------------------

&nbsp;Spent:        1500.0

&nbsp;Saved (New):  1500.0

&nbsp;Saved (%):    50.00%

------------------------------

&nbsp;Total Saved:  1500.0

&nbsp;Time Left:    2 months

==============================

