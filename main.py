from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np

import render as rn
import transf as tf

global M

locX=10
locY=10
sizeX=0
sizeY=0
window = 0                                             # glut window number
width, height = 500, 500                               # window size
width1, height1 = -500, -500                               # window size

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def draw_rect1(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(width1, width, height1, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

	
def draw():                                            # ondraw is called all the time
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
	glLoadIdentity()                                   # reset position
	refresh2d(width, height)                           # set mode to 2d
	rn.drawPolygon(M)
	rn.GraphLine()
	Ma = tf.transform(M)
	M = Ma
	glutSwapBuffers()   								# important for double buffering
	glutPostRedisplay()

# initialization
N = int(input())
PList = [] # DEFINE EMPTY LIST
for i in range(N): # GET POINTS
	X, Y = rn.getPoints()
	PList.append([int(X), int(Y),0])
M = np.matrix(PList)
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b"Tubes Algeo")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time   
glutMainLoop()
