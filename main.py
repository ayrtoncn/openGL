# 2D GRAPHICS
# WITH OPENGL

# IMPORT PYGAME OPENGL NUMPY (for matrix)
import render as rn
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# END OF IMPORT

SCREEN_SIZE = (800,800)

# FUNCTIONS



def main():

	pygame.display.set_mode(SCREEN_SIZE, OPENGL|DOUBLEBUF)

	#glEnable(GL_DEPTH_TEST)
	gluPerspective(45, (SCREEN_SIZE[0]/SCREEN_SIZE[1]), 0.1, 50.0)
	glOrtho(-1,1,-1,1,0.1,50)
	#glViewport(0,0,500,500)

	#Menggambar Graph Line

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	rn.GraphLine()
	pygame.display.flip()
	pygame.time.wait(10)
	"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	"""
	
	#DRAW
	#while True:
	#glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	#rn.GraphLine()
	#pygame.display.flip()
	#pygame.time.wait(10)
	
	N = int(input())
	PList = [] # DEFINE EMPTY LIST
	for i in range(N): # GET POINTS
		X, Y = rn.getPoints()
		PList.append([int(X)/SCREEN_SIZE[0], int(Y)/SCREEN_SIZE[1],0.0])
	rn.drawPolygon(PList)
	pygame.display.flip()
	
	
	x = input()
	
	
	
	#Points = np.array(PList)
	
	
	
main()