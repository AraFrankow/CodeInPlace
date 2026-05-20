from karel.stanfordkarel import *

"""
Get Karel to create a checkerboard pattern of beepers inside an empty rectangular world,
"""


def main():
    put_beeper()
    while left_is_clear():
        checker_row()
        ascend_row_and_setup()
    checker_row()
    go_home()

def go_home():
    turn_right()
    move_to_wall()
    turn_left()

def ascend_row_and_setup():
    if beepers_present():
        ascend_row()
    else:
        ascend_row()
        put_beeper()

def ascend_row():
    turn_left()
    move()
    turn_right()

def checker_row():
    if beepers_present():
        if front_is_clear():
            move()
            checker_from_empty_corner()
    else:
        checker_from_empty_corner()
    return_to_column_1()

def return_to_column_1():
    turn_around()
    move_to_wall()
    turn_around()

def checker_from_empty_corner():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()