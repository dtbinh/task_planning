#!/usr/bin/env python
import openravepy
import numpy as np
import time

print "INSIDE HERBENV"

class HerbEnv(object):

    def __init__(self,env,robot):
        self.env = env
        self.robot = robot
        self.openrave_init()
        
    def openrave_init(self):
        
        #import IPython
        #IPython.embed()
        # add a table
#        self.table = self.env.ReadKinBodyXMLFile('models/data/furniture/table.kinbody.xml')
        self.table = self.env.ReadKinBodyXMLFile('furniture/table.kinbody.xml')
        self.env.Add(self.table)
        table_pose = np.array([[ 0, 0, -1, 0.8], 
                                  [-1, 0,  0, 0], 
                                  [ 0, 1,  0, 0], 
                                  [ 0, 0,  0, 1]])
        self.table.SetTransform(table_pose)

        #add kinbodies
        #glass 1
#        self.target_kinbody1 = self.env.ReadKinBodyURI('models/data/objects/glass.kinbody.xml')
        self.target_kinbody1 = self.env.ReadKinBodyXMLFile('objects/plastic_glass.kinbody.xml')
        self.target_kinbody1.SetName("glass1")
        self.robot.GetEnv().Add(self.target_kinbody1)
        glass_pose = np.array([[ 0, 0, 0, 0.7], 
                                  [-1, 0,  1, -0.5], 
                                  [ 0, 1,  0, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_kinbody1.SetTransform(glass_pose)

        #glass 2
        self.target_kinbody2 = self.env.ReadKinBodyURI('objects/plastic_glass.kinbody.xml')
        self.target_kinbody2.SetName("glass2")
        self.robot.GetEnv().Add(self.target_kinbody2)
        glass_pose = np.array([[ 0, 0, 0, 0.5], 
                                  [-1, 0,  1, -0.4], 
                                  [ 0, 1,  0, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_kinbody2.SetTransform(glass_pose)

        #glass 3
        self.target_kinbody3 = self.env.ReadKinBodyURI('objects/plastic_glass.kinbody.xml')
        self.target_kinbody2.SetName("glass3")
        self.robot.GetEnv().Add(self.target_kinbody3)
        glass_pose = np.array([[ 0, 0, 0, 0.7], 
                                  [-1, 0,  1, -0.3], 
                                  [ 0, 1,  0, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_kinbody3.SetTransform(glass_pose)

        #add tray
        self.target_tray = self.env.ReadKinBodyURI('objects/wicker_tray.kinbody.xml')
        self.robot.GetEnv().Add(self.target_tray)
        tray_pose = np.array([[ 0, 1, 0, 0.6], 
                                  [1, 0,  0, 0.5], 
                                  [ 0, 0,  1, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_tray.SetTransform(tray_pose)

        #creating object list
        self.obj_list=[self.target_kinbody1, self.target_kinbody2, self.target_kinbody3]

    def bounding_box(self,body):
        obj  = body.ComputeAABB()
        max_xyz =  obj.pos()+obj.extents()
        min_xyz =  obj.pos()-obj.extents()
        min_max=np.hstack((min_xyz,max_xyz)).tolist()
        #print min_max
        return min_max
