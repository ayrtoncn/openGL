from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np
from math import *
import render as rn
import transf as tf
pertama=True
locX=10
locY=10
sizeX=0
sizeY=0
window = 0                                             # glut window number
width, height = 500, 500                               # window size
width1, height1 = -500, -500                               # window size
# initialization
def main():
	N = int(input())
	PList = [] # DEFINE EMPTY LIST
	global M
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
	global pertama
	global defaultM
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
	glLoadIdentity()                                   # reset position
	refresh2d(width, height)                           # set mode to 2d
	rn.drawPolygon(M)
	rn.GraphLine()
	glutSwapBuffers()   								# important for double buffering
	if(pertama):
		defaultM=M
	while(not(pertama)):
		n=input()
		inpTransfType=n.split(' ')
		if inpTransfType[0] == "translate" :
			X=int(inpTransfType[1])
			Y=int(inpTransfType[2])
			for points in M:
				points[0,0]=points[0,0]+X
				points[0,1]=points[0,1]+Y
			glutSwapBuffers()
			break
		elif inpTransfType[0] == "dilate" :
			dil=float(inpTransfType[1])
			for points in M:
				points[0,0]=points[0,0]*dil
				points[0,1]=points[0,1]*dil
			glutSwapBuffers()
			break
		elif inpTransfType[0] == "rotate" :
			sdt=radians(float(inpTransfType[1]))
			X=int(inpTransfType[2])
			Y=int(inpTransfType[3])
			for points in M:
				X1=points[0,0]
				Y1=points[0,1]
				points[0,0]=(cos(sdt)*(X1-X)-(sin(sdt))*(Y1-Y))+X
				points[0,1]=(sin(sdt)*(X1-X)+(cos(sdt))*(Y1-Y))+Y
			glutSwapBuffers()
			break
		elif inpTransfType[0] == "reflect" :
			param=inpTransfType[1]
			temp=param.split(',')
			if(len(temp)==1):
				if(param=='y=x'):
					for points in M:
						temp=points[0,0]
						points[0,0]=-points[0,1]
						points[0,1]=-temp
				elif(param=='y=-x'):
					for points in M:
						temp=points[0,0]
						points[0,0]=points[0,1]
						points[0,1]=temp
				elif(param=='x'):
					for points in M:
						points[0,1]=-points[0,1]
				elif(param=='y'):
					for points in M:
						points[0,0]=-points[0,0]
			else:
				X=float(temp[0][1:])
				Y=float(temp[1][:len(temp[1])-1])
				sdt=radians(180)
				for points in M:
					X1=points[0,0]
					Y1=points[0,1]
					points[0,0]=(cos(sdt)*(X1-X)-(sin(sdt))*(Y1-Y))+X
					points[0,1]=(sin(sdt)*(X1-X)+(cos(sdt))*(Y1-Y))+Y
			glutSwapBuffers()
			break
		elif inpTransfType[0] == "sheer" :
			sumbu=inpTransfType[1]
			K=float(inpTransfType[2])
			if(sumbu=='x'):
				for points in M:
					points[0,0]=points[0,0]+K*points[0,1]	
			elif(sumbu=='y'):
				for points in M:
					points[0,1]=points[0,1]+K*points[0,0]	
			glutSwapBuffers()
			break
		elif inpTransfType[0] == "stretch" :
			sumbu=inpTransfType[1]
			K=float(inpTransfType[2])
			if(sumbu=='x'):
				for points in M:
					points[0,0]=K*points[0,0]	
			elif(sumbu=='y'):
				for points in M:
					points[0,1]=K*points[0,1]	
			glutSwapBuffers()
			break
		elif inpTransfType[0]=='reset':
			print("test")
		elif inpTransfType[0]=='exit':
			exit()
	pertama=False
	glutPostRedisplay()


if __name__ == "__main__":
	main()
