#!/usr/bin/env python
import time
import numpy as np

''' so we have following fluents: In, Overlaps, min_dist, ClearX, Holding
'''

print "INSIDE FLUENTS"

class Fluents(object):

    def __init__(self,env,robot,kinbody_env):
        self.env = env
        self.robot = robot
        self.kinbody_env = kinbody_env

    def In(self,objname,region):
        bound_obj=self.kinbody_env.bounding_box(objname)

        if (bound_obj[0] >= region[0]) and (bound_obj[3]<= region[3]) and (bound_obj[1]>= region[1]) and (bound_obj[4] <= region[4]):
        #if (region[0][3] >= bound_obj[0]) and (region[0][3]<= bound_obj[1]) and (region[1][3] >= bound_obj[2]) and (region[1][3]<= bound_obj[3]) and (region[2][3] >= bound_obj[4]) and (region[2][3]<= bound_obj[5]):  
            print objname.GetName() + " is in"
            return True
        print objname.GetName() + " Object not in "
        return False

    def Overlaps(self,objname):
        obj_pos=[]
        sum_list=[]
        n_dims=[3,len(self.kinbody_env.obj_list)]

        dist_list=0
        for n in n_dims:
            dist_list = [dist_list] * n
        obj_ind=self.kinbody_env.obj_list.index(objname)
        for obj in self.kinbody_env.obj_list:
            obj_pos.append(obj.GetTransform()[:3,3])
        obj_pos=np.array(obj_pos)
        #print "obj_pos"+str(obj_pos)
        for i,item_i in enumerate(obj_pos):
            for j,item_j in enumerate(obj_pos):
                dist_list[i][j]=np.linalg.norm(item_j-item_i)
            print dist_list    
            sum_list.append(dist_list[i])
        #print sum_list    
        max_ind=sum_list.index(max(sum_list))
        if obj_ind==max_ind:
           print "object not overlapped is ", objname.GetName()
           return False
        else:
            print "object overlapped is ", objname.GetName()
            return True


    def min_dist(self,objname):
        robot_pose=self.robot.GetTransform()[:3,3]
        dist_list=[]
        obj_ind=self.kinbody_env.obj_list.index(objname)
        for obj in self.kinbody_env.obj_list:
            obj_pos=obj.GetTransform()[:3,3]
            dist_list.append(np.linalg.norm(robot_pose-obj_pos))
        min_ind=dist_list.index(min(dist_list))
        if obj_ind==min_ind:
           print "object at min dist from robot is ", objname.GetName()
           return True
        else:
            print "object not at min dist is ", objname.GetName()
            return False


    def ClearX(self,obj_list):
        check_non=0
        check_req=0
        non_obj=[]
        for req_obj in obj_list:
            for obj in self.kinbody_env.obj_list:
                if obj not in obj_list:
                    non_obj.append(obj)
                    if self.Overlaps(obj)==True: #can be changed with min_dist()
                        check_non+=1
            if check_non==len(non_obj):
                check_req+=1
        if check_req==len(obj_list):
            print "its clear"
            return True
        else:
            print "not clear"
            return False


    def Holding(self):
        for b in self.env.GetBodies():
            if self.robot.IsGrabbing(b):
                print "holding ", b.GetName()
                return b
        print "holding nothing"
        return None
