import os

# path = "C:/Users/Howard/Documents/learnAudio/Sound-Data/renameThese/Ambient_1_18"
path = "C:/Users/Howard/Documents/learnAudio/TalkingData/fold1"
count = 0
categoryName = "talking"
for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        if filename != ".DS_STORE":
            temp = filename.split(".")
            newName = str(categoryName + "_" + temp[0] + "-0-0-" + str(count) + "." + temp[1])
            # if "restroom" in temp[0] or "bathroom" in temp[0] or "toilet" in temp[0]:
            #     newName = str(temp[0] + "-0-0-" + str(count) + "." + temp[1])
            # else:
            #     newName = str(temp[0] + "-1-0-" + str(count)+"." + temp[1])

            toRename = str(root+"/"+newName)
            originalFile = str(root+"/"+filename)

            # os.rename(originalFile,toRename)
            print(toRename)
            print(originalFile)
            count += 1
#153954
#driving 161037 -> 161618
#walking
