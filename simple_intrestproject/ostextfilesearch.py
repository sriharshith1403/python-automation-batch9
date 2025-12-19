import os
#Allows Python to interact with the operating system (files & folders)

def find_txt_files(start_path): 
#after defines function
# "start_path" is the folder from where searching will begin

    for root, dirs, files in os.walk(start_path):
#os.walk() recursively walks through all folders and subfolders.Recursion means a function calling itself to solve a problem step by step.
#root- ->current folder path
#dirs--> list of subfolders.
#files--> list of files in the folder
        for file in files:
#Take one file name at a time from the list called files and work with it.
            if file.endswith(".txt"):
#check if the file name ends with .txt
                full_path = os.path.join(root, file)
#Joins folder path (root) and file name. Creates the complete file path
                print(full_path)

path = input("Enter directory path: ")

if os.path.exists(path):
    find_txt_files(path)
else:
    print("Invalid directory path")
