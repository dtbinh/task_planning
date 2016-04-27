#!/usr/bin/env python
import task_planning
import herbpy
from HerbEnv import HerbEnv
from Planner import *


#robot.PlanToNamedConfiguration(home, execute = True)

def main():
	#import IPython
	#IPython.embed()
	#env, robot = herbpy.initialize(sim=True)
	planning_env = HerbEnv()
	obj_list = planning_env.obj_list

	plan = Planner(planning_env,obj_list)
	plan.Plan(obj_list)
	time.sleep(10000)

    #traj = robot.ConvertPlanToTrajectory(plan)
    #robot.ExecuteTrajectory(traj)    

if __name__ == "__main__":

	main()   
    