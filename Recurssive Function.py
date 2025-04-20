def factorial(n):
    if n == 1: # The termination condition
        return 1 # The base case
    else:
        res = n * factorial(n-1) # The recursive call
        return res
print(factorial(7))

# Write a program to determine if a given number is a Prime Number or not. Use
#  recursion to implement the solution. The following code snippet illustrates how
#  this might work:

def is_prime_recursive(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor - 1)

# Test cases
print('is_prime(3):', is_prime_recursive(3))   # True
print('is_prime(7):', is_prime_recursive(7))   # True
print('is_prime(9):', is_prime_recursive(9))   # False
print('is_prime(31):', is_prime_recursive(31)) # True
print('is_prime(49):', is_prime_recursive(49)) # False


# Write a function which implements Pascal’s triangle for a specified number of
#  rows. Pascals triangle is a triangle of the binomial coefficients. The values held
#  in the triangle are generated as follows: In row 0 (the topmost row), there is a
#  unique nonzero entry 1. Each entry of each subsequent row is constructed by
#  adding the number above and to the left with the number above and to the right,
#  treating blank entries as 0. For example, the initial number in the first (or any
#  other) row is 1 (the sum of 0 and 1), whereas the numbers 1 and 3 in the third
#  row are added together to generate the number 4 in the fourth row. An example
#  of Pascals triangle for 4 rows is given below:

def pascal_triangle(n):
    for i in range(n):
        number = 1
        print(" " * (n - i), end="")  # for formatting
        for j in range(i + 1):
            print(number, end=" ")
            number = number * (i - j) // (j + 1)
        print()  # new line after each row

# Example usage
pascal_triangle(5)

def print_my_msg(msg):
    print(msg)
print_my_msg('Hello World')
print_my_msg('Good day')
print_my_msg('Welcome')
print_my_msg('Ola')


def square(n):
    return n * n
 # Store result from square in a variable
result = square( 4)
print(result)
# Send the result from square immediately to another function
print(square( 5))
 # Use the result returned from square in a conditional expression
if square(3) < 15:
 print(' Still less than 15 ')

 def swap(a, b):
    return b, a
 a = 2
 b = 3
 x, y = swap(a, b)
 print(x, ',', y)

def get_integer_input(message):
    """This function will display the message to the user
    and request that they input an integer.
    If the user enters something that is not a number
    then the input will be rejected
    and an error message will be displayed.
    The user will then be asked to try again."""
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)
age = get_integer_input('Please input your age: ')
print('age is', age)


def greeter(name, message):
    print('Welcome', name, '-', message)

greeter('Eloise','Hope you like Rugby')


def greeter(name, message='Live Long and Prosper'):
    print('Welcome', name, '-', message)


greeter('Eloise')
greeter('Eloise', 'Hope you like Python')

def greeter(name,
title = 'Dr',
prompt = 'Welcome',
message = 'Live Long and Prosper'):
 print(prompt, title, name, '-', message)

 def greeters(*args):
    for names in args:
        print('Welcome', names)
 greeters('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Jasmine')


