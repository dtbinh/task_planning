#!/usr/bin/env python
import herbpy
import numpy as np
from HerbEnv import HerbEnv
from Planner import *
import openravepy
import time

def main():
	sim = True	
	env, robot = herbpy.initialize(sim=sim,segway_sim=True)
	#robot.right_arm.SetActive()
	robot.head.SetStiffness(1)
	robot.head.MoveTo([0,-0.4])
	robot.SetActiveManipulator(robot.right_arm)
	env.SetViewer('qtcoin')
	env.GetViewer().SetName('HPN Viewer')
	env.Add(robot)
	kinbody_env = HerbEnv(env,robot,sim)
	
	import IPython
	IPython.embed()
	plan = Planner(env,robot,kinbody_env)
	plan.Plan(kinbody_env.obj_list)
#	time.sleep(10000)

if __name__ == "__main__":
	main()

