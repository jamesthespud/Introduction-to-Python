#!/usr/bin/env python3

#this program is degsined to calculate the perimeter and area of a rectangle.

print ("Program Author: James")
#print ("Student ID: xxxxxxx)
print ('PROGRAM 4 — FUNCTIONS')

#This variable tells the loop whether it should loop or not.

#1 means loop. anything else means don't loop
loop = 1

#this variable holds the user's choice in the menu:

Choice = 0
while loop == 1:
        #desplay the available options to the user
        print ("")
        print ("")
        print ("")
        print ("Welcome to Calculations Menu")

        print ("your options are: ")
        print ("")
        print ("1) AREA (SQUARE) ")
        print ("2) AREA (RECTANGLE) ")
        print ("3) AREA (CIRCLE) ")
        print ("4) PERIMETER (SQUARE) ")
        print ("5) PERIMETER (RECTANGLE) ")
        print ("6) PERIMETER (CIRCLE) ")
        print ("7) QUIT ")
        print ("")
#1) AREA (Square) 2)AREA (rectangle) 3) AREA (CIRCLE) 4) PERIMETER (Square) 5) PERIMETER (Rectangle) 6) PERIMETER (Circle)
        choice = int(input("choose your option (1,2,3,4,5,6 OR 7):"))
        if choice == 1:
                print ("You have chosen AREA (SQUARE)")
                bases = int(input ("base are : ") )
                print ("The Area is" , bases**2)
        elif choice == 2:
                print ("you have chosen AREA (RECTANGLE)")
                alength = int(input ("Input Length:"))
                awidth =int (input("Input Width: "))
                print ("The Area is", alength*awidth)
        elif choice == 3:
                print ("You have chosen AREA (CIRCLE)")
                aradius =int (input("Radius are: "))
                print ("The Area is", aradius**2*3.14)
        elif choice == 4:
                print ("You have chosen PERIMETER (SQUARE)")
                pbases= int(input("Base are: "))
                print ("The Perimeter is" , 4*pbases)
        elif choice == 5:
                print ("You have chosen PERIMETER (RECTANGLE)")
                plength =int(input("Input Length: "))
                pwidth =int (input("Input Width: "))
                print ("The Perimeter is" , (plength+pwidth)*2)
        elif choice == 6:
                print ("you have chosen PERIMETER (RECTANGLE)")
                pradius =int(input("Radius are:" ))
                print ("The Perimeter is", 2*3.14*pradius)
        elif choice == 7:
            loop =0
            print ("thankyou for using this program!")
