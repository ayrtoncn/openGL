from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys




def inpTransfType():
	transfType = input()

def transform(M):
	if inpTransfType() == "translate" :
		X, Y = input().split(' ')
		ListAdd = []
		for points in M:
			ListAdd.append([X,Y,0])
		MAdd = np.matrix(ListAdd)
		M = np.add(ListAdd,M)
	return M