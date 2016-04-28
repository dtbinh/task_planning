#!/usr/bin/env python
import task_planning
import herbpy
from task_planning.HerbEnv import HerbEnv
from task_planning.Planner import *

#env, robot = herbpy.initialize(sim=True)
#robot.PlanToNamedConfiguration(home, execute = True)

def main():
	#import IPython
	#IPython.embed()
        env, robot = herbpy.initialize(sim=True, attach_viewer='interactivemarker')

	planning_env = HerbEnv(env, robot)
	obj_list = planning_env.obj_list

	import IPython
	IPython.embed()

	plan = Planner(env, robot, planning_env)
	plan.Plan(obj_list)
	time.sleep(10000)

    #traj = robot.ConvertPlanToTrajectory(plan)
    #robot.ExecuteTrajectory(traj)    

if __name__ == "__main__":
	main()
