import os
path = './Sound-Data'

filestodel = "8"

for root, dirs, filenames in os.walk(path):
    print(root)
    for i in filenames:
        temp = i.split("-")
        if temp[0] != '.DS_Store':
            if temp[1] == filestodel:
                os.remove(str(root)+ "/" + str(i))
                print("removed: " + root + "/" + str(i))
