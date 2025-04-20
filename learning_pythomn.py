print('hello world')
# Kilometers to Miles Converter
# This version validates positive numeric input only
dist_Km = input('Please type a positive distance in kilometers: ')
if dist_Km.isnumeric():
    dist_Km = int(dist_Km)
    if dist_Km > 0:
        dist_miles = dist_Km * 0.6214
        print(f'The distance in miles is: {dist_miles:.2f} miles')
    else:
        print("The distance must be greater than zero.")
else:
    print("Invalid input. Please enter a positive number.")

# Positive/Negative Checker
num = int(input('Enter a number: '))
if num < 0:
    print(num, 'is negative')
elif num > 0:
    print(num, 'is positive')
    print(num, 'squared is ', num * num)
else:
    print(num, 'is zero')
print('Bye')

# Factorial Calculator
user = input('Type your number to get the factorial!: ')
if user.isnumeric():
    number = int(user)
    if number == 0:
        print("The factorial of 0 is 1.")
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print(f"The factorial of {number} is {factorial}.")
else:
    print("Invalid input. Please enter a non-negative whole number.")

# Prime Number Finder
user_input = input("Enter a number greater than or equal to 2: ")
if user_input.isnumeric():
    max_number = int(user_input)
    if max_number < 2:
        print("Error: Please enter a number greater than or equal to 2.")
    else:
        print(f"Prime numbers from 2 to {max_number}:")
        for num in range(2, max_number + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)
else:
    print("Invalid input. Please enter a whole number greater than or equal to 2.")

# Even or Odd Checker
number = int(input('Please enter your value: '))
if number % 2 == 0:
    print('Your input is even', number)
else:
    print('Your input is odd', number)

# While Loop Counter
count = 0
print('Starting')
while count < 10:
    print(count, ' ', end='')
    count += 1
print()  # End of while loop
print('Done')

# For Loop with even number check
for i in range(0, 10):
    print(i, ' ', end='')
    if i % 2 == 1:
        continue
    print('hey its an even number')
    print('we love even numbers')
print('Done')

# Dice Roller
import random
MIN = 1
MAX = 6
roll_again = 'y'
while roll_again == 'y':
    print('Rolling the dices...')
    print('The values are....')
    dice1 = random.randint(MIN, MAX)
    print(dice1)
    dice2 = random.randint(MIN, MAX)
    print(dice2)
    roll_again = input('Roll the dices again? (y / n): ')

# Status Checker based on Age
age = 15
status = 'teenager' if 12 < age < 20 else 'not teenager'
print(status)
