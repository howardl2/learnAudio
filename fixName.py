import os

path = "./New-Data/AmbientRecordings"
count = 0
for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        if filename != ".DS_STORE":
            temp = filename.split(".")
            print(temp)
            index = temp[1].find('wav')
            print(index)
            newName = str(temp[1][:index] + "."+temp[1][index:])
            print(newName)
            originalFile = str(root+"/"+filename)
            os.rename(originalFile,newName)
