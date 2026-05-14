from karel.stanfordkarel import *

def main():
    for i in range(2):
        down_to_up()
        move_4_squares()
        up_to_down()
        if front_is_clear():
            move_4_squares()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_and_put_beeper():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def move_4_squares():
    for i in range(4):
        move()

def down_to_up():
    turn_left()
    move_and_put_beeper()
    turn_right()

def up_to_down():
    turn_right()
    move_and_put_beeper()
    turn_left()

if __name__ == '__main__':
    main()