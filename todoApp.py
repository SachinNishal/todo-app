import sqlite3

print("----- Welcome to todo app ! -----")
keyPressed = input("   To add items    : press C \n   To view items   : press R \n\
   To edit items   : press U \n   To remove items : press D \n\
   --> : ")

if(keyPressed == "C" or keyPressed == "c"):
    print("C")
elif (keyPressed == "R" or keyPressed == "r"):
    print("R")
elif (keyPressed == "U" or keyPressed == "u"):
    print("U")
elif (keyPressed == "D" or keyPressed == "d"):
    print("D")
else:
    print("Invalid entry, Try again !")
