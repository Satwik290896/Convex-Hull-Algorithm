# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import glob
import shutil 
import sys
from numpy import *
import operator
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt


def main():
    #Robot_Configuration = array(sys.argv[1])
    #Obstacle_Verices = array(sys.argv[2])
    Robot_Configuration = array([(0,0),(1,0),(0,1),(-1,-1)])
    Obstacle_Vertices = array([(4,5),(9,10),(6,14),(3,10),(3,5)])
    Robot_Reference_point = array([(0,0)])
    Robot_Vertices = Robot_Configuration[1:len(Robot_Configuration)] - Robot_Configuration[0]
    
    Minkowski_sum(Robot_Reference_point, Robot_Vertices, Obstacle_Vertices)


def Minkowski_sum(Robot_Reference_point, Robot_Vertices, O_Vertices):
    Inv_Robot_Vertices = Inv_pairs_at_Ref(Robot_Reference_point, Robot_Vertices)
    Obstacle_C_Space = []
    
    for i in range(len(O_Vertices)):
        for j in range(len(Inv_Robot_Vertices)):
            Obstacle_C_Space.append(O_Vertices[i]+Inv_Robot_Vertices[j])
    
    hull = ConvexHull(Obstacle_C_Space)
    Obstacle_C_Space = array(Obstacle_C_Space)
    
    plt.plot(Obstacle_C_Space[:,0], Obstacle_C_Space[:,1], 'o')
    
    for simplex in hull.simplices:
        plt.plot(Obstacle_C_Space[simplex, 0], Obstacle_C_Space[simplex, 1], 'k-')

def Inv_pairs_at_Ref(Reference_point, Vertices):
    Vertices = Vertices - Reference_point
    Inv_Vertices = (-1)*Vertices + Reference_point
    
    return Inv_Vertices




main()