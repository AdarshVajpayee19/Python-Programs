# Oh Soldier Prettify my Folder

# Path,dictionary file, format

# this,that,normal
import os

def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

soldier(r"C:\Users\vajpa\PycharmProjects\PythonOopsPrograms\Testing", r"C:\Users\vajpa\PycharmProjects\PythonOopsPrograms\Testing\requirements.txt", ".jpg")

# Output can be seen in : Testing Folder
