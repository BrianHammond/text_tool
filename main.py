from class_text import *
import os

menu = ("""
1. Write a new text file (will overwrite existing file)
2. Append
3. Read
0. Exit  
""")

txt_folder = input("folder: ")
txt_file = input("file: ") + ".txt"
txt_full_path = txt_folder + "/"+ txt_file

while True:
    print(menu)
    choice = int(input("Enter Choice: "))

    match choice:
        case 0 :
            break

        case 1:
            if not os.path.isdir(txt_folder):
                print(f"{txt_folder} not found, creating folder")
                os.makedirs(txt_folder)
                Data_Input(txt_folder, txt_file, "w").data_write()
        
        case 2:
            if os.path.exists(txt_full_path):
                Data_Input(txt_folder, txt_file, "a").data_write()
            else:
                print(f"{txt_full_path} not found, please check or write a new file")

        case 3:
            if os.path.exists(txt_full_path):
                Data_Input(txt_folder, txt_file, "r").data_read()
            else:
                print(f"{txt_full_path} not found, please check")

        case _:
            print ("pick a valid option")