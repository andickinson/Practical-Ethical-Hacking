#!/bin/python3

# Variables and Methods
quote = "All is fair in love and war."
print(quote.upper()) # uppercase
print(quote.lower()) # lowercase
print(quote.title()) # title case

print(len(quote)) # string length

name = "Andrew" # String
age = 32 # int int(32)
GPA = 3.8 # float float(3.8)

print(int(age))
print(int(30.9))

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')
# Functions
print("Here is an example function:")

def who_am_i(): # this is a function
    name = "Andrew"
    age = "32"
    print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

# adding parameters
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

# multiple parameters
def add(x, y):
    print(x + y)

add(7, 7)

def multiply(x, y):
    return x * y

print(multiply(7, 7))

def square_root(x):
    print(x ** 0.5)

square_root(64)

def nl():
    print('\n')

nl()

# Boolean expressions
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))