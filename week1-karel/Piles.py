from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move()
        if beepers_present():
            while beepers_present():
                pick_beeper()

if __name__ == '__main__':
    main()