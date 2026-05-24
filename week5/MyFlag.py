from graphics import Canvas
    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300

def main():
    radius = 40
    center_x = CANVAS_WIDTH / 2
    center_y = CANVAS_HEIGHT / 2

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    rectangle(canvas, 0, 0, CANVAS_WIDTH, CANVAS_HEIGHT/3, "skyblue")
    rectangle(canvas, 0, CANVAS_HEIGHT-(CANVAS_HEIGHT/3), CANVAS_WIDTH, CANVAS_HEIGHT/3, "white")
    canvas.create_oval((center_x - radius), (center_y - radius), (center_x + radius), (center_y + radius), "yellow")
    rectangle(canvas, 0, 322, CANVAS_WIDTH, CANVAS_HEIGHT-(CANVAS_HEIGHT/3), "skyblue")

def rectangle(canvas, x1, y1, x2, y2, color):
    rect = canvas.create_rectangle(x1, y1, x2, y2, color)

if __name__ == '__main__':
    main()