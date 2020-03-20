# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:49:29 2020

@author: psubacz
"""

class Ball:
    '''
    ball class used to simulate a tennis ball
    '''
    def __init__(self):
        
        #tennis ball diameter (cm)
        self.tDiameter = 6.54
        #tennis ball mass (g)
        self.tMass = 56
        self.reset_ball()
        
    def reset_ball(self):
        self.x = 0
        self.y = 0
        self.z = 0