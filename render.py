from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import sys


graph_line = np.matrix([[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]])


def GraphLine():
	"""
	glEnableClientState(GL_VERTEX_ARRAY)
	vbo = GLuint()
	glGenBuffers(1,vbo)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	glBufferData(GL_ARRAY_BUFFER,sys.getsizeof(graph_line),graph_line,GL_STATIC_DRAW)
	glEnableVertexAttribArray(0)
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0)
	glDrawArrays(GL_LINES,0,1)
	"""
	glPushMatrix()
	glBegin(GL_LINES)
	for points in graph_line:
		glVertex3fv(points)
	glEnd()
	glPopMatrix()

def getPoints():
	return input().split(",")
	
def drawPolygon(Points):
	glBegin(GL_POLYGON)
	for points in Points:
		glVertex3fv(points)
	glEnd()
