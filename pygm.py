import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Inicializar Pygame
pygame.init()

# Crear una ventana
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Configurar la vista de OpenGL
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, width, 0, height, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Función para dibujar el triángulo
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(400, 100)
    glVertex2f(200, 500)
    glVertex2f(600, 500)
    glEnd()

# Bucle principal de la aplicación
while True:
    # Manejo de eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Limpiar el búfer de la ventana
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Dibujar el triángulo
    draw_triangle()

    # Actualizar la ventana
    pygame.display.flip()
    pygame.time.wait(10)