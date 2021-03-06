#!/usr/bin/env python

from Fluents import Fluents
import openravepy
import numpy as np
import herbpy

print "INSIDE OPERATOR"

class Operators(object):
    def __init__(self,env,robot,kinbody_env):
        
        self.env=env
        self.robot=robot
        self.kinbody_env = kinbody_env
        self.fluents=Fluents(self.env,self.robot,self.kinbody_env)

    def Pick(self,object_id,object_loc):
        
        if (self.fluents.Holding()==None) and (self.fluents.In(object_id,object_loc)==True) and (self.fluents.ClearX([object_id])==True):#and (self.fluents.IsReachable(object_id)==True)

            self.robot.PushGrasp(object_id,manip = self.robot.right_arm)
	    self.robot.Lift(object_id, manip = self.robot.right_arm)
            print str(object_id) + " has been picked"
            return True
        else:
	    print str(object_id) + " has not been picked"
	    return False
            
    def Place(self,object_id,goal_id):

        if (self.fluents.Holding()==object_id):# and (self.fluents.ClearX([object_id])==True):
            self.robot.SetActiveManipulator(self.robot.right_arm)
            self.robot.Place(object_id,goal_id,manip = self.robot.right_arm)
            print str(object_id) + " has been placed"
	    return True
        else:
            print False
	    return False
