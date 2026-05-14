from karel.stanfordkarel import *

# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.

def main():
    while front_is_clear():
        move()
        if beepers_present():
            while beepers_present():
                pick_beeper()

if __name__ == '__main__':
    main()