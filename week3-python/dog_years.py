"""
Write a program which asks a user to input an age in human years, and converts it to the equivalent age in dog years.
"""
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    human_year = input("Enter an age in calendar years: ")
    age = int(human_year) * DOG_YEARS_MULTIPLIER
    print (f"That's {age} in dog years!")


if __name__ == '__main__':
    main()