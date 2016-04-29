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
        
        if (self.fluents.Holding()==None) and (self.fluents.In(object_id,object_loc)==True):#and (self.fluents.ClearX([object_id])==True):
            check=0
            for obj in self.kinbody_env.obj_list:
                if obj is not object_id:
                    if not self.env.CheckCollision(self.robot,obj):
                        check+=1

            #from prpy.rave import Disabled
            #if check==len(self.kinbody_env.obj_list)-1:
            import IPython
            IPython.embed()
            self.robot.Grasp(object_id,manip = self.robot.right_arm)
        
            print str(object_id) + " has been picked"
        else:
            print False

    def Place(self,object_id,goal_id):

        if (self.fluents.Holding()==object_id):# and (self.fluents.ClearX([object_id])==True):
            self.robot.SetActiveManipulator(self.robot.right_arm)
            self.robot.Place(object_id,goal_id,manip = self.robot.right_arm)

            print str(object_id) + " has been placed"
        else:
            print False
