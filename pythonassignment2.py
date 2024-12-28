# -*- coding: utf-8 -*-
"""PythonAssignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CKujDWBFpFR9DuJBghmP6OBhLm7bXPrk

Name :- Divyesh Nath Tripathi

Q1: Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.

Answer: The def keyword is used to create a function in Python. Here's a function to return the list of odd numbers:
"""

def odd_numbers():
    return [num for num in range(1, 26) if num % 2 != 0]

print(odd_numbers())

"""Q2: Why *args and **kwargs are used in some functions? Create a function each for *args and **kwargs to demonstrate their use.
Answer:
*args is used to pass a variable number of positional arguments to a function.
**kwargs is used to pass a variable number of keyword arguments to a function.
"""

# Function using *args
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))

# Function using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(Name="Alice", Age=25, City="New York")

"""Q3: What is an iterator in Python? Name the method used to initialize the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

Answer:
An iterator is an object that can be iterated upon.
iter() is used to initialize an iterator, and next() is used for iteration.
"""

nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iterator = iter(nums)
for _ in range(5):
    print(next(iterator))

"""Q4: What is a generator function in Python? Why is the yield keyword used? Give an example of a generator function.

Answer:
A generator function in Python is used to return an iterator. It uses yield to produce a series of values instead of returning them all at once.
"""

def square_numbers(n):
    for i in range(n):
        yield i ** 2

squares = square_numbers(5)
for square in squares:
    print(square)

"""Q5: Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

Answer:
"""

def prime_numbers():
    for num in range(2, 1000):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num

primes = prime_numbers()
for _ in range(20):
    print(next(primes))

"""Q6: Write a Python program to print the first 10 Fibonacci numbers using a while loop.

Answer:
"""

a, b = 0, 1
count = 0
while count < 10:
    print(a)
    a, b = b, a + b
    count += 1

"""Q7: Write a List Comprehension to iterate through the string 'pwskills'.

Answer:
"""

string = 'pwskills'
output = [char for char in string]
print(output)

"""Q8: Write a Python program to check whether a given number is a Palindrome or not using a while loop.

Answer:
"""

def is_palindrome(num):
    original = str(num)
    reverse = original[::-1]
    return original == reverse

number = 121
print(f"{number} is a palindrome: {is_palindrome(number)}")

"""Q9: Write a code to print odd numbers from 1 to 100 using list comprehension.

Answer:
"""

# Create a list from 1 to 100
numbers = [num for num in range(1, 101)]
# Filter odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)