from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    fill_row()
    reset()
    while beepers_present():
        remove_from_sides()
    if facing_east():
        turn_around()
        move()
        turn_around()
    else:
        turn_around()
    put_beeper()

def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def reset():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def remove_from_sides():
    pick_beeper()
    move()
    while beepers_present() and front_is_clear():
        move()
    turn_around()
    if no_beepers_present():
        move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()