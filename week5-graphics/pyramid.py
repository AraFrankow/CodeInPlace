from graphics import Canvas
import random
""""
Write a program that draws a pyramid consisting of bricks arranged in horizontal rows, so that the number of bricks in each row decreases by one as you move up the pyramid
"""

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base
ROWS_IN_PYRAMID = BRICKS_IN_BASE

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for row in range(ROWS_IN_PYRAMID):
        bricks_in_row = BRICKS_IN_BASE - row
        for brick in range(bricks_in_row):
            left_x = (CANVAS_WIDTH - (BRICK_WIDTH * bricks_in_row)) /2 + brick * BRICK_WIDTH
            top_y = CANVAS_HEIGHT - ((row + 1) * BRICK_HEIGHT)

            right_x = left_x + BRICK_WIDTH
            bottom_y = top_y + BRICK_HEIGHT

            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "yellow", "black")
    
if __name__ == '__main__':
    main()