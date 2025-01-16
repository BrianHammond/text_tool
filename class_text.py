# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#
# nothing special here

class Misc:
    def __init__(self, txt_folder, txt_file):
        self.txt_folder = txt_folder
        self.txt_file = txt_file
        self.txt_full_path = txt_folder + "/" + txt_file

class Data_Input(Misc):
    def __init__(self, txt_folder, txt_file, writing_mode):
        super().__init__(txt_folder, txt_file)
        self.writing_mode = writing_mode

    def data_write(self):
        txt_data = input("Type whatever you want into the text file: ")

        with open(self.txt_full_path, self.writing_mode) as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
            file.write(txt_data+"\n")
            print(f"text file {self.txt_full_path} was created")

    def data_read(self):
        file_path = self.txt_full_path

        with open(file_path, self.writing_mode) as file:
            content = file.read()
            print(content)