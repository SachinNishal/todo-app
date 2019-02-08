import sqlite3
import os


if os.path.isfile("./todo.db") is False:
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("CREATE TABLE todo(item varchar(100))")
    conn.commit()
else:
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()



print("----- Welcome to todo app ! -----")
keyPressed = input("   To add items    : press C \n   To view items   : press R \n\
   To edit items   : press U \n   To remove items : press D \n\
   --> : ")

if(keyPressed == "C" or keyPressed == "c"):
    thing = input("Enter a todo item : ")
    c.execute("INSERT INTO todo VALUES(?)", (thing,))
    conn.commit()
    conn.close()

elif (keyPressed == "R" or keyPressed == "r"):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT * FROM todo")
    all=c.fetchall()
    for _ in all:
        print(*_, sep="")
    conn.close()


elif (keyPressed == "U" or keyPressed == "u"):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    thing = input("Enter a current item : ")
    newthing = input("Enter a updated item : ")
    c.execute("UPDATE todo SET item = ? WHERE item= ?",(newthing,thing))
    conn.commit()
    conn.close()


elif (keyPressed == "D" or keyPressed == "d"):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    thing = input("Enter a current item to delete : ")
    c.execute("DELETE FROM todo WHERE item= ?",(thing,))
    conn.commit()
    conn.close()




else:
    print("Invalid entry, Try again !")




###todo- add error handling to avoid multiple items with same name,add error handling to U & D unavilable things