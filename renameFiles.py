import os

# path = './Sound-Data'
path = "C:/Users/Howard/Documents/learnAudio/Sound-Data/"
numberTracker = []
# INDEXTODEL = 0

oldMissing = []
thresh = 0


def renameFiles(INDEXTODEL):
    for root, dirs, filenames in os.walk(path):
        for i in filenames:
            temp = i.split("-")
            if temp[0] != '.DS_Store':
                if temp[1] not in numberTracker:
                    numberTracker.append(temp[1])

    missingNumbers = []
    for i in range(10):
        if str(i) not in numberTracker:
            missingNumbers.append(i)



    for root, dirs, filenames in os.walk(path):
        for i in filenames:
            temp = i.split("-")
            if temp[0] != '.DS_Store':
                # os.rename(str(root+"/"+i),str(root+"/"+"0192021.wav"))
                # break;
                if int(temp[1]) == (missingNumbers[INDEXTODEL]+1):

                    toRename = str(root+"/"+temp[0]+"-"+str(missingNumbers[INDEXTODEL])+"-"+"-".join(temp[2:]))
                    originalFile = str(root+"/"+i)
                    print("Original: " + originalFile)
                    print("New: " + toRename)
                    os.rename(originalFile,toRename)
    return(missingNumbers)

print(renameFiles(0))
# runningCount = 0
# while True:
#     print(thresh)
#     runningCount += 1
#     newMissing = renameFiles(INDEXTODEL)
#     if newMissing == oldMissing and runningCount > 3:
#         INDEXTODEL += 1
#         runningCount = 0
#         if INDEXTODEL >len(newMissing):
#             INDEXTODEL -= 2
#             thresh += 1
#     if thresh == 5:
#         break
