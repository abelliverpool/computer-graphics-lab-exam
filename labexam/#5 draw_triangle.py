import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    width, height = 500, 400
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Draw Triangle")

   
    glClearColor(1, 1, 1, 1)  # White background
    glColor3f(0.5, 0, 0.5)  # Purple color

   
    vertices = [
        (0, 1),
        (-1, -1),
        (1, -1)
    ]

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_F1):
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        for vertex in vertices:
            glVertex2f(*vertex)
        glEnd()
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
