#!/usr/bin/env python
import herbpy
import numpy as np
from HerbEnv import HerbEnv
from Planner import *
import openravepy
import time

def main():
	env, robot = herbpy.initialize(sim=True)
	#robot.right_arm.SetActive()
	robot.SetActiveManipulator(robot.right_arm)
	#import IPython
	#IPython.embed()
	env.SetViewer('qtcoin')
	env.GetViewer().SetName('HPN Viewer')
	env.Add(robot)
	kinbody_env = HerbEnv(env,robot)

	plan = Planner(env,robot,kinbody_env)
	plan.Plan(kinbody_env.obj_list)
#	time.sleep(10000)

if __name__ == "__main__":
	main()

