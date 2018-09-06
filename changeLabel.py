# Changes the label for the specific sound files group
# i.e. filename-0-0-1.wav -> filename-1-0-1.wav if we want to change the sound category from 0 to 1

import os

# path = "C:/Users/Howard/Documents/learnAudio/Sound-Data/renameThese/Ambient_1_18"
path = "C:/Users/Howard/Documents/learnAudio/TalkingData/set2"
labelToRename = 0
renameLabelTo = 3
for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        if filename != ".DS_STORE":
            temp = filename.split(".")

            getLabelCat = temp[0].split("-")
            if (int(getLabelCat[1]) == labelToRename):

                newName = str(getLabelCat[0] + "-" + str(renameLabelTo) + "-" + getLabelCat[2] + "-" + getLabelCat[3] + "." + temp[1])

                toRename = str(root+"/"+newName)
                originalFile = str(root+"/"+filename)

                os.rename(originalFile,toRename)
                print(toRename)
                print(originalFile)
