 import os
import pathlib
#organize all files by extension
file_extension_list = []
current_area = os.getcwd()
files = os.listdir()

#find every extension. if the extension already exists in the list then move to the next file until all files are iterated over
for i in files:
    file_extension = pathlib.Path(i).suffix[1:]
    if file_extension in file_extension_list:
        continue
    if file_extension == "":
        file_extension = "blank"
    file_extension_list += [file_extension]
#make a folder for every extension in the file extension list.
for extension in file_extension_list:
    folder_to_be_created_fullpath = os.path.join(current_area,extension)
    os.mkdir(folder_to_be_created_fullpath)
#move files according to extension
#get file name
for i in files:
    file_extension = pathlib.Path(i).suffix[1:]
    if not "." in i:
        file_extension = "blank"
    os.rename(os.path.join(current_area,i),os.path.join(current_area,file_extension,i))
#if file extension matches folder name move it there
