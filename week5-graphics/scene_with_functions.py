from graphics import Canvas
import math
"""
In this assignment, you will draw a natural scene while practicing how to break a program into functions with parameters. 
You are also being given an AI code-completion tool for this assignment. 
The tool can suggest code, but you are responsible for reading the generated code carefully and deciding whether it is correct.
"""
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_sun(canvas, 60, 50)
    
    
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 20, 50, 'pink')
    draw_cloud(canvas, 260, 35, 'purple')

    draw_tree(canvas, 50, 280, "green")
    draw_tree(canvas, 150, 280, "red")
    draw_tree(canvas, 300, 280, "orange")
    draw_grass(canvas, 0, 300)
    
    draw_house(canvas, 200, 280, "skyblue")
    
    # TODO: draw two more clouds, and three trees

def draw_house(canvas, x, y, color):
    """Draws a house with the bottom left corner at (x, y)."""
    house_width = 80
    house_height = 60
    roof_height = 40

    # Draw the main house rectangle
    canvas.create_rectangle(
        x,
        y - house_height,
        x + house_width,
        y,
        color
    )

    # Draw the roof as a triangle
    roof_peak_x = x + house_width / 2
    roof_peak_y = y - house_height - roof_height
    canvas.create_polygon(
        x, y - house_height,
        x + house_width, y - house_height,
        roof_peak_x, roof_peak_y,
        color="brown"
    )

def draw_grass(canvas, x, y):
    """Draws a patch of grass at (x, y)."""
    grass_height = 20
    grass_width = 400
    canvas.create_rectangle(
        x,
        y - grass_height,
        x + grass_width,
        y,
        "green"
    )

def draw_sun(canvas, x, y):
    """Draws the sun centered at (x, y)."""
    sun_radius = 40
    canvas.create_oval(
        x - sun_radius, y - sun_radius,
        x + sun_radius, y + sun_radius,
        "yellow"
    )

def draw_tree(canvas, x, y, color):
    """Draws a tree at (x, y) with the given color for the leaves."""
    # Draw the trunk
    canvas.create_rectangle(
        x,
        y - TRUNK_HEIGHT,
        x + TRUNK_WIDTH,
        y,
        "brown"
    )
    # Draw the leaves
    leaf_center_x = x + TRUNK_WIDTH / 2
    leaf_center_y = y - TRUNK_HEIGHT - LEAVES_SIZE / 2.5
    canvas.create_oval(
        leaf_center_x - LEAVES_SIZE / 2,
        leaf_center_y - LEAVES_SIZE / 2,
        leaf_center_x + LEAVES_SIZE / 2,
        leaf_center_y + LEAVES_SIZE / 2,
        color
    )
def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

# TODO: You should define a function like draw_cloud
# for trees, as well as for any extra elements in the scene.


if __name__ == '__main__':
    main()