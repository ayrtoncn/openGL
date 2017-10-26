# 2D GRAPHICS
# WITH OPENGL

# IMPORT PYGAME OPENGL NUMPY (for matrix)
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
from numpy import matrix

# END OF IMPORT

# FUNCTIONS

def getPoints():
	return input().split(",")

def main():
	N = int(input()) # INPUT N
	PList = [] # DEFINE EMPTY LIST
	for i in range(N): # GET POINTS
		X, Y = getPoints()
		PList.append([int(X),int(Y)]) 

	Points = np.array(PList)
	
	
main()
