from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys


graph_line = np.matrix([[0,500,0],[0,-500,0],[500,0,0],[-500,0,0]])
width, height = 500, 500                           		    # window size
width1, height1 = -500, -500                               # window size

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
	drawGrid()
	glBegin(GL_LINES)
	glColor3f(1.0,1.0,1.0)
	for points in graph_line:
		glVertex3fv(points)
	glEnd()
	
	
def drawGrid():
	#draw horizontal grid
	X = width1
	Y = height1
	glBegin(GL_LINES)
	glColor3f(0.2,0.2,0.2)
	while (X < width):
		glVertex3fv((X,height1,0))
		glVertex3fv((X,height,0))
		X += 100
	while (Y < height):
		glVertex3fv((width1,Y,0))
		glVertex3fv((width,Y,0))
		Y += 100
	glEnd()
	

def getPoints(N):
	s = "> Input Titik "+ str(N) + ": "
	
	return input(s).split(",")
	
def triangulate(polygon):
    vertices = []
    def edgeFlagCallback(param1, param2): pass
    def beginCallback(param=None):
        vertices = []
    def vertexCallback(vertex, otherData=None):
        vertices.append(vertex)
    def combineCallback(vertex, neighbors, neighborWeights, out=None):
        out = vertex
        return out
    def endCallback(data=None): pass

    tess = gluNewTess()
    gluTessProperty(tess, GLU_TESS_WINDING_RULE, GLU_TESS_WINDING_ODD)
    gluTessCallback(tess, GLU_TESS_EDGE_FLAG_DATA, edgeFlagCallback)#forces triangulation of polygons (i.e. GL_TRIANGLES) rather than returning triangle fans or strips
    gluTessCallback(tess, GLU_TESS_BEGIN, beginCallback)
    gluTessCallback(tess, GLU_TESS_VERTEX, vertexCallback)
    gluTessCallback(tess, GLU_TESS_COMBINE, combineCallback)
    gluTessCallback(tess, GLU_TESS_END, endCallback)
    gluTessBeginPolygon(tess, 0)

    #first handle the main polygon
    gluTessBeginContour(tess)
    for point in polygon:
        point3d = (point[0,0], point[0,1], point[0,2])
        gluTessVertex(tess, point3d, point3d)
    gluTessEndContour(tess)

   

    gluTessEndPolygon(tess)
    gluDeleteTess(tess)
    return vertices
	
def drawPolygon(Polygon):
	vertices = triangulate(Polygon)
	glBegin(GL_TRIANGLES)
	glColor3f(0.5, 1.0, 0.5)  
	for points in vertices:
		glVertex3fv(points)
	glEnd()
	glutSwapBuffers()
	
