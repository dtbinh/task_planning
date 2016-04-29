#!/usr/bin/env python

from collections import deque
from Fluents import Fluents
from Operators import Operators
import time
#from herbpy import *

class Planner(object):

    print "INSIDE PLANNER"
    def __init__(self,planning_env,robot,kinbody_env):
        
        self.planning_env = planning_env
        self.list = kinbody_env.obj_list
        self.robot = robot
        self.kinbody_env = kinbody_env

    def Plan(self,object_list):
        goal_loc= self.kinbody_env.target_tray.GetTransform()
        print "goal:" + str(goal_loc)
        
        '''start_loc_box = self.kinbody_env.bounding_box(self.kinbody_env.table)
        start_loc_box[4] = (start_loc_box[1]+start_loc_box[4])/2
        op.Pick(self.list[1], start_loc_box)
        op.Place(self.list[1],self.kinbody_env.target_tray)
        time.sleep(10000)
	'''
	op = Operators(self.planning_env, self.robot,self.kinbody_env)
	start_loc_box = self.kinbody_env.bounding_box(self.kinbody_env.table)
        start_loc_box[4] = (start_loc_box[1]+start_loc_box[4])/2
        print "start bounding_box", start_loc_box
	list_picked = []
	c=0        
	while c<len(self.list):	
		for i in range(len(self.list)):
			print i

                	if op.Pick(self.list[i], start_loc_box) == True:
                    		op.Place(self.list[i],self.kinbody_env.target_tray)
			c+=1
	print "End of planner"
