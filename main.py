# 2D GRAPHICS
# WITH OPENGL

# IMPORT PYGAME OPENGL NUMPY (for matrix)
import render as rn
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# END OF IMPORT

SCREEN_SIZE = (600,600)

# FUNCTIONS


def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE, OPENGL|DOUBLEBUF)

	#gluPerspective(0, (SCREEN_SIZE[0]/SCREEN_SIZE[1]), 0.1, 50.0)
	#glTranslatef(0.0,0.000001,)

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	rn.GraphLine()
	pygame.display.flip()

	
	#while True:
	#for event in pygame.event.get():
	#	if event.type == pygame.QUIT:
	#		pygame.quit()
	#		quit()

	N = int(input()) # INPUT N
	#PList = [] # DEFINE EMPTY LIST
	#for i in range(N): # GET POINTS
	#	X, Y = getPoints()
	#	PList.append([int(X),int(Y)]) 

	#Points = np.array(PList)
	
	
	
main()