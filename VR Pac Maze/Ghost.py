import viz
import vizshape
import vizconnect
import random

class Ghost(viz.EventClass):
	# Parameters
	x = 0
	z = 0
		
	left = False
	right = False
	up = False
	down = False
		
	def __init__(self, x, z, left, right, up, down):
		viz.EventClass.__init__(self)
		
		# Start timer event for movement
		self.callback(viz.TIMER_EVENT, self.onTimer)
		
		# Position of change in path
		self.x = x
		self.z = z
		self.y = 0.7
		
		# What paths can be taken
		self.left = left
		self.right = right
		self.up = up
		self.down = down
		
		# Make the collision box at disired position
		self.box = vizshape.addBox(size=[1,1.5,1], color=[1,1,0])
		mat = viz.Matrix()
		mat.postTrans(self.x,self.y,self.z)
		self.box.setMatrix(mat)
		#self.box.collideMesh()
		#self.box.enable(viz.COLLIDE_NOTIFY)
		
		# Specify callback method for collision]
#		self.callback(viz.COLLIDE_BEGIN_EVENT, self.onCollideBegin)
#		self.callback(viz.COLLIDE_END_EVENT, self.onCollideEnd)
		
		# Start Timer
		self.starttimer(1, 1/25.0, viz.FOREVER)
		
	def onTimer(self,num):
		if self.left:
			self.x = self.x-.1
		elif self.right:
			self.x = self.x+.1
		elif self.up:
			self.z = self.z+.1
		elif self.down:
			self.z = self.z-.1
		mat = viz.Matrix()
		#mat.postTrans(viz.MainView.getPosition(0), -1.0, viz.MainView.getPosition(2))
		mat.setPosition([self.x, self.y, self.z])
		self.box.setMatrix(mat)	
		
	def ChangeDirection(self, left, right, up, down):
		directions = []
		#establish possible paths depending on physical path and ghost's current direction
		#if you can turn to a left pathway
		if left == True:
			#and ghost isn't coming from the left pathway by going right
			if (self.right == False):
				directions.append('left')
		if right == True:
			if (self.left == False):
				directions.append('right')
		if up == True:
			if (self.down == False):
				directions.append('up')
		if down == True:
			if (self.up == False):
				directions.append('down')
		# Randomly pick availible directions
		direction = random.choice(directions)
		print(direction)
		
		#check what is picked
		if direction == 'left':
			self.left = True
			self.right = False
			self.up = False
			self.down = False
		elif direction == 'right':
			self.left = False
			self.right = True
			self.up = False
			self.down = False
		elif direction == 'up':
			self.left = False
			self.right = False
			self.up = True
			self.down = False
		elif direction == 'down':
			self.left = False
			self.right = False
			self.up = False
			self.down = True