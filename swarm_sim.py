import random
import math
import numpy as np

SIZE = 10
DT = 0.1

class Sprite:
	def __init__(self, idx, pos, vel, ranges):
		self.idx = idx
		self.pos = pos
		self.vel = vel
		self.ranges = ranges

	def __repr__(self):
		return "Sprite " + str(self.idx)

	def __str__(self):
		return "Sprite " + str(self.idx)

	def update_range(self, idy, dist):
		self.ranges[idy] = dist


def swarm_measure(swarm):
	for sprite in swarm:
		ranges = np.empty(SIZE, dtype=float)
		for sprite2 in swarm:
			rel_pos = sprite2.pos - sprite.pos
			dist =  np.linalg.norm(rel_pos)
			noise = random.random()
			if sprite == sprite2:
				ranges[sprite2.idx] = 0
			else:
				ranges[sprite2.idx] = dist + noise
		sprite.ranges = ranges

def swarm_move(swarm, dt):
	for sprite in swarm:
		sprite.pos = sprite.pos + sprite.vel*dt
							


if __name__ == '__main__':
	
	# Generate random swarm in 10m radius
	swarm = []
	for i in range(0, SIZE):
		pos = 10*np.array([random.random(), random.random(), random.random()])
		vel = 2*np.array([random.random()-0.5, random.random()-0.5, random.random()-0.5])
		swarm.append(Sprite(i, pos, vel, np.array([])))
	swarm_measure(swarm)
	for sprite in swarm:
		print sprite.ranges
	swarm_move(swarm, DT)
	swarm_measure(swarm)
	for sprite in swarm:
		print sprite.ranges
	
		

