def progressbaring(inTakeFiles, allFiles):
    theBar = ["[","_","_","_","_","_","_","_","_","_","_","]"]
    percent = inTakeFiles/allFiles * 100
    
    

    if percent <= 100 and percent >= 90:
        theBar[1] = "O"
    
    elif percent <= 90 and percent >= 80:
        for i in range(1, 2):
            theBar[i] = "O"
    
    elif percent <= 80 and percent >= 70:
        for i in range(1, 3):
            theBar[i] = "O"
    
    elif percent <= 70 and percent >= 60:
        for i in range(1, 4):
            theBar[i] = "O"
    
    elif percent <= 60 and percent >= 50:
        for i in range(1, 5):
            theBar[i] = "O"
    
    elif percent <= 50 and percent >= 40:
        for i in range(1, 6):
            theBar[i] = "O"

    elif percent <= 40 and percent >= 30:
        for i in range(1, 7):
            theBar[i] = "O"

    elif percent <= 30 and percent >= 20:
        for i in range(1, 8):
            theBar[i] = "O"

    elif percent <= 20 and percent >= 10:
        for i in range(1, 9):
            theBar[i] = "O"

    elif percent <= 10:
        for i in range(1, 10):
            theBar[i] = "O"

    leResult = ""
    for i in range(len(theBar)):
 
        leResult = leResult + theBar[i]

    print(leResult + " " + str(percent) + "%")    

