from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
locX=10
locY=10
sizeX=0
sizeY=0
window = 0                                             # glut window number
width, height = 500, 400                               # window size
width1, height1 = -500, -400                               # window size

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

def draw_line():
    glBegin(GL_LINE)
    glVertex2f(10,10)
    glVertex2f(20,20)
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
    glLineWidth(2.5)
    glColor3f(1.0,1.0,1.0)
    draw_line()
    #sizex=int(input())
    #sizey=int(input())
    inputan=input()
    trans=inputan.split(' ')
    if(trans[0]=='translasi'):  
        glTranslatef(locX+(int(trans[1])),locY+(int(trans[2])),0)
    elif(trans[0]=='kotak'):
        global sizeX
        global sizeY
        sizeX=(int(trans[1]))
        sizeY=(int(trans[2]))
    elif(trans[0]=='rotate'):
        sudut=int(trans[1])
        glRotate(sudut,locX,locY,0)    
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_rect1(locX, locY, sizeX, sizeY)                        # rect at (10, 10) with width 200, height 100
    glutSwapBuffers()                                  # important for double buffering

X=True
# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b"Tubes Algeo")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
#glutIdleFunc(draw)                                     # draw all the time   
while(X):
    glutMainLoopEvent()
print("tes1")
