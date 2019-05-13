import viz
import vizconnect

import vizproximity
import vizinfo
import viztask
import vizact

from Direction import*
from Ghost import*

viz.setMultiSample(4)

# To Turn on VR controls, uncomment this line below
#vizconnect.go('vizconnect_config.py')

# Add another view
subView = viz.addView()
subView.setPosition([0,45,0])
subView.setEuler([0,90,0])
# Add a new window.
subWindow = viz.addWindow()
#Set the size and position of the window.
subWindow.setSize([0.5,0.5])
subWindow.fov(40)
subWindow.setPosition([0,1])

#Assign the new view to the new window.
subWindow.setView( subView )

# Add collision
viz.MainView.collision(viz.ON)
viz.MainView.collisionBuffer(0.3)
# add the map
maze = viz.addChild('pac.dae')

# Add the path of the map
path1 = Direction(0.2434, 2.8173, True, True, False, False)
path2 = Direction(-2.7133, 2.8751, False, True, False, True)
path3 = Direction(-2.7133, 0.2607, True, False, True, True)
path4 = Direction(-2.7133, -2.1671, False, True, True, True)
path5 = Direction(-2.7133, -4.7065, True, True, True, False)
path6 = Direction(-0.922, -4.7065, True, False, False, True)
path7 = Direction(-0.932, -7.2322, True, True, True, False)
path8 = Direction(-3.1291, -7.2322, True, True, False, True)
path9 = Direction(-5.4851, -7.2221, False, True, True, True)
path10 = Direction(-5.4851, -10.01, True, False, True, False)
path11 = Direction(-8.4062, -10.01, True, True, True, False)
path12 = Direction(-8.3254, -6.9047, True, False, False, True)
path13 = Direction(-9.9111, -6.9272, False, True, True, False)
path14 = Direction(-9.9211, -4.7065, False, True, False, True)
path15 = Direction(-5.4851, -4.7065, True, True, True, True)
path16 = Direction(-5.4851,  0.2607, False, True, True, True)
path17 = Direction(-5.4851, 4.4012,  True, False, True, True)
path18 = Direction(-10.0146, 4.4012, False, True, True, False)
path19 = Direction(-10.0146, 7.7492, False, True, True, True)
path20 = Direction(-10.0146, 11.4527, False, True, False, True)
path21 = Direction(-5.4851, 11.4527, True, True, False, True)
path22 = Direction(-0.87, 11.4527, True, False, False, True)
path23 = Direction(-0.87, 7.7492, True, True, True, False)
path24 = Direction(1.6622, 7.7492, True, True, True, False)
path25 = Direction(1.6622, 11.4527, False, True, False, True)
path26 = Direction(6.3989, 11.4527, True, True, False, True)
path27 = Direction(11.5045, 11.4527, True, False, False, True)
path28 = Direction(11.5045, 7.7492, True, False, True, True)
path29 = Direction(11.5045, 4.8434, True, False, True, False)
path30 = Direction(6.3989, 4.8434, False, True, True, True)
path31 = Direction(6.3989, 7.7492, True, True, True, True)
path32 = Direction(3.8302, 7.7492, True, True, False, True)
path33 = Direction(3.8302, 5.2223, True, False, True, False)
path34 = Direction(1.6622, 5.2223, False, True, False, True)
path35 = Direction(1.6622, 2.8751, True, True, True, False)
path36 = Direction(-1.0937, 2.8751, True, True, True, False)
path37 = Direction(-1.0937, 4.8444, True, False, False, True)
path38 = Direction(-2.9353, 4.8444, False, True, True, False)
path39 = Direction(-2.9353, 7.7492, True, True, False, True)
path40 = Direction(-5.4851, 7.7492, True, True, True, True)
path41 = Direction(3.7092, 2.9337, True, False, False, True)
path42 = Direction(3.7092, 0.299, False, True, True, True)
path43 = Direction(6.3989, 0.299, False, True, True, True)
path44 = Direction(6.3989, -4.8820, True, True, True, True)
path45 = Direction(11.5045, -4.8820, True, False, False, True)
path46 = Direction(11.5045, -7.4158, True, False, True, False)
path47 = Direction(9.5077, -7.4158, False, True, False, True)
path48 = Direction(9.5077, -10.01, True, True, True, False)
path49 = Direction(11.2715, -10.01, True, False, False, True)
path50 = Direction(11.2715, -12.4145, True, False, True, False)
path51 = Direction(1.6333, -12.4145, True, True, True, False)
path52 = Direction(1.6333, -10.01, False, True, False, True)
path53 = Direction(4.2588, -10.01, True, False, True, False)
path54 = Direction(4.2588, -7.1979, True, True, False, True)
path55 = Direction(1.6333, -7.1979, True, True, True, False)
path56 = Direction(1.6333, -4.8820, False, True, False, True)
path57 = Direction(3.7124, -4.8820, True, True, True, False)
path58 = Direction(3.7124, -2.1671, True, False, True, True)
path59 = Direction(6.3989, -10.01, False, True, True, False)
path60 = Direction(6.3989, -7.1979, True, False, True, True)
path61 = Direction(-3.1291, -10.01, False, True, True, False)
path62 = Direction(-0.932, -10.01, True, False, False, True)
path63 = Direction(-0.932, -12.4145, True, True, True, False)
path64 = Direction(-9.9111, -12.4145, False, True, True, False)

