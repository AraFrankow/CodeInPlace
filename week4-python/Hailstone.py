"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    my_num = int(input("Enter a number: "))
    while my_num != 1:
        remainder = my_num % 2
        if remainder == 1:
            result = 3 * my_num + 1
            result = int(result)
            print(f"{my_num} is odd, so I make 3n + 1: {result}")
            my_num = result
        else:
            result = my_num / 2
            result = int(result)
            print(f"{my_num} is even, so I take half: {result}")
            my_num = result

if __name__ == "__main__":
    main()