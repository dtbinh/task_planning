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

        # add a table
        self.table = self.env.ReadKinBodyXMLFile('models/data/furniture/table.kinbody.xml')
        #self.table = self.env.ReadKinBodyXMLFile('furniture/table.kinbody.xml')
        self.env.Add(self.table)
        self.table.SetName("table")
        table_pose = np.array([[ 0, 0, -1, 0.9], 
                                  [-1, 0,  0, 0], 
                                  [ 0, 1,  0, 0], 
                                  [ 0, 0,  0, 1]])
        self.table.SetTransform(table_pose)

        #add kinbodies
        #glass 1
        self.target_kinbody1 = self.env.ReadKinBodyURI('models/data/objects/plastic_glass.kinbody.xml')
        self.target_kinbody1.SetName("glass1")
        self.env.Add(self.target_kinbody1)
        glass_pose = np.array([[ 0, 0, 0, 1.0], 
                              [-1, 0,  1, -0.5], 
                              [ 0, 1,  0, 0.7165], 
                              [ 0, 0,  0, 1]])
        self.target_kinbody1.SetTransform(glass_pose)
        self.place_on(self.target_kinbody1, self.table)

        #glass 2
        self.target_kinbody2 = self.env.ReadKinBodyURI('models/data/objects/plastic_glass.kinbody.xml')
        self.target_kinbody2.SetName("glass2")
        self.env.Add(self.target_kinbody2)
        glass_pose = np.array([[ 0, 0, 0, 0.8], 
                                  [-1, 0,  1, -0.4], 
                                  [ 0, 1,  0, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_kinbody2.SetTransform(glass_pose)
        self.place_on(self.target_kinbody2, self.table)

        #glass 3
        self.target_kinbody3 = self.env.ReadKinBodyURI('models/data/objects/plastic_glass.kinbody.xml')
        self.target_kinbody3.SetName("glass3")
        self.env.Add(self.target_kinbody3)
        glass_pose = np.array([[ 0, 0, 0, 1.0], 
                                  [-1, 0,  1, -0.3], 
                                  [ 0, 1,  0, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_kinbody3.SetTransform(glass_pose)
        self.place_on(self.target_kinbody3, self.table)

        #add tray
        self.target_tray = self.env.ReadKinBodyURI('models/data/objects/wicker_tray.kinbody.xml')
        self.env.Add(self.target_tray)
        tray_pose = np.array([[ 0, 1, 0, 0.9], 
                                  [1, 0,  0, 0.5], 
                                  [ 0, 0,  1, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_tray.SetTransform(tray_pose)
        self.place_on(self.target_tray, self.table)

        #creating object list
        self.obj_list=[self.target_kinbody1, self.target_kinbody2, self.target_kinbody3]

    def bounding_box(self,body):
        obj  = body.ComputeAABB()
        max_xyz =  obj.pos()+obj.extents()
        min_xyz =  obj.pos()-obj.extents()
        min_max=np.hstack((min_xyz,max_xyz)).tolist()
        #print min_max
        return min_max

    def place_on(self, obj, on_obj):
        pos = obj.GetTransform()
        while obj.GetEnv().CheckCollision(obj, on_obj):
            pos[2,3] += 0.01
            obj.SetTransform(pos)
