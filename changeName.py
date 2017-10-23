import os

path = "./New-Data/fold2"
count = 0
for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        if filename != ".DS_STORE":
            temp = filename.split(".")
            print(temp)
            newName = str(temp[0] + "-3-0-" + str(count) + temp[1])

            toRename = str(root+"/"+"."+newName)
            originalFile = str(root+"/"+filename)

            os.rename(originalFile,toRename)
            count += 1
