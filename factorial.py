""" This script calculates factorial of given number """
import sys
def factorial(n):
    """
    This function calculates factorial using recursion
    """
    return 1 if n == 1 else n * factorial(n - 1)

def validate_argument(arg):
    """
    This function validates given argument
    """
    try:
        if int(arg) < 1:
            raise Exception
        if isinstance(int(arg), int):
            return True
    except Exception as e:
        print(f"Please provide positive int number")
def main():
    """
    This is a main function
    """
    args = len(sys.argv) - 1
    if args != 1:
        print(f"Please run this script with one parameter")
        sys.exit()
    elif args == 1:
        num = sys.argv[1]

        if validate_argument(num):
            print(f"Factorial of given number equals {factorial(int(num))}")

if __name__ == "__main__":
    main()

