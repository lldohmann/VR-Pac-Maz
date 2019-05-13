import viz
import vizshape
import vizconnect

import vizproximity
import vizinfo
import viztask
import vizact

class Direction(viz.EventClass):
	# Parameters
	x = 0
	z = 0
		
	left = False
	right = False
	up = False
	down = False
		
	def __init__(self, x, z, left, right, up, down):
		viz.EventClass.__init__(self)
		
		# Position of change in path
		self.x = x
		self.z = z
		self.y = 0.5
		
		# What paths can be taken
		self.left = left
		self.right = right
		self.up = up
		self.down = down

		# Create sensors for paths
		self.sensor = vizproximity.Sensor(vizproximity.Box([.5,.5,.5], center=[0,0,0]),source=viz.Matrix.translate(self.x,self.y,self.z))
		
	def onCollideBegin(self,e):
		print('collision beinging detected')
		
	def onCollideEnd(self,e):
		print('collision ending detected')
		