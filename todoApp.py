import sqlite3
import os


if os.path.isfile("./todo.db") is False:  # Check if the db already exists.
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()  # Open a DB connection
    c.execute("CREATE TABLE todo(item varchar(100) PRIMARY KEY)") # Create a table.
else:
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()


print("----- Welcome to todo app ! -----")
keyPressed = input("   To add items    : press C \n   To view items   : press R \n\
   To edit items   : press U \n   To remove items : press D \n\
   --> : ")

if(keyPressed == "C" or keyPressed == "c"):
    try:
        newItem = input("Enter a todo item : ")  # code to add new item
        c.execute("INSERT INTO todo VALUES(?) ", (newItem,))
    except sqlite3.IntegrityError:
        print("Item already exists ! ")

elif (keyPressed == "R" or keyPressed == "r"):
    c.execute("SELECT * FROM todo")  # code to select items
    allRows = c.fetchall()
    for _ in allRows:
        print(*_, sep="")

elif (keyPressed == "U" or keyPressed == "u"):
    existingItem = input("Enter a current item : ")  # code to update item
    newItem = input("Enter an updated item : ")
    c.execute("UPDATE todo SET item = ? WHERE item= ?",
              (newItem, existingItem))


elif (keyPressed == "D" or keyPressed == "d"):  # code to delete item
    existingItem = input("Enter a current item to delete : ")
    c.execute("DELETE FROM todo WHERE item= ?", (existingItem,))

else:
    print("Invalid entry, Try again !") # Exception handling.

conn.commit()  # Save & Close DB connection
conn.close()