path65 = Direction(-9.9111, -10.01, False, True, False, True)
#path66 = Direction(6.3989, -7.1979, True, False,True, True)

g = Ghost(3.7092, 2.8173, True, False, False, False)

#viz.phys.enable()True, False,True, True

#Sensor test
#Add main viewpoint as proximity target
target = vizproximity.Target(g.box)
#Create proximity manager
manager = vizproximity.Manager()
#Add target to manager
manager.addTarget(g.box)
#Add paths sensors to manager
manager.addSensor(path1.sensor)
manager.addSensor(path2.sensor)
manager.addSensor(path3.sensor)
manager.addSensor(path4.sensor)
manager.addSensor(path5.sensor)
manager.addSensor(path6.sensor)
manager.addSensor(path7.sensor)
manager.addSensor(path8.sensor)
manager.addSensor(path9.sensor)
manager.addSensor(path10.sensor)
manager.addSensor(path11.sensor)
manager.addSensor(path12.sensor)
manager.addSensor(path13.sensor)
manager.addSensor(path14.sensor)
manager.addSensor(path15.sensor)
manager.addSensor(path16.sensor)
manager.addSensor(path17.sensor)
manager.addSensor(path18.sensor)
manager.addSensor(path19.sensor)
manager.addSensor(path20.sensor)
manager.addSensor(path21.sensor)
manager.addSensor(path22.sensor)
manager.addSensor(path23.sensor)
manager.addSensor(path24.sensor)
manager.addSensor(path25.sensor)
manager.addSensor(path26.sensor)
manager.addSensor(path27.sensor)
manager.addSensor(path28.sensor)
manager.addSensor(path29.sensor)
manager.addSensor(path30.sensor)
manager.addSensor(path31.sensor)
manager.addSensor(path32.sensor)
manager.addSensor(path33.sensor)
manager.addSensor(path34.sensor)
manager.addSensor(path35.sensor)
manager.addSensor(path36.sensor)
manager.addSensor(path37.sensor)
manager.addSensor(path38.sensor)
manager.addSensor(path39.sensor)
manager.addSensor(path40.sensor)
manager.addSensor(path41.sensor)
manager.addSensor(path42.sensor)
manager.addSensor(path43.sensor)
manager.addSensor(path44.sensor)
manager.addSensor(path45.sensor)
manager.addSensor(path46.sensor)
manager.addSensor(path47.sensor)
manager.addSensor(path48.sensor)
manager.addSensor(path49.sensor)
manager.addSensor(path50.sensor)
manager.addSensor(path51.sensor)
manager.addSensor(path52.sensor)
manager.addSensor(path53.sensor)
manager.addSensor(path54.sensor)
manager.addSensor(path55.sensor)
manager.addSensor(path56.sensor)
manager.addSensor(path57.sensor)
manager.addSensor(path58.sensor)
manager.addSensor(path59.sensor)
manager.addSensor(path60.sensor)
manager.addSensor(path61.sensor)
manager.addSensor(path62.sensor)
manager.addSensor(path63.sensor)
manager.addSensor(path64.sensor)
manager.addSensor(path65.sensor)

