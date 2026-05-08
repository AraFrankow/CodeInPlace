from karel.stanfordkarel import *

def main():
    move_to_the_wall()
    turn_and_move()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move_to_the_wall()
    turn_and_move()
    turn_right()
    
def move_to_the_wall():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_and_move():
    turn_right()
    move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()