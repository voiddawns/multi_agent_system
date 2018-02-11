#!/usr/bin/python3

import visual
import threading

def visual_init(window_x=800, window_y=600):
	entities = visual.init(window_x, window_y)
	visual_thread = threading.Thread(target = visual.run)
	visual_thread.start()

	# entities.append(visual.entity(300, 300,		'agent1.bmp'))
	# entities.append(visual.entity(300, 300, 	'agent1.bmp'))
	# entities.append(visual.entity(300, 300, 	'agent1.bmp'))
	# entities.append(visual.entity(300, 300, 	'agent1.bmp'))
	# for i in range(1000):
	# 	entities[0].go_right()
	# 	entities[1].go_left()
	# 	entities[2].go_up()
	# 	entities[3].go_down()
	
	return entities


class agent(object):
	def __init__(self, x_pos=0, y_pos=0, agent_type='imuno'):
		self.x = x_pos
		self.y = y_pos
		self.type = agent_type

	def think(self):
		print('think')

	def body_acquirment(self):
		global entities
		entities.append(visual.entity(0, 0, 'agent1.bmp'))
		self․body = entities[-1]


class world(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	





if __name__ == '__main__':
	visual_init(600, 600)
	a = agent()
