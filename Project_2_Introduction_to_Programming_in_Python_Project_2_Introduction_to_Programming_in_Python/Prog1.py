#!/usr/bin/env python3

#Here I'm setting up defining my functions and the parameters through which we pass values to a function and solve some math.

def adding_two_parameters(item_one, item_two):
 return item_one + item_two
def substracts_two_parameters(item_one, item_two):
 return item_one - item_two
def multiplies_two_parameters(item_one, item_two):
 return item_one * item_two
def divides_two_parameters(item_one, item_two):
 return item_one / item_two
def exponetof_two_parameters(item_one, item_two):
 return item_one ** item_two
def remainderof_two_parameters(item_one, item_two):
 return item_one % item_two

#Displaying author and program information
print("Program Author: James")
#print("Student ID: xxxxxx")
print("Program 1 - Math Functions")

#here I am setting variables for when I run functions below
w = 2
x = 4
y = 3
z = 5
print("")

#declaring W, X,  Y and Z
print("If the value of w is:", w)
print("If the value of x is:", x)
print("If the value of y is:", y)
print("And if the value of z is:", z)
print("")

#ADDITION
print("A calculation (w + w) will result in:")
print(adding_two_parameters(w, w))
print("")

#SUBTRACTION
print("A calculation (x - w) will result in:")
print(substracts_two_parameters(x, w))
print("")

#MULTIPLICATION
print("A calculation (x * w) multiples to")
print(multiplies_two_parameters(x, w))
print("")

#DIVISION
print("A calculation (x / w) will result in:")
print(divides_two_parameters(x, w))
print("")

#EXPONENTNT
print("A Calculatoion of w to the Power of y will result in")
print(exponetof_two_parameters(w, y))
print("")

#REMANINDER
print("The remainder of (z % w) will result in:")
print(remainderof_two_parameters(z, w))
print("")
