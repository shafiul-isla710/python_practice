course = 'python programming language' #This is a python programming language. will will learn python string methods and apply them in our code.

print(course.upper())  # Convert to uppercase
print(course.lower())  # Convert to lowercase
print(course.title())  # Convert to title case

print(course.find('lan'))  # Find substring
print(course.replace('python', 'JavaScript'))  # Replace substring

print('programming' in course)  # Check substring presence it return boolean value as like as True or False
print('java' in course)  # Check substring presence it return boolean value as like as True or False


#string operations

first = 'John'
last = 'Doe'
full_name = first + ' ' + last  # Concatenation
print(full_name)

#string concatenation another way
full_name2 = f'{first} {last}'  # Using f-strings
print(full_name2)


#python numbers 

x = 10
y = 3

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y)  # Floor division
print(x % y)  # Modulo
print(x ** y)  # Exponentiation

x += 5  # Augmented assignment
print(x)

#python math functions
import math

print(math.ceil(2.4))  # Round up to the nearest integer
print(math.floor(2.4))  # Round down to the nearest integer
print(math.sqrt(16))  # Calculate the square root

print(abs(-7))  # Absolute value
print(round(3.6))  # Round to the nearest integer