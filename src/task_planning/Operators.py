#!/usr/bin/env python

from Fluents import Fluents
import time
import openravepy
import numpy as np
import herbpy

print "INSIDE OPERATOR"

class Operators(object):
    def __init__(self,object_id,env,robot,kinbody_env):
        
        self.env=env
        self.robot=robot
        self.kinbody_env = kinbody_env
        self.fluents=Fluents(self.env,self.robot,self.kinbody_env)
        self.object_id = object_id

    def Pick(self,object_id,object_loc):
        
        if (self.fluents.Holding()==None) and (self.fluents.In(object_id,object_loc)==True):# and (self.fluents.ClearX([object_id])==True):
            
#            import IPython
#            IPython.embed()

            self.robot.Grasp(object_id,manip = self.robot.right_arm)
            #herbpy.action.Grasp(object_id)#, manip = self.robot.right_arm)
            print str(object_id) + " has been picked"
        else:
            print False

    def Place(self,object_id,goal_id):

        if (self.fluents.Holding()==object_id) and (self.fluents.ClearX([object_id])==True):
            self.robot.Place(object_id,goal_id,manip = robot.right_arm)
            print str(object_id) + " has been placed"
        else:
            print False
