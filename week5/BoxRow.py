from graphics import Canvas
"""
Let's practice making graphics with lots of repeated elements. 
This will help us get familiar with working with multiple shapes and pixel calculations!
Make a line of boxes as shown below, such that the boxes fill the bottom of the canvas. 
Each box should have a width and height of BOX_SIZE, making a total of 5 boxes perfectly in line with one anothe
"""
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for i in range(N_BOXES):
        left = i * BOX_SIZE
        top = CANVAS_HEIGHT - BOX_SIZE
        right = left + BOX_SIZE
        bottom = CANVAS_HEIGHT

        canvas.create_rectangle(
            left, 
            top,
            right, 
            bottom,
            "white",
            "black"
        )

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()