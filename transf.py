from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys




def inpTransfType():
	transfType = input()

def transform(M):
	if inpTransfType() == "translate" :
		X, Y = input().split(' ')
		for points in M:
			points[0,0]=points[0,0]+X
			points[0,1]=points[0,1]+Y
		'''ListAdd = []
		for points in M:
			ListAdd.append([X,Y,0])
		MAdd = np.matrix(ListAdd)
		M = np.add(ListAdd,M)'''
		print(M)
	return M