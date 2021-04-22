import os
import shutil
import random
import progressbar

def dumpProccess(directory, destination):
    destination = destination + "\\"
    directory = directory + "\\"

    allFilesTr = 0
    inTakeFilesTr = 0

    for root, folder, files in os.walk(str(directory)):  
        for filename in files:
             
            allFilesTr = allFilesTr + 1
            inTakeFilesTr = allFilesTr 
    for filename in files:
        print("Original: " + filename)
        origFilename = filename
        
        randPrefix = ""
        i = 0
        while i != 3:
            listRand = ["a", "b", "c", 'd', "ab", "bc", "cd", "aa", "bb", "cc", "dd"]
            pickRandLetter = str(listRand[random.randint(0,10)])
            randPrefix = randPrefix + str(random.randint(1,30)) + pickRandLetter
            i = i + 1
        filename = randPrefix + "_" + filename   
        print("Renamed: " + filename)
        os.rename(str(directory) + str(origFilename), str(directory) + filename)
        shutil.move(str(directory) + str(filename), str(destination) + filename)
        inTakeFilesTr = inTakeFilesTr - 1

        progressbar.progressbaring(inTakeFilesTr, allFilesTr)
