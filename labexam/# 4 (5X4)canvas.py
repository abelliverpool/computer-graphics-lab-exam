#question 4 part A

import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of which is 500 X 400 
    canvas_width = 500
    canvas_height = 400

    # Create the canvas
    canvas = pygame.display.set_mode((canvas_width, canvas_height))

    # title 

    pygame.display.set_caption("Canvas")
    # Fill the canvas with white color
   
    canvas.fill((255,255,255))
    #  question 4 part  B :Draw a red line 
    pygame.draw.line(canvas, (255, 0, 0), (50, 50), (50 + 200, 50), 3)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.quit()
                    sys.exit()

        # Update the canvas
        pygame.display.update()

# Call the main function
main()

# question 4 part C : Draw a triangle using vertices ||  Use draw.polygon or just use vertices to draw triangles and
# write a code that displays a shape as shown below:

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_triangle(vertices, color):
    glBegin(GL_TRIANGLES)
    glColor3f(*color)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    width, height = 500, 400
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Draw Shape")

    # Set up OpenGL
    glClearColor(1, 1, 1, 1)  # White background

    # Define vertices for the blue triangle
    blue_triangle = [
        (0, 1),
        (-1, -1),
        (1, -1)
    ]

    # Define vertices for the white triangle
    white_triangle = [
        (0, 0.5),
        (-0.5, -0.5),
        (0.5, -0.5)
    ]

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_F1):
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw the blue triangle
        draw_triangle(blue_triangle, (0, 0, 1))  # Blue color
        
        # Draw the white triangle
        draw_triangle(white_triangle, (1, 1, 1))  # White color
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
