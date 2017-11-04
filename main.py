from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np
import input as rn
import transf as tf


pertama=True
window = 0                                             # glut window number
width, height = 500, 500                               # window size
width1, height1 = -500, -500                               # window size
# initialization
def main():
	glutInit()                                             # initialize glut
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitWindowSize(width, height)                      # set window size
	glutInitWindowPosition(0, 0)                           # set window position
	window = glutCreateWindow(b"Tubes Algeo")              # create window with title
	glutDisplayFunc(draw)   								# set draw function callback
	glutIdleFunc(draw)                                     # draw all the time   
	glutMainLoop()                                          # done drawing a rectangle


	
	
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(width1, width, height1, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
	

def draw():                                            # ondraw is called all the time
	global pertama
	global defaultM
	global M
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
	glLoadIdentity()                                   # reset position
	refresh2d(width, height)                           # set mode to 2d
	if(pertama):
		rn.GraphLine()
		glutSwapBuffers()
		M = tf.getMatrix()
		pertama = False
	rn.GraphLine()
	rn.drawPolygon(M)
	#glutSwapBuffers()
	#glutSwapBuffers()
	M = tf.transform()
	glutSwapBuffers()
	glutPostRedisplay()
	


if __name__ == "__main__":
	main()
