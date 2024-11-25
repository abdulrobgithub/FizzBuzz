"""
A simple FizzBuzz implementation in Python.

This script prints numbers from 1 to MAX_VALUE. For multiples of three,
it prints "Fizz" instead of the number, and for multiples of five, it
prints "Buzz". For numbers that are multiples of both three and five,
it prints "FizzBuzz".
"""

MAX_VALUE = 17  # Change this value to modify the range

def fizzbuzz(n):
    """
    Determines the FizzBuzz output for a given number.
    
    Args:
        n (int): The number to evaluate.
    
    Returns:
        str or int: "Fizz", "Buzz", "FizzBuzz", or the number itself.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

def main():
    """
    Calls fizzbuzz on numbers from 1 to MAX_VALUE and prints the results.
    """
    for i in range(1, MAX_VALUE + 1):
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()
