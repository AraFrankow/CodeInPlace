from karel.stanfordkarel import *

def main():
    move_to_beeper()
    pick_beeper()
    move()
    turn_left()
    move_to_beeper()
    turn_around()
    move()
    put_beeper()
    move_to_the_wall()
    turn_right()
    move_to_the_wall()
    turn_around()

def move_to_beeper():
    while no_beepers_present():
        move()

def move_to_the_wall():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()