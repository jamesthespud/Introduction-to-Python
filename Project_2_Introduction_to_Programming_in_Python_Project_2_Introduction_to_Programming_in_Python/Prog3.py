#!/usr/bin/env python3

#passwordtry and usernametry tells the loop whether it should loop or not.

# 1 means loop. Anything else means it will not loop.
passwordtry = 1
usernametry = 1

#Password is Hello and it is case sensative, author name is  also case sensative.

correctpassword = "Hello"
programmername = "James Debnam"
print ("Program Author: James")
#print ("Student ID: xxxxxxx")
print ('Program 3 — Loops and if Conditions')
while passwordtry == 1:
    password = str(input("Please enter Password: "))
    if correctpassword == password:
        print ("")
        print ("")
        print("Welcome to the second half of the program")
    while usernametry == 1:
        username = str(input ("Please enter user name: "))
# When name is Cher or Madonna (case sensative), ask to show autograph, if it's author name, show what a great name, if it's any other input it will show that's a nice name
# program will end when author name is entered correctly, otherwise, it will keep looping to ask for a name.
        cher = "Cher"
        madonna = "Madonna"
        if username == programmername:
            usernametry = 0
            passwordtry = 0
            print ("What a great name!")
        elif username == cher:
            print ("May I have your autograph, please?")
        elif username == madonna:
            print ("May I have your autograph, please?")
        elif username != programmername:
             print (username,", That's a nice name")
