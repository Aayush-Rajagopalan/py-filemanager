import os
import shutil

source = input("Enter the source directory (example: C:/Users/admin/Downloads): ")
#Downloads Folder

#make a new folder
directory = input('Enter the directory You want the files to move to: ')

#list file extension for the file to move to
ending = input('Enter the file extension: ')
sourcefiles = os.listdir(source)

path = os.path.join(source, directory)


os.mkdir(path)
print("Directory Created")

for file in sourcefiles:
    if file.endswith(ending) :
        shutil.move(os.path.join(source,file), os.path.join(path,file))


print("Files Moved")