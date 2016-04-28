#!/usr/bin/env python
import herbpy
import numpy as np
from HerbEnv import HerbEnv
from Planner import *

#env, robot = herbpy.initialize(sim=True)
#robot.PlanToNamedConfiguration('home', execute = True)

def main():
	env, robot = herbpy.initialize(sim=True, attach_viewer='interactivemarker')
	kinbody_env = HerbEnv(env,robot)
	import IPython
	IPython.embed()

	plan = Planner(env,robot,kinbody_env)
	plan.Plan(kinbody_env.obj_list)
#	time.sleep(10000)

if __name__ == "__main__":

	main()
