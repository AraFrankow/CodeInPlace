from graphics import Canvas
"""
Students in Code in Place are from 150 different countries! Wow. 
Let's celebrate our international class by drawing flags. 
To start out, one of the most straightforward flags to draw using Python graphics is the flag of Indonesia
"""
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    canvas.create_rectangle(
        0,
        0,
        CANVAS_WIDTH,
        CANVAS_HEIGHT / 2,
        "red"
    )

if __name__ == '__main__':
    main()