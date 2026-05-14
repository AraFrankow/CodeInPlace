from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    while front_is_clear():
        while front_is_clear():
            put_beeper()
            move()
        put_beeper()
        turn_right()
        front_clear()
        turn_around()
        if front_is_clear():
            move()
            turn_around()
    turn_around()
    front_clear()

def front_clear():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()