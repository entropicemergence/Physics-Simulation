# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:45:20 2019

@author: i
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:17:10 2019

@author: i
"""
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np



def axis():
    ax=np.array([[-9,0,0],[9,0,0]])
    
    glBegin(GL_LINES)
    
    glVertex3fv(ax[0])
    glVertex3fv(ax[1])
    glEnd()

    

def line(location):
    
    glBegin(GL_LINES)
    
    for loc in location:
        glVertex2fv(loc)
    glEnd()
    
def lineb(location):
    glBegin(GL_LINES)
    for loc in range(location.shape[0]-1):
        glVertex2fv(location[loc])
        glVertex2fv(location[loc+1])
        glColor3fv((0,1,0))
    glEnd()
    
def circle(center, radius):
    glBegin(GL_LINES)
    q=(np.linspace(0,2*np.pi,24))
    x=(radius*np.sin(q))+center[0]
    y=(radius*np.cos(q))+center[1]
    for n in range(23):
        glVertex2fv([x[n],y[n]])
        glVertex2fv([x[n+1],y[n+1]])
        glColor3fv((0,1,1))
#    glVertex3fv(ax[0])
#    glVertex3fv(ax[1])
    glEnd();

def points(initial):
    
    initial=initial+(np.random.random([initial.shape[0],3])-0.5)*0.08
    # Plot points in bright red
    glColor3f(0.0, 1.0, 0.0)
    # Increase the point size
    
    glPointSize(1.4)
    glBegin(GL_POINTS)
    for aa in initial:   
        glVertex3f(aa[0], aa[1],aa[2])
#        glVertex2f(0.4, 0)
    glEnd()
    return initial


def main():
    pygame.init()
    display = (1280,760)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(50, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    n=15000
    initial=np.random.random([n,3])-0.5
    initialbol=np.ones([n])*0.5
    initial=initial[initialbol>((initial[:,0]**2)+(initial[:,1]**2)+(initial[:,2]**2))**0.5]
            
        

    while True:

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#        
#        axis()
#        circle([0,0],0.99)
#        circle([0.,0.99],0.4)
        initial=points(initial)

        
        pygame.display.flip()
        pygame.time.wait(10)


main()