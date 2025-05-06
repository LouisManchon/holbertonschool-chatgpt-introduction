#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    """
    Entry point of the script. Parses command-line input and prints the factorial.
    """
    if len(sys.argv) != 2:
        print("Usage: {} <non-negative integer>".format(sys.argv[0]))
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        result = factorial(num)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
