# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#
# nothing special here

import os

class Files:
    def __init__(self, folder, file):
        self.folder = folder
        self.file = file
        self.full_path = folder + "/" + file

class Data(Files):
    def __init__(self, folder, file, writing_mode):
        super().__init__(folder, file)
        self.writing_mode = writing_mode

    def data(self):
        txt_data = input("Type whatever you want into the text file: ")

        with open(self.full_path, self.writing_mode) as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
            file.write(txt_data+"\n")
            print(f"text file {self.full_path} was created")