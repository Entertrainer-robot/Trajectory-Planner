# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:25:50 2020

@author: psubacz
"""

import numpy as np
#from time import perf_counter


class sparse_map:
    '''
    The robot has a map that is used to:
     - Keeping track of robot pose
     -  Storing known obstacles
     -  Each point in the map is correlated to a discrete point in real life. 
     -  Each point should has a ‘space take’ feature. This feature has a fragility counter, that is the higher the scaler, the less we want to throw a ball in that direction
     -  The scalar will be generated through an object recognition process; objects recognized will be tagged with higher scaler the more fragile something is. (glass and TVs should have a high value, walls and furniture should have a middle value, open space should have a low value.
     -  Similar to a point cloud

    '''
    
    def __init__(self,dis_x=3,dis_y=3,dis_z=3):
        '''
        creates a map of scores that can be used
        '''
        self._map = np.zeros((dis_x,dis_y,dis_z))
        
#    class Node():
#        '''
#        Node class to store information
#        '''
#        def __init__(self,seed_score = 0,last_seen = perf_counter()):
#            self.score = seed_score
#            self.last_seen = last_seen
#    
#    def __init__(self,dis_x=3,dis_y=3,dis_z=3):
#        self._map = [] 
#        for i in range(dis_x):
#            x = []
#            for ii in range(dis_y):
#                y = []
#                for iii in range(dis_z):
#                    y.append(self.Node())
#                x.append(y)
#            self._map.append(x)
#                
#    
#    def discretize_state(self,state):
#        '''
#        discretizes the state to the size of the map.
#        for example, x = 15.03231 will be discretized to 15.03 for a 4 int map
#        
#        saves space in case we have a large space state to work with
#        '''
#        discrete_state = np.around(state)
#        return discrete_state
#        
#        pass
#        


