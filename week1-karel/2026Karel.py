from karel.stanfordkarel import *

def main():
    for i in range(20):
        repet()
    move()
    for i in range(6):
        put_beeper()
    move()

def repet():
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    turn_right()

def turn_right():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()