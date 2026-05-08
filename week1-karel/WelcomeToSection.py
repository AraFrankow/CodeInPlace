from karel.stanfordkarel import *


def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        safe_move()

            
def build_hospital():
    build_column()
    move()
    build_column()

def build_column():
    if beepers_present():
        pick_beeper()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move_to_wall()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def safe_move():
    if front_is_clear():
        move()

if __name__ == '__main__':
    main()