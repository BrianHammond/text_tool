# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#
# nothing special here

import os

folder_path = "files"
file_name = input("Enter the file name: ")+".txt"
full_path = folder_path+"/"+file_name

txt_data = input("Type whatever you want into the text file: ")

with open(full_path, "w") as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
    file.write(txt_data)
    print(f"text file {full_path} was created")

if os.path.exists(full_path): # returns a bool
    print(f"The location of {full_path} exists")
    if os.path.isfile(full_path): # checks if this is a file
        print("this is a file")
    elif os.path.isdir(full_path): # checks to see if this is a folder
        print("this is a folder")
else:
    print("can't find file")
