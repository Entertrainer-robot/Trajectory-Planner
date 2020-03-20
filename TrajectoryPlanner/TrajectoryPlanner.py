# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:11:35 2020

@author: psubacz
"""

#load env
#find direction 
#calucalate trajectory
#
import numpy as np
from collections import deque
from datatypes_and_strucutures.tennis_ball import Ball
from physics_model import Flight_Model_1

        
class TrajectoryPlanner:
    '''
    
    '''
    def __init__(self, balls_loaded = None, ori = 0):
        
        if balls_loaded ==None:
            self.balls_loaded = deque([Ball(),Ball(),Ball()],3)
        else:
            self.balls_loaded = balls_loaded
        #X-Y orienetation of the robot from map
        self.ori = ori
        
        self.FM1 =Flight_Model_1()
        
        self.MAX_RANGE = 4.572 #m
        
        print(self.get_ball_loadout())
        
        self.lnchr_angle = self.FM1.deg_2_rad(45)
        
    def get_ball_loadout(self):
        return len(self.balls_loaded)
    
    def get_lnchr_angle(self):
        return self.lnchr_angle
    
    def calc_lnch_vel(self,d):
        '''
        placeholder function for spring calculation from distance to velocity
        
        waiting on dan/troy to finish mechanical calculations
        '''
        
        spring_low = 1 #m/s
        spring_high = 22 #m/s
        return np.random.uniform(spring_low,spring_high)
    
    def get_dead_rkn_dist(self):
        '''
        placeholder function to get dead reckoning linear distance infront of 
        the robot
        '''
        launch_low = 0.01 #m 
        launch_high = 10 #m
        return np.random.uniform(launch_low,launch_high)
        
        
    def calculate_trajectory(self,g = -9.81):
        '''
        Generates a trajectory path from the currect location and orientation 
        to a target location and orientation
        
        '''
        
        #Query a random range from the map or range finder
        d = self.get_dead_rkn_dist()
        
        #if the range is not known, then do not shoot. 
        if d>self.MAX_RANGE:
            return False
        
        #calculate the minimum velocity needed to reach the distance.  
        vel = self.calc_lnch_vel(d)
        if vel == False:
            return False
        #calcalute the angle to possibly shoot from, Pick the angle that has 
        #   the least ammount of movement
        x_disp = self.FM1.cal_angle_reach(g,d,vel)
        if (np.isnan(x_disp[0])and np.isnan(x_disp[1])):
            return False
        
        #pick the angle that has the shortest travel from the current angle
        self.lnchr_angle = x_disp[0] if (np.abs(self.lnchr_angle-x_disp[0])<np.abs(self.lnchr_angle-x_disp[1])) else x_disp[1]
        
        print(d,vel,x_disp)
        trajectoryPath = None
        
#        while True:
#            
#            
#            if trajectoryPath is not None:
#                break
#            #create a trajectory generator 
#            v_0
#            theta = 45
#            traj_gen = self.FM1.trajectory_seq(vel,45,-9.81)



        
        
        
        
        
        trajectoryPath = None
        return trajectoryPath
    
    def evaluate_trajectory(self,map_,traj_cord):
        if map_[traj_cord[0]][traj_cord[1]] >10:
            return False
        else:
            return True

TP = TrajectoryPlanner()
TP.calculate_trajectory()