#Toggle debug shapes with keypress
vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

def EnterProximity(e):
	if e.sensor == path1.sensor:
		print('sensor 1 working')
		g.ChangeDirection(True, True, False, False)
	if e.sensor == path2.sensor:
		print('sensor 2 working')
		g.ChangeDirection(False, True, False, True)
	if e.sensor == path3.sensor:
		print('sensor 3 working')
		g.ChangeDirection(True, False, True, True)
		
	if e.sensor == path4.sensor:
		print('sensor 4 working')
		g.ChangeDirection(False, True, True, True)
	if e.sensor == path5.sensor:
		print('sensor 5 working')
		g.ChangeDirection(True, True, True, False)
	if e.sensor == path6.sensor:
		print('sensor 6 working')
		g.ChangeDirection(True, False, False, True)
		
	if e.sensor == path7.sensor:
		print('sensor 7 working')
		g.ChangeDirection(True, True, True, False)
	if e.sensor == path8.sensor:
		print('sensor 8 working')
		g.ChangeDirection(True, True, False, True)
	if e.sensor == path9.sensor:
		print('sensor 9 working')
		g.ChangeDirection(False, True, True, True)
		
	if e.sensor == path10.sensor:
		print('sensor 10 working')
		g.ChangeDirection(True, False, True, False)
	if e.sensor == path11.sensor:
		print('sensor 11 working')
		g.ChangeDirection(True, True, True, False)
	if e.sensor == path12.sensor:
		print('sensor 12 working')
		g.ChangeDirection(True, False, False, True)
		
	if e.sensor == path13.sensor:
		print('sensor 13 working')
		g.ChangeDirection(False, True, True, False)
	if e.sensor == path14.sensor:
		print('sensor 14 working')
		g.ChangeDirection(False, True, False, True)
	if e.sensor == path15.sensor:
		print('sensor 15 working')
		g.ChangeDirection(True, True, True, True)
		
	if e.sensor == path16.sensor:
		print('sensor 16 working')
		g.ChangeDirection(False, True, True, True)
	if e.sensor == path17.sensor:
		print('sensor 17 working')
		g.ChangeDirection(True, False, True, True)
	if e.sensor == path18.sensor:
		print('sensor 18 working')
		g.ChangeDirection(False, True, True, False)
		
	if e.sensor == path19.sensor:
		print('sensor 19 working')
		g.ChangeDirection(False, True, True, True)
	if e.sensor == path20.sensor:
		print('sensor 20 working')
		g.ChangeDirection(False, True, False, True)
	if e.sensor == path21.sensor:
		print('sensor 21 working')
		g.ChangeDirection(True, True, False, True)	
		
	if e.sensor == path22.sensor:
		print('sensor 22 working')
		g.ChangeDirection(True, False, False, True)
	if e.sensor == path23.sensor:
		print('sensor 23 working')
		g.ChangeDirection(True, True, True, False)
	if e.sensor == path24.sensor:
		print('sensor 24 working')
		g.ChangeDirection(True, True, True, False)	
		
	if e.sensor == path25.sensor:
		print('sensor 25 working')
		g.ChangeDirection(False, True, False, True)
	if e.sensor == path26.sensor:
		print('sensor 26 working')
		g.ChangeDirection(True, True, False, True)
	if e.sensor == path27.sensor:
		print('sensor 27 working')
		g.ChangeDirection(True, False, False, True)	
	
	if e.sensor == path28.sensor:
		print('sensor 28 working')
		g.ChangeDirection( True, False, True, True)
	if e.sensor == path29.sensor:
		print('sensor 29 working')
		g.ChangeDirection(True, False, True, False)
	if e.sensor == path30.sensor:
		print('sensor 30 working')
		g.ChangeDirection(False, True, True, True)	
		
	if e.sensor == path31.sensor:
		print('sensor 31 working')
		g.ChangeDirection( True, True, True, True)
	if e.sensor == path32.sensor:
		print('sensor 32 working')
		g.ChangeDirection(True, True, False, True)
	if e.sensor == path33.sensor:
		print('sensor 33 working')
		g.ChangeDirection(True, False, True, False)	
		
	if e.sensor == path34.sensor:
		print('sensor 34 working')
		g.ChangeDirection( False, True, False, True)
	if e.sensor == path35.sensor:
		print('sensor 35 working')
		g.ChangeDirection(True, True, True, False)
	if e.sensor == path36.sensor:
		print('sensor 36 working')
		g.ChangeDirection(True, True, True, False)
		
	if e.sensor == path37.sensor:
		print('sensor 37 working')
		g.ChangeDirection( True, False, False, True)
	if e.sensor == path38.sensor:
		print('sensor 38 working')
		g.ChangeDirection(False, True, True, False)
	if e.sensor == path39.sensor:
		print('sensor 39 working')
		g.ChangeDirection(True, True, False, True)	
		
	if e.sensor == path40.sensor:
		print('sensor 40 working')
		g.ChangeDirection( True, True, True, True)
	if e.sensor == path41.sensor:
		print('sensor 41 working')
		g.ChangeDirection(True, False, False, True)
	if e.sensor == path42.sensor:
		print('sensor 42 working')
		g.ChangeDirection(False, True, True, True)	
		
	if e.sensor == path43.sensor:
		print('sensor 43 working')
		g.ChangeDirection( True, False, True, True)
	if e.sensor == path44.sensor:
		print('sensor 44 working')
		g.ChangeDirection(True, True, True, True)
	if e.sensor == path45.sensor:
		print('sensor 45 working')
		g.ChangeDirection(True, False, False, True)	
		
	if e.sensor == path46.sensor:
		print('sensor 46 working')
		g.ChangeDirection(True, False, True, False)
	if e.sensor == path47.sensor:
		print('sensor 47 working')
		g.ChangeDirection(False, True, False, True)
	if e.sensor == path48.sensor:
		print('sensor 48 working')
		g.ChangeDirection(True, True, True, False)	
		
	if e.sensor == path49.sensor:
		print('sensor 49 working')
		g.ChangeDirection(True, False, False, True)
	if e.sensor == path50.sensor:
		print('sensor 50 working')
		g.ChangeDirection(True, False, True, False)
	if e.sensor == path51.sensor:
		print('sensor 51 working')
		g.ChangeDirection(True, True, True, False)	
		
	if e.sensor == path52.sensor:
		print('sensor 52 working')
		g.ChangeDirection(False, True, False, True)
	if e.sensor == path53.sensor:
		print('sensor 53 working')
		g.ChangeDirection(True, False, True, False)
	if e.sensor == path54.sensor:
		print('sensor 54 working')
		g.ChangeDirection(True, True, False, True)	
		
	if e.sensor == path55.sensor:
		print('sensor 55 working')
		g.ChangeDirection(True, True, True, False)
	if e.sensor == path56.sensor:
		print('sensor 56 working')
		g.ChangeDirection(False, True, False, True)
	if e.sensor == path57.sensor:
		print('sensor 57 working')
		g.ChangeDirection( True, True, True, False)	
		
	if e.sensor == path58.sensor:
		print('sensor 58 working')
		g.ChangeDirection(True, False, True, True)
	if e.sensor == path59.sensor:
		print('sensor 59 working')
		g.ChangeDirection(False, True, True, False)
	if e.sensor == path60.sensor:
		print('sensor 60 working')
		g.ChangeDirection(True, False, True, True)
		
	if e.sensor == path61.sensor:
		print('sensor 61 working')
		g.ChangeDirection(False, True, True, False)
	if e.sensor == path62.sensor:
		print('sensor 62 working')
		g.ChangeDirection(True, False, False, True)
	if e.sensor == path63.sensor:
		print('sensor 63 working')
		g.ChangeDirection(True, True, True, False)
		
	if e.sensor == path64.sensor:
		print('sensor 64 working')
		g.ChangeDirection(False, True, True, False)
	if e.sensor == path65.sensor:
		print('sensor 65 working')
		g.ChangeDirection(False, True, False, True)
	
manager.onEnter(None, EnterProximity)

#Without vr
viz.go()
