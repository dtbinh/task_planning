#!/usr/bin/env python
import task_planning
import herbpy
from HerbEnv import HerbEnv
from Planner import *

#env, robot = herbpy.initialize(sim=True)
#robot.PlanToNamedConfiguration(home, execute = True)

def main():
	#import IPython
	#IPython.embed()

	planning_env = HerbEnv()
	obj_list = planning_env.obj_list

	import IPython
	IPython.embed()

	plan = Planner(planning_env,obj_list)
	plan.Plan(obj_list)
	time.sleep(10000)

    #traj = robot.ConvertPlanToTrajectory(plan)
    #robot.ExecuteTrajectory(traj)    

if __name__ == "__main__":
	main()