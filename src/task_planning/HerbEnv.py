#!/usr/bin/env python
import openravepy
import numpy as np
import time

print "INSIDE HERBENV"

class HerbEnv(object):

    def __init__(self,env,robot,sim):
        self.env = env
        self.robot = robot

	if sim:
            self.openrave_init()
        else:
            self.perception_init()
	       
    def perception_init(self):
        self.robot.right_arm.PlanToNamedConfiguration('home',execute=True)

        self.robot.DetectObjects()

        good =False
        while not good:
            for b in self.env.GetBodies():
                if b != self.robot:
                    self.env.Remove(b)

            self.robot.DetectObjects()

            check= raw_input('Press "enter" to continue, "r" to redetect')
            if check != 'r':
                good= True

        glasses = [b for b in self.env.GetBodies() if 'glass' in b.GetName()]
        self.table = [b for b in self.env.GetBodies() if 'table' in b.GetName()][0]
        self.target_tray = [b for b in self.env.GetBodies() if 'tray' in b.GetName()][0]
        table_pos=self.table.GetTransform()
	table_pos[2,3]+=0.04
	self.table.SetTransform(table_pos)
        for g in glasses:
            self.place_on(g, self.table)
            self.place_after(g)
        self.place_on(self.target_tray, self.table)


        self.obj_list=glasses
        
    def openrave_init(self):

        # add a table
        self.table = self.env.ReadKinBodyXMLFile('models/data/furniture/table.kinbody.xml')
        #self.table = self.env.ReadKinBodyXMLFile('furniture/table.kinbody.xml') fuze_bottle.kinbody.xml/
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
        glass_pose = np.array([[ 0, 0, 0, 0.9],
                              [-1, 0,  1, -0.2],
                              [ 0, 1,  0, 0.7165],
                              [ 0, 0,  0, 1]])
        self.target_kinbody1.SetTransform(glass_pose)
        self.place_on(self.target_kinbody1, self.table)

        #glass 2
        self.target_kinbody2 = self.env.ReadKinBodyURI('models/data/objects/plastic_glass.kinbody.xml')
        self.target_kinbody2.SetName("glass2")
        self.env.Add(self.target_kinbody2)
        glass_pose = np.array([[ 0, 0, 0, 0.6], 
                                  [-1, 0,  1, -0.4], 
                                  [ 0, 1,  0, 0.7165],
                                  [ 0, 0,  0, 1]])
        self.target_kinbody2.SetTransform(glass_pose)
        self.place_on(self.target_kinbody2, self.table)

        #glass 3
        self.target_kinbody3 = self.env.ReadKinBodyURI('models/data/objects/plastic_glass.kinbody.xml')
        self.target_kinbody3.SetName("glass3")
        self.env.Add(self.target_kinbody3)
        glass_pose = np.array([[ 0, 0, 0, 0.8], 
                                  [-1, 0,  1, -0.5], 
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
        #self.place_on(self.target_tray, self.table)

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
            pos[2,3] += 0.02
            obj.SetTransform(pos)
    
    def place_after(self, obj):
        pos = obj.GetTransform()
        pos[0,3] += 0.01
	pos[1,3]+= 0.01
        obj.SetTransform(pos)
