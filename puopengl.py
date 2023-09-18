import geopandas as gpd
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
data = gpd.read_file('s.dxf')
def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)
    
    for geom in data.geometry:
        if geom.geom_type == 'Polygon':
            for polygon in geom:
                glBegin(GL_POLYGON)
                for point in polygon.exterior.coords:
                    glVertex3f(point[0], point[1], 0)
                glEnd()
        elif geom.geom_type == 'LineString':
            glBegin(GL_LINE_STRIP)
            for point in geom.coords:
                glVertex3f(point[0], point[1], 0)
            glEnd()
        elif geom.geom_type == 'Point':
            glBegin(GL_POINTS)
            glVertex3f(geom.x, geom.y, 0)
            glEnd()
    
    pygame.display.flip()
    
def setup():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    
    glTranslatef(0.0, 0.0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        render()
setup()