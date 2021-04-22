import sys
import dump

# Taking the directions
def takeFrom():
    dir1 = open("dir1.ini", "r")
    dir1Text = dir1.readline()
    dir1.close()
    return dir1Text
def takeTo():
    dir2 = open("dir2.ini", "r")
    dir2Text = dir2.readline()
    dir2.close()
    return dir2Text

print ("Welcome to Zeno's Transfer Utility! Type the number of an option you want to pick.")
print ("Be sure you've typed the right directions here(also, no backslashes in the end)")

chooseParam = 0

while chooseParam == 0:
    print ("From: " + str(takeFrom()))
    print ("To: " + str(takeTo()))
    print (" 1. Start dumping\n 2. Change the from directory\n 3. Change the to directory\n 4. Why no backslashes?(a.k.a. Help)\n 5. Exit")

    try:
        duraduma = 0
        duraduma = int(input())

        if duraduma == 1:
            dump.dumpProccess(takeFrom(), takeTo())
            print("Done!")

        elif duraduma == 2:
            print("Type the start position without backslash in the end: ")
            bruh = str(input())
            dir1 = open("dir1.ini", "w")
            dir1Text = dir1.write(bruh)
            dir1.close()
        elif duraduma == 3:
            print("Type the end position without backslash in the end: ")
            bruh = str(input())
            dir2 = open("dir2.ini", "w")
            dir2Text = dir2.write(bruh)
            dir2.close()
        elif duraduma == 4:
            print("Because I don't know how to separate with-backslash and without-backslash directories.\nP.S. i'm b4d @ english hell ye, sry\nAlso no folder in the start directory, this can cause a crash(fix soon)")    
        elif duraduma == 5:
            sys.exit()
            
        else:
            print('Wrong number!')    

    except ValueError:
        print("That's not even an int value!")
        duraduma = 0
    
    