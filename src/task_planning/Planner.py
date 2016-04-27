#!/usr/bin/env python

from collections import deque
from Fluents import Fluents
from Operators import Operators
#from herbpy import *

class Planner(object):

    print "INSIDE PLANNER"
    def __init__(self, planning_env,object_list):
        self.planning_env = planning_env
        self.list = object_list
        print "obj list" + str(object_list)

    def Plan(self,object_list):
    	
        goal_loc= self.planning_env.target_tray.GetTransform()
        print "goal:" + str(goal_loc)
        
        while(self.list):
            start_loc_box = self.planning_env.bounding_box(self.list[1])
            goal_loc_box = self.planning_env.bounding_box(self.planning_env.target_tray)
            
            op = Operators(self.list[1],self.planning_env)
            op.Pick(self.list[1], start_loc_box)
            #op.Place(self.list[i], goal_loc)

            '''if op.Pick(self.list[i], start_loc) == True:
                op.Place(self.list[i],self.planning_env.target_tray)
                del self.list[i]
            else: 
                i = i+1
            '''


        '''while(self.list):
            for i in range(len(self.list)-1):
                
                start_loc_box = self.planning_env.bounding_box(self.list[i])
                goal_loc_box = self.planning_env.bounding_box(self.planning_env.target_tray)
               
                op = Operators(self.list[0],self.planning_env)
                op.Pick(self.list[i], start_loc_box)
                #op.Place(self.list[i], goal_loc)

                if op.Pick(self.list[i], start_loc) == True:
                    op.Place(self.list[i],goal_loc)
                    del self.list[i]
                else: 
                    i = i+1
        '''

print "End of planner"


'''def main():
    robotEnv = HerbEnv()
    obj_list = robotEnv.obj_list
    plan = Planner(robotEnv,obj_list)
    plan.Plan(obj_list)
    print "**************HERB***********************"
    time.sleep(10000)

if __name__ == '__main__':
    main()   
'''