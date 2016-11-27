# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:55:57 2016

@author: Adrien
"""

import environment as env
import agent


world = env.Environment(10,10)
agent = agent.Agent(world)
print(world)
print(agent)


