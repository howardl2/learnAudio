import os

path = "./TalkingData/fold1"
count = 0
for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        if filename != ".DS_STORE":
            temp = filename.split(".")
            print(temp)
            index = temp[1].find('wav')
            newName = str(temp[1][:index] + "."+temp[1][index:])
            print(filename, newName)
            originalFile = str(root+"/"+filename)
            # os.rename(originalFile,newName)
