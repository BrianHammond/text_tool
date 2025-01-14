from class_text import *
import os

menu = ("""
1. Write a new text file (will overwrite existing file)
2. Append
0. Exit  
""")

folder = input("folder: ")
file = input("file: ") + ".txt"

while True:
    print(menu)
    choice = int(input("Enter Choice: "))

    match choice:
        case 0 :
            break

        case 1:
            Folder(folder, file).check()
            Data(folder, file, "w").data()
        
        case 2:
            Data(folder, file, "a").data()

        case _:
            print ("pick a valid option")