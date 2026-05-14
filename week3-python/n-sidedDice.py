import random

def main():
    sides_str = input("How many sides does your dice have? ")
    sides_int = int(sides_str)
    dado = random.randint(1, sides_int)
    print("Your roll is "+str(dado))

if __name__ == '__main__':
    main()