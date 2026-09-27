"""
Module 2 — Activity: File Sorting with os and shutil
Student: Bugay, Jenny L.
Date: 09/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

For this activity, I just followed the instruction wherein I use the mkdir and dir to 
list the files. Although my code are not working, it only create the folder and it is
printed as it is. 


============================================
KEY VOCABULARY
============================================
- os module: It is a built-in library code and it is a low level system operation.
- shutil module: It provides a collection of high level operation on files and 
directories.  
- file path: Location of file and folder.
- directory: Organized list and files used to locate information.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# --- 
import os
import shutil

folder = ["images", "videos", "documents", "others"]

user = input("Put a folder path: ")

if os.path.exists(user):
    print("The folder is true! Proceed")

    file = os.listdir(user)
    images = 0,
    videos = 0,
    documents = 0,
    others = 0,

    print(file)

    images = os.mkdir()
    videos = os.mkdir()
    documents = os.mkdir()
    others = os.mkdir()

    for file in os.path.exists():
        


else:
    print("Error")
 ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

Since it is my first time using those code, I don't really have any idea on how they
work. 

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
