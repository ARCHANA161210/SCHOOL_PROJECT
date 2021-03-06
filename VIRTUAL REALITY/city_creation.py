﻿import viz
import vizact
import vizfx
import vizcam
import vizinfo
import time
import vizdlg
import viztask

viz.setMultiSample(16)
viz.fov(60)
viz.go()
viz.clearcolor(viz.SKYBLUE)


view = viz.MainView

viz.MainView.move([-30,4,-40])
viz.MainView.setEuler([0,0,0])
viz.MainView.gravity(0.0) 

#road between two fire 
fire1=viz.addChild('fire2.dae')
fire1.setPosition(40,15,05)
fire1.setScale(.5,.5,.5)

fire2=viz.addChild('fire2.dae')
fire2.setPosition(45,25,60)
fire2.setScale(.5,.5,.5)

#black building
fire3=viz.addChild('fire2.dae')
fire3.setPosition(-150,18,50)
fire3.setScale(.5,.5,.5)

#TOWN = viz.addChild('circle_PARK.dae')
ground = viz.addChild('GROUND.osgb')
ground.setPosition(0,0,0)
'''
home=viz.addChild('home.dae')
home.setPosition(3,0,-40)
home.setScale(0.6,0.6,0.6)
home.setEuler(90,0,0)
'''
grass=viz.addChild('ground_grass.osgb')
grass.setScale([20,2,20])
grass.setPosition(0,0.01,0)
ground.setScale(5,5,5)
#TOWN.setPosition(0,0.5,0)
#TOWN.setScale(0.8,0.8,0.8)
####################################################################
choices = ['Hostile Agent','Non-Hostile Agent','Selfish-Agent','Goal-Following Agent','Leader Following Agent','Fuzzy-Behaviour Agent']
dialog = vizdlg.ChooseDialog(prompt='Select The Agent Type:', choices=choices)
dialog.setScreenAlignment(viz.ALIGN_CENTER)

Numbers = ['1','2','3','4','5','6','7','8','9','10']
how_many = vizdlg.ChooseDialog(prompt='Select The Number of Agents', choices=Numbers)
how_many.setScreenAlignment(viz.ALIGN_CENTER)






############################add avatars####################################

male11=viz.addAvatar('vcc_male2.cfg', pos=(50,0,56), euler=(270,0,0) )
male11.setScale(2,1.8,2)
male11.state(2)

#in the corner where there is no signal light
male1=viz.addAvatar('vcc_male2.cfg', pos=(5.5,0,115), euler=(270,0,0) )
male1.setScale(2,1.8,2)
male1.state(4)

male2=viz.addAvatar('vcc_male_blue.osgb', pos=(4,0,113), euler=(0,0,0) )
male2.setScale(2,1.8,2)
male2.state(4)


#NEAR THE TRASHCANE three people
female1=viz.addAvatar('vcc_female_white.osgb', pos=(4,0,76), euler=(90,0,0) )
female1.setScale(2,1.8,2)
female1.state(14)

male3=viz.addAvatar('vcc_male_blue.osgb', pos=(6,0,75), euler=(270,0,0) )
male3.setScale(2,1.8,2)
male3.state(4)

male40=viz.addAvatar('vcc_male.cfg', pos=(5,0,74), euler=(0,0,0) )
male40.setScale(2,1.8,2)
male40.state(1)

male4=viz.addAvatar('vcc_male.cfg', pos=(-5,0,113), euler=(180,0,0) )
male4.setScale(2,1.8,2)
male4.state(1)

#center of the park dancing guys
male5=viz.addAvatar('vcc_male_blue.osgb', pos=(-15.5,0,96), euler=(130,0,0) )
male5.setScale(2,1.8,2)
male5.state(5)

male8=viz.addAvatar('vcc_male2.cfg', pos=(-25,0,96), euler=(160,0,0) )
male8.setScale(2,1.8,2)
male8.state(5)

#near boarder of signal light two people in original avtars
female2=viz.addAvatar('vcc_female.cfg', pos=(-49,0,72), euler=(90,0,0) )
female2.setScale(2,1.9,2)
female2.state(14)

male6=viz.addAvatar('vcc_male2.cfg', pos=(-45,0,73), euler=(270,0,0) )
male6.setScale(2,1.9,2)
male6.state(4)

#NEAR the tree red and pink couple
female3=viz.addAvatar('vcc_female_red.osgb', pos=(-40,0,82), euler=(90,0,0) )
female3.setScale(2,1.9,2)
female3.state(14)

male7=viz.addAvatar('vcc_male_white.osgb', pos=(-37,0,83), euler=(270,0,0) )
male7.setScale(2,1.9,2)
male7.state(4)

#near to trash and bench sitted guy
male1=viz.addAvatar('vcc_male2.cfg', pos=(-49,0,132), euler=(200,0,0) )
male1.setScale(2,1.9,2)
male1.state(6)

male2=viz.addAvatar('vcc_male2_red.osgb', pos=(-32,0,133), euler=(40,0,0) )
male2.setScale(2,1.9,2)
male2.state(5)

trash= viz.addChild('trash.dae')
trash.setScale(1,1,1)
trash.setPosition(-44,0,130)
trash.setEuler(170,0,0)

bench5= viz.addChild('bench.dae')
bench5.setScale(2.5,2.0,2.5)
bench5.setPosition(-51,0,133)
bench5.setEuler(0,0,0)

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################


#red male

#male face
myface1 = viz.add('morph_head.vzf')
myface1.setScale(2.5,1.8,2.5)
myface1.visible(viz.OFF)
#female face
myface2 = viz.add('biohead_all_morph.vzf') 
myface2.setScale(2,1.8,2)
myface2.visible(viz.OFF)

#Add two different face images. 
first_texture = viz.addTexture('stan.jpg')
second_texture = viz.addTexture('ollie.jpg')

#Paste both face images onto the head.
myface1.texture(first_texture)
myface1.texture(second_texture, '', 1)

#Use a fragment program to blend the textures.
blend = viz.addFragmentProgram('multitexblend.fp')
myface1.apply(blend)
blend.param(0,0)


red_female1=viz.addAvatar('vcc_female_red.osgb', pos=(-22.5,0,-16), euler=(90,0,0) )
red_female1.setScale(2,1.8,2)
red_female1.state(6)
red_female1.visible(viz.OFF)

red_female2=viz.addAvatar('vcc_female_red.osgb', pos=(4,0,8), euler=(270,0,0) )
red_female2.setScale(2,1.8,2)
red_female2.state(6)
red_female2.visible(viz.OFF)

red_female3=viz.addAvatar('vcc_female_red.osgb', pos=(-20,0,-16), euler=(270,0,0) )
red_female3.setScale(2,1.8,2)
red_female3.state(6)
red_female3.setFace(myface2)
red_female3.visible(viz.OFF)

red_female4=viz.addAvatar('vcc_female_red.osgb', pos=(-52.5,0,-16), euler=(90,0,0) )
red_female4.setScale(2,1.8,2)
red_female4.state(6)
red_female4.visible(viz.OFF)

red_female5=viz.addAvatar('vcc_female_red.osgb', pos=(-50.5,0,-16), euler=(270,0,0) )
red_female5.setScale(2,1.8,2)
red_female5.state(6)
red_female5.visible(viz.OFF)

red_female6=viz.addAvatar('vcc_female_red.osgb', pos=(2,0,80), euler=(90,0,0) )
red_female6.setScale(2,1.8,2)
red_female6.state(6)
red_female6.visible(viz.OFF)

red_man2=viz.addAvatar('vcc_male2_red.osgb', pos=(-20,0,-14), euler=(180,0,0) )
red_man2.setScale(2,1.8,2)
red_man2.state(5)
red_man2.visible(viz.OFF)


red_man3=viz.addAvatar('vcc_male2_red.osgb', pos=(-20,0,-22), euler=(270,0,0) )
red_man3.setScale(2,1.8,2)
red_man3.state(4)
red_man3.visible(viz.OFF)
red_man3.setFace(myface1)


red_man4=viz.addAvatar('vcc_male1_red.osgb', pos=(2,0,8), euler=(90,0,0) )
red_man4.setScale(2,1.8,2)
red_man4.state(6)
red_man4.visible(viz.OFF)


red_man5=viz.addAvatar('vcc_male1_red.osgb', pos=(4,0,80), euler=(270,0,0) )
red_man5.setScale(2,1.8,2)
red_man5.state(6)
red_man5.visible(viz.OFF)



##################################################################
#blue male
blue_man2=viz.addAvatar('vcc_male_blue.osgb', pos=(4,0,15), euler=(0,0,0) )
blue_man2.setScale(2,1.8,2)
blue_man2.state(4)
blue_man2.visible(viz.OFF)


blue_man3=viz.addAvatar('vcc_male_blue.osgb', pos=(4,0,18), euler=(270,0,0) )
blue_man3.setScale(2,1.8,2)
blue_man3.state(4)
blue_man3.visible(viz.OFF)


blue_man4=viz.addAvatar('vcc_male_blue1.osgb', pos=(5,0,-22), euler=(270,0,0) )
blue_man4.setScale(2,1.8,2)
blue_man4.state(2)
blue_man4.visible(viz.OFF)



blue_man5=viz.addAvatar('vcc_male_blue1.osgb', pos=(-20,0,102), euler=(270,0,0) )
blue_man5.setScale(2,1.8,2)
blue_man5.state(2)
blue_man5.visible(viz.OFF)

blue_man6=viz.addAvatar('vcc_male_blue.osgb', pos=(-5,0,-30), euler=(270,0,0) )
blue_man6.setScale(2,1.8,2)
blue_man6.state(2)
blue_man6.visible(viz.OFF)

blue_female1=viz.addAvatar('vcc_female_blue.osgb', pos=(-15,0,-42), euler=(270,0,0) )
blue_female1.setScale(2,1.8,2)
blue_female1.state(2)
blue_female1.visible(viz.OFF)

blue_female2=viz.addAvatar('vcc_female_blue.osgb', pos=(-15,0,82), euler=(270,0,0) )
blue_female2.setScale(2,1.8,2)
blue_female2.state(2)
blue_female2.visible(viz.OFF)

blue_female3=viz.addAvatar('vcc_female_blue.osgb', pos=(-3,0,-28), euler=(270,0,0) )
blue_female3.setScale(2,1.8,2)
blue_female3.state(2)
blue_female3.visible(viz.OFF)

blue_female4=viz.addAvatar('vcc_female_blue.osgb', pos=(-25,0,120), euler=(270,0,0) )
blue_female4.setScale(2,1.8,2)
blue_female4.state(2)
blue_female4.visible(viz.OFF)


############green man#################################################################
green_man1=viz.addAvatar('vcc_male_green.osgb', pos=(-4,0,0), euler=(270,0,0) )
green_man1.setScale(2,1.8,2)
green_man1.state(4)
green_man1.visible(viz.OFF)

green_man2=viz.addAvatar('vcc_male2_green.osgb', pos=(-4,0,5), euler=(0,0,0) )
green_man2.setScale(2,1.8,2)
green_man2.state(4)
green_man2.visible(viz.OFF)

green_man3=viz.addAvatar('vcc_male_green.osgb', pos=(-6,0,-26), euler=(270,0,0) )
green_man3.setScale(2,1.8,2)
green_man3.state(4)
green_man3.visible(viz.OFF)

green_man4=viz.addAvatar('vcc_male2_green.osgb', pos=(-8,0,-15), euler=(0,0,0) )
green_man4.setScale(2,1.8,2)
green_man4.state(4)
green_man4.visible(viz.OFF)

green_man5=viz.addAvatar('vcc_male_green.osgb', pos=(-10,0,-30), euler=(270,0,0) )
green_man5.setScale(2,1.8,2)
green_man5.state(4)
green_man5.visible(viz.OFF)

green_man6=viz.addAvatar('vcc_male2_green.osgb', pos=(-40,0,-32), euler=(0,0,0) )
green_man6.setScale(2,1.8,2)
green_man6.state(4)
green_man6.visible(viz.OFF)


green_female1=viz.addAvatar('vcc_male_green.osgb', pos=(-4,0,90), euler=(270,0,0) )
green_female1.setScale(2,1.8,2)
green_female1.state(4)
green_female1.visible(viz.OFF)


green_female2=viz.addAvatar('vcc_female_green.osgb', pos=(-5,0,12), euler=(270,0,0) )
green_female2.setScale(2,1.8,2)
green_female2.state(2)
green_female2.visible(viz.OFF)

green_female3=viz.addAvatar('vcc_male_green.osgb', pos=(-40,0,118), euler=(270,0,0) )
green_female3.setScale(2,1.8,2)
green_female3.state(4)
green_female3.visible(viz.OFF)


green_female4=viz.addAvatar('vcc_female_green.osgb', pos=(-20,0,120), euler=(270,0,0) )
green_female4.setScale(2,1.8,2)
green_female4.state(2)
green_female4.visible(viz.OFF)

###########purple avtars###################################

white_female1=viz.addAvatar('vcc_female_purple.osgb', pos=(-18,0,-28), euler=(90,0,0) )
white_female1.setScale(2,1.8,2)
white_female1.state(14)
white_female1.visible(viz.OFF)

white_female2=viz.addAvatar('vcc_female_purple.osgb', pos=(-38,0,-18), euler=(90,0,0) )
white_female2.setScale(2,1.8,2)
white_female2.state(14)
white_female2.visible(viz.OFF)

white_female3=viz.addAvatar('vcc_female_purple.osgb', pos=(-28,0,-28), euler=(90,0,0) )
white_female3.setScale(2,1.8,2)
white_female3.state(14)
white_female3.visible(viz.OFF)

white_female4=viz.addAvatar('vcc_female_purple.osgb', pos=(-18,0,108), euler=(90,0,0) )
white_female4.setScale(2,1.8,2)
white_female4.state(14)
white_female4.visible(viz.OFF)

white_male1=viz.addAvatar('vcc_male1_purple.osgb', pos=(-10,0,-28), euler=(90,0,0) )
white_male1.setScale(2,1.8,2)
white_male1.state(14)
white_male1.visible(viz.OFF)


white_male2=viz.addAvatar('vcc_male2_purple.osgb', pos=(-16,0,-18), euler=(90,0,0) )
white_male2.setScale(2,1.8,2)
white_male2.state(14)
white_male2.visible(viz.OFF)

white_male3=viz.addAvatar('vcc_male1_purple.osgb', pos=(-21,0,128), euler=(90,0,0) )
white_male3.setScale(2,1.8,2)
white_male3.state(14)
white_male3.visible(viz.OFF)


white_male4=viz.addAvatar('vcc_male2_purple.osgb', pos=(-10,0,-18), euler=(90,0,0) )
white_male4.setScale(2,1.8,2)
white_male4.state(14)
white_male4.visible(viz.OFF)

white_male5=viz.addAvatar('vcc_male1_purple.osgb', pos=(-10,0,-28), euler=(90,0,0) )
white_male5.setScale(2,1.8,2)
white_male5.state(14)
white_male5.visible(viz.OFF)


white_male6=viz.addAvatar('vcc_male2_purple.osgb', pos=(-39,0,80), euler=(90,0,0) )
white_male6.setScale(2,1.8,2)
white_male6.state(14)
white_male6.visible(viz.OFF)


##############orange avtars

orange_male1=viz.addAvatar('vcc_male1_orange.osgb', pos=(-16,0,0), euler=(270,0,0) )
orange_male1.setScale(2,1.8,2)
orange_male1.state(4)
orange_male1.visible(viz.OFF)

orange_male2=viz.addAvatar('vcc_male2_orange.osgb', pos=(-36,0,5), euler=(0,0,0) )
orange_male2.setScale(2,1.8,2)
orange_male2.state(4)
orange_male2.visible(viz.OFF)

orange_male3=viz.addAvatar('vcc_male1_orange.osgb', pos=(-49,0,-32), euler=(270,0,0) )
orange_male3.setScale(2,1.8,2)
orange_male3.state(4)
orange_male3.visible(viz.OFF)

orange_male4=viz.addAvatar('vcc_male2_orange.osgb', pos=(-36,0,-35), euler=(0,0,0) )
orange_male4.setScale(2,1.8,2)
orange_male4.state(4)
orange_male4.visible(viz.OFF)

orange_male5=viz.addAvatar('vcc_male1_orange.osgb', pos=(-46,0,-10), euler=(270,0,0) )
orange_male5.setScale(2,1.8,2)
orange_male5.state(4)
orange_male5.visible(viz.OFF)

orange_male6=viz.addAvatar('vcc_male2_orange.osgb', pos=(-46,0,5), euler=(0,0,0) )
orange_male6.setScale(2,1.8,2)
orange_male6.state(4)
orange_male6.visible(viz.OFF)


orange_female1=viz.addAvatar('vcc_female_orange.osgb', pos=(-46,0,8), euler=(270,0,0) )
orange_female1.setScale(2,1.8,2)
orange_female1.state(4)
orange_female1.visible(viz.OFF)


orange_female2=viz.addAvatar('vcc_female_orange.osgb', pos=(-16,0,12), euler=(270,0,0) )
orange_female2.setScale(2,1.8,2)
orange_female2.state(2)
orange_female2.visible(viz.OFF)

orange_female3=viz.addAvatar('vcc_female_orange.osgb', pos=(-16,0,125), euler=(270,0,0) )
orange_female3.setScale(2,1.8,2)
orange_female3.state(4)
orange_female3.visible(viz.OFF)


orange_female4=viz.addAvatar('vcc_female_orange.osgb', pos=(-36,0,120), euler=(270,0,0) )
orange_female4.setScale(2,1.8,2)
orange_female4.state(2)
orange_female4.visible(viz.OFF)

####################################yellow avatars##################################

yellow_male1=viz.addAvatar('vcc_male1_yellow.osgb', pos=(-26,0,0), euler=(270,0,0) )
yellow_male1.setScale(2,1.8,2)
yellow_male1.state(4)
yellow_male1.visible(viz.OFF)

yellow_male2=viz.addAvatar('vcc_male2_yellow.osgb', pos=(-36,0,-5), euler=(0,0,0) )
yellow_male2.setScale(2,1.8,2)
yellow_male2.state(4)
yellow_male2.visible(viz.OFF)

yellow_male3=viz.addAvatar('vcc_male1_yellow.osgb', pos=(-46,0,90), euler=(270,0,0) )
yellow_male3.setScale(2,1.8,2)
yellow_male3.state(4)
yellow_male3.visible(viz.OFF)

yellow_male4=viz.addAvatar('vcc_male2_yellow.osgb', pos=(-26,0,-5), euler=(0,0,0) )
yellow_male4.setScale(2,1.8,2)
yellow_male4.state(4)
yellow_male4.visible(viz.OFF)

yellow_male5=viz.addAvatar('vcc_male1_yellow.osgb', pos=(-46,0,130), euler=(270,0,0) )
yellow_male5.setScale(2,1.8,2)
yellow_male5.state(4)
yellow_male5.visible(viz.OFF)

yellow_male6=viz.addAvatar('vcc_male2_yellow.osgb', pos=(-26,0,135), euler=(0,0,0) )
yellow_male6.setScale(2,1.8,2)
yellow_male6.state(4)
yellow_male6.visible(viz.OFF)

yellow_female1=viz.addAvatar('vcc_female_yellow.osgb', pos=(-26,0,-8), euler=(270,0,0) )
yellow_female1.setScale(2,1.8,2)
yellow_female1.state(4)
yellow_female1.visible(viz.OFF)


yellow_female2=viz.addAvatar('vcc_female_yellow.osgb', pos=(-46,0,-12), euler=(270,0,0) )
yellow_female2.setScale(2,1.8,2)
yellow_female2.state(2)
yellow_female2.visible(viz.OFF)

yellow_female3=viz.addAvatar('vcc_female_yellow.osgb', pos=(-26,0,-18), euler=(270,0,0) )
yellow_female3.setScale(2,1.8,2)
yellow_female3.state(4)
yellow_female3.visible(viz.OFF)

yellow_female4=viz.addAvatar('vcc_female_yellow.osgb', pos=(-26,0,-20), euler=(270,0,0) )
yellow_female4.setScale(2,1.8,2)
yellow_female4.state(2)
yellow_female4.visible(viz.OFF)

########add sun and sky##############################
sky=viz.addChild('sky_day.osgb') 
sun=vizfx.addDirectionalLight()
sun.setScale(500,500,500)
sun.color(5.0,5.0,5)
sun.setEuler(90,0,0)
sky.setPosition(500,0,500)
sky.setScale(10,10,10)
'''
# Setup keyboard/mouse tracker
tracker = vizcam.addWalkNavigate(moveScale=2.0)
tracker.setPosition([0,1.8,0])
viz.link(tracker,viz.MainView)
viz.mouse.setVisible(True)
'''
# Add a yellow spot light 
light1 = vizfx.addSpotLight(euler=(0,45,0), pos=(0,3,0), color=viz.YELLOW)
light2 = vizfx.addSpotLight(euler=(0,45,0), pos=(40,3,30), color=viz.YELLOW)

# Add a white directional light pointing down 
light = vizfx.addDirectionalLight(euler=(0,90,0), color=viz.WHITE)
TOWN1 = viz.addChild('full_SCEEN1.dae')
TOWN1.setPosition(0,0.7,0)
####################placing benches around##################

bench1= viz.addChild('bench.dae')
bench1.setScale(2,2,2)
bench1.setPosition(4,0,68)
bench1.setEuler(170,0,0)

bench2= viz.addChild('bench.dae')
bench2.setScale(2,2,2)
bench2.setPosition(0,0,100)
bench2.setEuler(180,0,0)


trash= viz.addChild('trash.dae')
trash.setScale(1,1,1)
trash.setPosition(-1,0,68)
trash.setEuler(80,0,0)

'''
bench2= viz.addChild('bench.dae')
bench2.setScale(5,5,5)
bench2.setPosition(12,0,110)
bench2.setEuler(90,0,0)


bench4= viz.addChild('bench.dae')
bench4.setScale(3,3,3)
bench4.setPosition(-50,0,130)
bench4.setEuler(310,0,0)
'''

####################################placing tree all around#####################

tree= viz.addChild('palms.dae')
tree.setScale(2,2,2)
tree.setPosition(8,0,70)
tree.setEuler(80,0,0)

######################placing cars########################################


###########################WINDOWS VIEW###############################################

import vizinfo

# Create a new window in the upper left corner
UpperLeftWindow = viz.addWindow(pos=(0,1.0),size=(0.2,0.2))

#Create a new window in the upper right corner
UpperRightWindow = viz.addWindow(pos=(0.7,1.0),size=(0.2,0.2))

# Create a new viewpoint
BirdView = viz.addView()

#Attach the bird's eye view to the upper left window
UpperLeftWindow.setView(BirdView)

#Move the view above the center of the room
BirdView.setPosition([0,500,0])

#Rotate the view so that it looks down
BirdView.setEuler([0,90,0])

#Create another viewpoint
RearView = viz.addView()

#Attach the rear view to the upper right window
UpperRightWindow.setView(RearView)

#Increase the field-of-view for both windows
UpperLeftWindow.fov(60)
UpperRightWindow.fov(60)

#Add an arrow marker to bird's eye view window to represent our current position/orientation
arrow = viz.addTexQuad(parent=viz.ORTHO,scene=UpperLeftWindow,size=20)
arrow.texture(viz.add('arrow.tif'))

def UpdateViews():

	#Get the current head orientation and position
	yaw,pitch,roll = viz.MainView.getEuler()
	pos = viz.MainView.getPosition()

	#Move the rear view to the current position
	RearView.setPosition(pos)

	#Rotate the rear view so that it faces behind us
	RearView.setEuler([yaw+180,0,0])

	#Move arrow to our current location
	x,y,z = UpperLeftWindow.worldToScreen(pos,mode=viz.WINDOW_PIXELS)
	arrow.setPosition([x,y,0])
	arrow.setEuler([0,0,-yaw])

vizact.ontimer(0,UpdateViews)

######################################animated view#############################################

def AnimateView1():
	
	viz.MainView.move([510,10,500])
	viz.MainView.setEuler([90,0,0])
		
def AnimateView2():
	
	viz.MainView.move([-520,10,180])
	viz.MainView.setEuler([90,0,0])
		
def AnimateView3():
	
	viz.MainView.move([530,20,-500])
	viz.MainView.setEuler([90,0,0])
		
def AnimateView4():
	
	viz.MainView.move([-500,20,-530])
	viz.MainView.setEuler([90,0,0])
	
def AnimateView5():

	viz.MainView.move([0,20,0])
	viz.MainView.setEuler([90,0,0])
	
def AnimateView6():
	camera = vizcam.addKeyboard6DOF()
	camera.setPosition([0,2,0])
	
camera = vizcam.addKeyboard6DOF()
camera.setPosition([0,2,0])
#Setup keyboard events
vizact.onkeydown('1',AnimateView1)
vizact.onkeydown('2',AnimateView2)
vizact.onkeydown('3',AnimateView3)
vizact.onkeydown('4',AnimateView4)
vizact.onkeydown('5',AnimateView5)
vizact.onkeydown('6',AnimateView6)

############################car in loop######################

import viz
import vizinfo
import vizact

#black fency car
car1= viz.addChild('car1.dae')
car1.setScale(1.5,1.5,1.5)
car1.setPosition(85,0.8,42)
car1.setEuler(90,0,0)

car2= viz.addChild('car3.dae')
car2.setScale(1.5,1.5,1.5)
car2.setPosition(75,0.8,50)
car2.setEuler(90,0,0)
#250,0.8,42

car3= viz.addChild('car7.dae')
car3.setScale(1.5,1.5,1.5)
car3.setPosition(45,0.8,185)
car3.setEuler(270,0,0)

car4= viz.addChild('car1.dae')
car4.setScale(1.5,1.5,1.5)
car4.setPosition(75,0.8,50)
car4.setEuler(0,0,0)

#green car
car5= viz.addChild('car5.dae')
car5.setScale(1.5,1.5,1.5)
car5.setPosition(85,0.8,156)
car5.setEuler(0,0,0)

#black car
car6= viz.addChild('car6.dae')
car6.setScale(1.5,1.5,1.5)
car6.setPosition(70,0.8,149)
car6.setEuler(0,0,0)

#yellow car 1
car7= viz.addChild('car3.dae')
car7.setScale(1.5,1.5,1.5)
car7.setPosition(34,0.8,30)
car7.setEuler(180,0,0)

#green  car 2
car8= viz.addChild('car5.dae')
car8.setScale(1.5,1.5,1.5)
car8.setPosition(28,0.8,30)
car8.setEuler(270,0,0)

#yellow car 2
car9= viz.addChild('car6.dae')
car9.setScale(1.5,1.5,1.5)
car9.setPosition(-83,0.8,250)
car9.setEuler(90,0,0)

#green  car 3
car10= viz.addChild('car8.dae')
car10.setScale(1.5,1.5,1.5)
car10.setPosition(-73,1,250)
car10.setEuler(270,0,0)

#Create the animation path
path1 = viz.addAnimationPath()
path2 = viz.addAnimationPath()
path3 = viz.addAnimationPath()
path4 = viz.addAnimationPath()
path5 = viz.addAnimationPath()
path6 = viz.addAnimationPath()
path7 = viz.addAnimationPath()
path8 = viz.addAnimationPath()
path9 = viz.addAnimationPath()
path10 = viz.addAnimationPath()


#Initialize an array of control points
positions1 = [ [136,0,150],[136,0,-50],[136,0,250]]
positions2 = [ [-50,0,50], [80,0,50],[130,0,50] ]
positions3 = [ [131.5,0,85], [131.5,0,-50],[131.5,0,285] ]
positions4 = [ [-150,0,34],[70,0,34],[180,0,34]]
positions5 = [ [-200,0,156], [105,0,156],[305,0,156] ]
positions6 = [ [-200,0,149], [170,0,149],[270,0,149] ]      
positions7 = [ [34,0,250],[34,0,-30],[34,0,-230] ]
positions8 = [ [23,0,-250],[23,0,-30],[23,0,230] ]
positions9 = [ [-83,0,255],[-83,0,-30],[-83,0,-230] ]
positions10 = [ [-65,0,-65],[-65,0,-30],[-65,0,150] ]


for x,pos in enumerate(positions1):
	path1.addControlPoint(x+1,pos=pos)

for y,pos in enumerate(positions2):
	path2.addControlPoint(x+1,pos=pos)
	
for s,pos in enumerate(positions3):
	path3.addControlPoint(x+1,pos=pos)
	
for z,pos in enumerate(positions4):
	path4.addControlPoint(x+1,pos=pos)
	#path4.setAxisAngle(0,0,0,45)
	
#for green car1
for w,pos in enumerate(positions5):
	path5.addControlPoint(x+1,pos=pos)
	
#for black car
for t,pos in enumerate(positions6):
	path6.addControlPoint(x+1,pos=pos)

#for yellow car7
for m,pos in enumerate(positions7):
	path7.addControlPoint(x+1,pos=pos)

#for green car2 car8
for n,pos in enumerate(positions8):
	path8.addControlPoint(x+1,pos=pos)
	
#for yellow car2 car9
for n,pos in enumerate(positions9):
	path9.addControlPoint(x+1,pos=pos)

	
#for yellow car2 car9
for k,pos in enumerate(positions10):
	path10.addControlPoint(x+1,pos=pos)


#Set the initial loop mode to circular
path1.setLoopMode(viz.CIRCULAR)
path2.setLoopMode(viz.CIRCULAR)
path3.setLoopMode(viz.CIRCULAR)
path4.setLoopMode(viz.CIRCULAR)
path5.setLoopMode(viz.CIRCULAR)
path6.setLoopMode(viz.CIRCULAR)
path7.setLoopMode(viz.CIRCULAR)
path8.setLoopMode(viz.CIRCULAR)
path9.setLoopMode(viz.CIRCULAR)
path10.setLoopMode(viz.CIRCULAR)



#Automatically compute tangent vectors for cubic bezier translations
path1.computeTangents()
path2.computeTangents()
path3.computeTangents()
path4.computeTangents()
path5.computeTangents()
path6.computeTangents()
path7.computeTangents()
path8.computeTangents()
path9.computeTangents()
path10.computeTangents()



#Automatically rotate the path
path1.setAutoRotate(viz.OFF)
path2.setAutoRotate(viz.OFF)
path3.setAutoRotate(viz.OFF)
path4.setAutoRotate(viz.OFF)
path5.setAutoRotate(viz.OFF)
path6.setAutoRotate(viz.OFF)
path7.setAutoRotate(viz.OFF)
path8.setAutoRotate(viz.OFF)
path9.setAutoRotate(viz.OFF)
path10.setAutoRotate(viz.OFF)



#Link the ball to the path
viz.link(path1,car1)
viz.link(path2,car2)
viz.link(path3,car3)
viz.link(path4,car4)
viz.link(path5,car5)
viz.link(path6,car6)
viz.link(path7,car7)
viz.link(path8,car8)
viz.link(path9,car9)
viz.link(path10,car10)


#Play the animation path
path1.play()
path2.play()
path3.play()
path4.play()
path5.play()
path6.play()
path7.play()
path8.play()
path9.play()
path10.play()

path1.setSpeed(0.1)
path2.setSpeed(0.1)
path3.setSpeed(0.1)
path4.setSpeed(0.2)
path5.setSpeed(0.2)
path6.setSpeed(0.1)
path7.setSpeed(0.1)
path8.setSpeed(0.1)
path9.setSpeed(0.1)
path10.setSpeed(0.1)
########################################placing lights in loop
'''
#########################left hand1
red_light1=viz.addChild('red.dae')
red_light1.setPosition(43,5,58)
red_light1.setScale(4,4,4)
red_light1.visible(viz.OFF)

yellow_light1=viz.addChild('yellow.dae')
yellow_light1.setPosition(43,5,58)
yellow_light1.setScale(4,4,4)
yellow_light1.visible(viz.OFF)


green_light1=viz.addChild('green.dae')
green_light1.setPosition(43,5,58)
green_light1.setScale(4,4,4)
green_light1.visible(viz.OFF)


red_light2=viz.addChild('red.dae')
red_light2.setPosition(30.5,10,59.5)
red_light2.setScale(4,4,4)
red_light2.visible(viz.OFF)


yellow_light2=viz.addChild('yellow.dae')
yellow_light2.setPosition(30.5,10,59.5)
yellow_light2.setScale(4,4,4)
yellow_light2.visible(viz.OFF)


green_light2=viz.addChild('green.dae')
green_light2.setPosition(30.5,10,59.5)
green_light2.setScale(4,4,4)
green_light2.visible(viz.OFF)

######################left hand2

red_light11=viz.addChild('red.dae')
red_light11.setPosition(35,11,31)
red_light11.setScale(4,4,4)
red_light11.setEuler(180,0,0)
red_light11.visible(viz.OFF)

yellow_light11=viz.addChild('yellow.dae')
yellow_light11.setPosition(35,11,58)
yellow_light11.setScale(4,4,4)
yellow_light11.visible(viz.OFF)
yellow_light11.setEuler(180,0,0)


green_light11=viz.addChild('green.dae')
green_light11.setPosition(35,11,58)
green_light11.setScale(4,4,4)
green_light11.visible(viz.OFF)
green_light11.setEuler(180,0,0)

red_light22=viz.addChild('red.dae')
red_light22.setPosition(22,11,31)
red_light22.setScale(4,4,4)
red_light22.setEuler(180,0,0)
red_light22.visible(viz.OFF)

yellow_light22=viz.addChild('yellow.dae')
yellow_light22.setPosition(22,11,31)
yellow_light22.setScale(4,4,4)
yellow_light22.visible(viz.OFF)
yellow_light22.setEuler(180,0,0)

green_light22=viz.addChild('green.dae')
green_light22.setPosition(22,11,31)
green_light22.setScale(4,4,4)
green_light22.visible(viz.OFF)
green_light22.setEuler(180,0,0)

##########################right hand 1###############################################
Rred_light11=viz.addChild('red.dae')
Rred_light11.setPosition(42.5,9,49)
Rred_light11.setScale(4,4,4)
Rred_light11.setEuler(90,0,0)
Rred_light11.visible(viz.OFF)

Ryellow_light11=viz.addChild('yellow.dae')
Ryellow_light11.setPosition(42.5,9,49)
Ryellow_light11.setScale(4,4,4)
Ryellow_light11.visible(viz.OFF)
Ryellow_light11.setEuler(90,0,0)

Rgreen_light11=viz.addChild('green.dae')
Rgreen_light11.setPosition(42.5,9,49)
Rgreen_light11.setScale(4,4,4)
Rgreen_light11.visible(viz.OFF)
Rgreen_light11.setEuler(90,0,0)


Rred_light22=viz.addChild('red.dae')
Rred_light22.setPosition(42.5,9,39)
Rred_light22.setScale(4,4,4)
Rred_light22.setEuler(90,0,0)
Rred_light22.visible(viz.OFF)


Ryellow_light22=viz.addChild('yellow.dae')
Ryellow_light22.setPosition(42.5,9,39)
Ryellow_light22.setScale(4,4,4)
Ryellow_light22.visible(viz.OFF)
Ryellow_light22.setEuler(90,0,0)


Rgreen_light22=viz.addChild('green.dae')
Rgreen_light22.setPosition(42.5,9,39)
Rgreen_light22.setScale(4,4,4)
Rgreen_light22.visible(viz.OFF)
Rgreen_light22.setEuler(90,0,0)

##########################right hand 2###############################################
R2_red_light11=viz.addChild('red.dae')
R2_red_light11.setPosition(12.1,9,49)
R2_red_light11.setScale(4,4,4)
R2_red_light11.setEuler(270,0,0)
Rred_light11.visible(viz.OFF)

R2_yellow_light11=viz.addChild('yellow.dae')
R2_yellow_light11.setPosition(12.1,9,49)
R2_yellow_light11.setScale(4,4,4)
R2_yellow_light11.visible(viz.OFF)
R2_yellow_light11.setEuler(270,0,0)

R2_green_light11=viz.addChild('green.dae')
R2_green_light11.setPosition(12.1,9,49)
R2_green_light11.setScale(4,4,4)
R2_green_light11.visible(viz.OFF)
R2_green_light11.setEuler(270,0,0)


R2_red_light22=viz.addChild('red.dae')
R2_red_light22.setPosition(13,9,39)
R2_red_light22.setScale(4,4,4)
R2_red_light22.setEuler(270,0,0)
R2_red_light22.visible(viz.OFF)


R2_yellow_light22=viz.addChild('yellow.dae')
R2_yellow_light22.setPosition(13,9,39)
R2_yellow_light22.setScale(4,4,4)
R2_yellow_light22.visible(viz.OFF)
R2_yellow_light22.setEuler(270,0,0)


R2_green_light22=viz.addChild('green.dae')
R2_green_light22.setPosition(13,9,39)
R2_green_light22.setScale(4,4,4)
R2_green_light22.visible(viz.OFF)
R2_green_light22.setEuler(270,0,0)


###########################################################################################################################
def signal_lights():
	
	red_light1.visible(viz.ON)
	red_light2.visible(viz.ON)
	time.sleep(0.5)
	red_light1.visible(viz.OFF)
	red_light2.visible(viz.OFF)
	yellow_light1.visible(viz.ON)
	yellow_light2.visible(viz.ON)
	time.sleep(0.5)
	yellow_light1.visible(viz.OFF)
	yellow_light2.visible(viz.OFF)
	green_light1.visible(viz.ON)
	green_light2.visible(viz.ON)
		
vizact.onkeydown('s',signal_lights)

'''
################################################################################
#################################################################################################################################
def bmw_card_driver():
	
	car = viz.addChild('bmw.dae')
	car.setEuler([0,0,0])
	car.setScale(0.5,0.5,0.5)
	MOVE_SPEED = 5
	TURN_SPEED = 60

	def updatecar():
		#move view forward and backward
		if viz.key.isDown(viz.KEY_UP):
			view.move([0,0,MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
		elif viz.key.isDown(viz.KEY_DOWN):
			view.move([0,0,-MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)

		#rotate body of view left and right
		if viz.key.isDown(viz.KEY_RIGHT):
			view.setEuler([TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
		elif viz.key.isDown(viz.KEY_LEFT):
			view.setEuler([-TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)

		#set the car to view position and body orientation
		car.setPosition(view.getPosition())
		car.setEuler(view.getEuler(viz.BODY_ORI))
		car.setPosition([3.02,-5.50,5.04],viz.REL_LOCAL)

	vizact.ontimer(0,updatecar)

	#update head of view based on mouse movements
	def mousemove(e):
		euler = view.getEuler(viz.HEAD_ORI)
		euler[0] += e.dx*0.1
		euler[1] += -e.dy*0.1
		euler[1] = viz.clamp(euler[1],-85.0,85.0)
		view.setEuler(euler,viz.HEAD_ORI)

	viz.callback(viz.MOUSE_MOVE_EVENT,mousemove)
	viz.mouse(viz.OFF)
	viz.mouse.setVisible(False)

	vizact.onmousedown(viz.MOUSEBUTTON_LEFT,view.reset,viz.HEAD_ORI)
	vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,view.reset, viz.BODY_ORI |viz.HEAD_POS)
	vizact.onmousedown(viz.MOUSEBUTTON_RIGHT,updatecar)

vizact.onkeydown('b',bmw_card_driver)

############################################################################################################################

def select_menu():	
	dialog.selection = 0
	yield dialog.show()
	if(dialog.selection==0):
			yield how_many.show()
			if(how_many.selection==0): #for 1
						red_female1.visible(viz.ON)

			if(how_many.selection==1): #for 2
						red_female1.visible(viz.ON)
						red_female3.visible(viz.ON)
						myface1.visible(viz.ON)

			if(how_many.selection==2): #for 3
						red_female1.visible(viz.ON)	
						red_female2.visible(viz.ON)
						red_female3.visible(viz.ON)
						myface2.visible(viz.ON)

						
			if(how_many.selection==3): #for 4
						red_female1.visible(viz.ON)	
						red_female2.visible(viz.ON)
						red_female3.visible(viz.ON)
						red_man4.visible(viz.ON)
						myface2.visible(viz.ON)
						
			if(how_many.selection==4): #for 5
						red_female1.visible(viz.ON)	
						red_female2.visible(viz.ON)
						red_female3.visible(viz.ON)
						red_man3.visible(viz.ON)
						red_man4.visible(viz.ON)
						myface1.visible(viz.ON)
						myface2.visible(viz.ON)
						
			if(how_many.selection==5): #for 6
						red_female1.visible(viz.ON)
						red_female2.visible(viz.ON)
						red_female3.visible(viz.ON)
						red_man2.visible(viz.ON)
						red_man3.visible(viz.ON)
						red_man4.visible(viz.ON)
						myface1.visible(viz.ON)
						myface2.visible(viz.ON)
						
			if(how_many.selection==6): #for 7
						red_female1.visible(viz.ON)
						red_female2.visible(viz.ON)
						red_female3.visible(viz.ON)
						red_female4.visible(viz.ON)
						red_man2.visible(viz.ON)
						red_man3.visible(viz.ON)
						red_man4.visible(viz.ON)
						myface1.visible(viz.ON)
						myface2.visible(viz.ON)
						
			if(how_many.selection==7):
						red_female1.visible(viz.ON)
						red_female2.visible(viz.ON)
						red_female3.visible(viz.ON)
						red_female4.visible(viz.ON)
						red_female5.visible(viz.ON)
						red_man2.visible(viz.ON)
						red_man3.visible(viz.ON)
						red_man4.visible(viz.ON)
						myface1.visible(viz.ON)
						myface2.visible(viz.ON)
			if(how_many.selection==8):
						red_female1.visible(viz.ON)
						red_female2.visible(viz.ON)
						red_female3.visible(viz.ON)
						red_female4.visible(viz.ON)
						red_female5.visible(viz.ON)
						red_female6.visible(viz.ON)
						red_man2.visible(viz.ON)
						red_man3.visible(viz.ON)
						red_man4.visible(viz.ON)
						myface1.visible(viz.ON)
						myface2.visible(viz.ON)
			if(how_many.selection==9):
						red_female1.visible(viz.ON)
						red_female2.visible(viz.ON)
						red_female3.visible(viz.ON)
						red_female4.visible(viz.ON)
						red_female5.visible(viz.ON)
						red_female6.visible(viz.ON)
						red_man2.visible(viz.ON)
						red_man3.visible(viz.ON)
						red_man4.visible(viz.ON)
						red_man5.visible(viz.ON)
						myface1.visible(viz.ON)
						myface2.visible(viz.ON)
	if(dialog.selection==1):  ##########green agent
			yield how_many.show()
			if(how_many.selection==0): #for 1
						green_female1.visible(viz.ON)

			if(how_many.selection==1): #for 2
						green_female1.visible(viz.ON)
						green_female2.visible(viz.ON)
			

			if(how_many.selection==2): #for 3
						green_female1.visible(viz.ON)	
						green_female2.visible(viz.ON)
						green_female3.visible(viz.ON)
					
						
			if(how_many.selection==3): #for 4
						green_female1.visible(viz.ON)	
						green_female2.visible(viz.ON)
						green_female3.visible(viz.ON)
						green_female4.visible(viz.ON)
						
			if(how_many.selection==4): #for 5
						green_female1.visible(viz.ON)	
						green_female2.visible(viz.ON)
						green_female3.visible(viz.ON)
						green_female4.visible(viz.ON)
						green_man1.visible(viz.ON)
						
						
			if(how_many.selection==5): #for 6
						green_female1.visible(viz.ON)	
						green_female2.visible(viz.ON)
						green_female3.visible(viz.ON)
						green_female4.visible(viz.ON)
						green_man1.visible(viz.ON)
						green_man2.visible(viz.ON)

						
			if(how_many.selection==6): #for 7
						green_female1.visible(viz.ON)	
						green_female2.visible(viz.ON)
						green_female3.visible(viz.ON)
						green_female4.visible(viz.ON)
						green_man1.visible(viz.ON)
						green_man2.visible(viz.ON)
						green_man3.visible(viz.ON)
						
			if(how_many.selection==7): #for 8
						green_female1.visible(viz.ON)	
						green_female2.visible(viz.ON)
						green_female3.visible(viz.ON)
						green_female4.visible(viz.ON)
						green_man1.visible(viz.ON)
						green_man2.visible(viz.ON)
						green_man3.visible(viz.ON)
						green_man4.visible(viz.ON)
						
			if(how_many.selection==8): #for 9
						green_female1.visible(viz.ON)	
						green_female2.visible(viz.ON)
						green_female3.visible(viz.ON)
						green_female4.visible(viz.ON)
						green_man1.visible(viz.ON)
						green_man2.visible(viz.ON)
						green_man3.visible(viz.ON)
						green_man4.visible(viz.ON)
						green_man5.visible(viz.ON)
						
			if(how_many.selection==9): #for 9
						green_female1.visible(viz.ON)	
						green_female2.visible(viz.ON)
						green_female3.visible(viz.ON)
						green_female4.visible(viz.ON)
						green_man1.visible(viz.ON)
						green_man2.visible(viz.ON)
						green_man3.visible(viz.ON)
						green_man4.visible(viz.ON)
						green_man5.visible(viz.ON)
						green_man6.visible(viz.ON)
				
	if(dialog.selection==2):
			yield how_many.show()
			if(how_many.selection==0): #for 1
						orange_female1.visible(viz.ON)

			if(how_many.selection==1): #for 2
						orange_female1.visible(viz.ON)
						orange_female2.visible(viz.ON)
			

			if(how_many.selection==2): #for 3
						orange_female1.visible(viz.ON)	
						orange_female2.visible(viz.ON)
						orange_female3.visible(viz.ON)
					
						
			if(how_many.selection==3): #for 4
						orange_female1.visible(viz.ON)	
						orange_female2.visible(viz.ON)
						orange_female3.visible(viz.ON)
						orange_female4.visible(viz.ON)
						
			if(how_many.selection==4): #for 5
						orange_female1.visible(viz.ON)	
						orange_female2.visible(viz.ON)
						orange_female3.visible(viz.ON)
						orange_female4.visible(viz.ON)
						orange_male1.visible(viz.ON)
						
						
			if(how_many.selection==5): #for 6
						orange_female1.visible(viz.ON)	
						orange_female2.visible(viz.ON)
						orange_female3.visible(viz.ON)
						orange_female4.visible(viz.ON)
						orange_male1.visible(viz.ON)
						orange_male2.visible(viz.ON)

						
			if(how_many.selection==6): #for 7
						orange_female1.visible(viz.ON)	
						orange_female2.visible(viz.ON)
						orange_female3.visible(viz.ON)
						orange_female4.visible(viz.ON)
						orange_male1.visible(viz.ON)
						orange_male2.visible(viz.ON)
						orange_male3.visible(viz.ON)
						
			if(how_many.selection==7): #for 8
						orange_female1.visible(viz.ON)	
						orange_female2.visible(viz.ON)
						orange_female3.visible(viz.ON)
						orange_female4.visible(viz.ON)
						orange_male1.visible(viz.ON)
						orange_male2.visible(viz.ON)
						orange_male3.visible(viz.ON)
						orange_male4.visible(viz.ON)
						
			if(how_many.selection==8): #for 9
						orange_female1.visible(viz.ON)	
						orange_female2.visible(viz.ON)
						orange_female3.visible(viz.ON)
						orange_female4.visible(viz.ON)
						orange_male1.visible(viz.ON)
						orange_male2.visible(viz.ON)
						orange_male3.visible(viz.ON)
						orange_male4.visible(viz.ON)
						orange_male5.visible(viz.ON)
						
			if(how_many.selection==9): #for 9
						orange_female1.visible(viz.ON)	
						orange_female2.visible(viz.ON)
						orange_female3.visible(viz.ON)
						orange_female4.visible(viz.ON)
						orange_male1.visible(viz.ON)
						orange_male2.visible(viz.ON)
						orange_male3.visible(viz.ON)
						orange_male4.visible(viz.ON)
						orange_male5.visible(viz.ON)
						orange_male6.visible(viz.ON)

				
	if(dialog.selection==3):
			yield how_many.show()
			if(how_many.selection==0): #for 1
						white_female1.visible(viz.ON)

			if(how_many.selection==1): #for 2
						white_female1.visible(viz.ON)
						white_female2.visible(viz.ON)
			

			if(how_many.selection==2): #for 3
						white_female1.visible(viz.ON)	
						white_female2.visible(viz.ON)
						white_female3.visible(viz.ON)
					
						
			if(how_many.selection==3): #for 4
						white_female1.visible(viz.ON)	
						white_female2.visible(viz.ON)
						white_female3.visible(viz.ON)
						white_female4.visible(viz.ON)
						
			if(how_many.selection==4): #for 5
						white_female1.visible(viz.ON)	
						white_female2.visible(viz.ON)
						white_female3.visible(viz.ON)
						white_female4.visible(viz.ON)
						white_male1.visible(viz.ON)
						
						
						
			if(how_many.selection==5): #for 6
						white_female1.visible(viz.ON)	
						white_female2.visible(viz.ON)
						white_female3.visible(viz.ON)
						white_female4.visible(viz.ON)
						white_male1.visible(viz.ON)
						white_male2.visible(viz.ON)
					
						
						
			if(how_many.selection==6): #for 7
						white_female1.visible(viz.ON)	
						white_female2.visible(viz.ON)
						white_female3.visible(viz.ON)
						white_female4.visible(viz.ON)
						white_male1.visible(viz.ON)
						white_male2.visible(viz.ON)
						white_male3.visible(viz.ON)
						
						
			if(how_many.selection==7): #for 8
						white_female1.visible(viz.ON)	
						white_female2.visible(viz.ON)
						white_female3.visible(viz.ON)
						white_female4.visible(viz.ON)
						white_male1.visible(viz.ON)
						white_male2.visible(viz.ON)
						white_male3.visible(viz.ON)
						white_male4.visible(viz.ON)
						
						
			if(how_many.selection==8): #for 9
						white_female1.visible(viz.ON)	
						white_female2.visible(viz.ON)
						white_female3.visible(viz.ON)
						white_female4.visible(viz.ON)
						white_male1.visible(viz.ON)
						white_male2.visible(viz.ON)
						white_male3.visible(viz.ON)
						white_male4.visible(viz.ON)
						white_male5.visible(viz.ON)
						
						
			if(how_many.selection==9): #for 9
						white_female1.visible(viz.ON)	
						white_female2.visible(viz.ON)
						white_female3.visible(viz.ON)
						white_female4.visible(viz.ON)
						white_male1.visible(viz.ON)
						white_male2.visible(viz.ON)
						white_male3.visible(viz.ON)
						white_male4.visible(viz.ON)
						white_male5.visible(viz.ON)
						white_male6.visible(viz.ON)
						
				
	if(dialog.selection==4):
			yield how_many.show()
			if(how_many.selection==0): #for 1
						blue_female1.visible(viz.ON)

			if(how_many.selection==1): #for 2
						blue_female1.visible(viz.ON)
						blue_female2.visible(viz.ON)
			

			if(how_many.selection==2): #for 3
						blue_female1.visible(viz.ON)	
						blue_female2.visible(viz.ON)
						blue_female3.visible(viz.ON)
						
						
			if(how_many.selection==3): #for 4
						blue_female1.visible(viz.ON)	
						blue_female2.visible(viz.ON)
						blue_female3.visible(viz.ON)
						blue_female4.visible(viz.ON)	
						
						
			if(how_many.selection==4): #for 5
						blue_female1.visible(viz.ON)	
						blue_female2.visible(viz.ON)
						blue_female3.visible(viz.ON)
						blue_female4.visible(viz.ON)	
						blue_man2.visible(viz.ON)
						
						
			if(how_many.selection==5): #for 6
						blue_female1.visible(viz.ON)	
						blue_female2.visible(viz.ON)
						blue_female3.visible(viz.ON)
						blue_female4.visible(viz.ON)	
						blue_man2.visible(viz.ON)
						blue_man3.visible(viz.ON)
						
			if(how_many.selection==6): #for 7
						blue_female1.visible(viz.ON)	
						blue_female2.visible(viz.ON)
						blue_female3.visible(viz.ON)
						blue_female4.visible(viz.ON)	
						blue_man2.visible(viz.ON)
						blue_man3.visible(viz.ON)
						blue_man4.visible(viz.ON)	
						
						
			if(how_many.selection==7): #for 8
						blue_female1.visible(viz.ON)	
						blue_female2.visible(viz.ON)
						blue_female3.visible(viz.ON)
						blue_female4.visible(viz.ON)	
						blue_man2.visible(viz.ON)
						blue_man3.visible(viz.ON)
						blue_man4.visible(viz.ON)	
						blue_man5.visible(viz.ON)
						bl
						
						
			if(how_many.selection==8): #for 9
						blue_female1.visible(viz.ON)	
						blue_female2.visible(viz.ON)
						blue_female3.visible(viz.ON)
						blue_female4.visible(viz.ON)	
						blue_man2.visible(viz.ON)
						blue_man3.visible(viz.ON)
						blue_man4.visible(viz.ON)	
						blue_man5.visible(viz.ON)
						blue_man6.visible(viz.ON)
						
						
			if(how_many.selection==9): #for 9
						blue_female1.visible(viz.ON)	
						blue_female2.visible(viz.ON)
						blue_female3.visible(viz.ON)
						blue_female4.visible(viz.ON)	
						blue_man2.visible(viz.ON)
						blue_man3.visible(viz.ON)
						blue_man4.visible(viz.ON)	
						blue_man5.visible(viz.ON)
						blue_man6.visible(viz.ON)
						blue_man7.visible(viz.ON)
				
	if(dialog.selection==5):
			yield how_many.show()
			if(how_many.selection==0): #for 1
						yellow_female1.visible(viz.ON)
					

			if(how_many.selection==1): #for 2
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						
			

			if(how_many.selection==2): #for 3
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						yellow_female3.visible(viz.ON)
						
						
			if(how_many.selection==3): #for 4
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						yellow_female3.visible(viz.ON)
						yellow_female4.visible(viz.ON)
						
						
			if(how_many.selection==4): #for 5
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						yellow_female3.visible(viz.ON)
						yellow_female4.visible(viz.ON)
						yellow_male1.visible(viz.ON)
						
						
						
			if(how_many.selection==5): #for 6
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						yellow_female3.visible(viz.ON)
						yellow_female4.visible(viz.ON)
						yellow_male1.visible(viz.ON)
						yellow_male2.visible(viz.ON)
						
						
			if(how_many.selection==6): #for 7
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						yellow_female3.visible(viz.ON)
						yellow_female4.visible(viz.ON)
						yellow_male1.visible(viz.ON)
						yellow_male2.visible(viz.ON)
						yellow_male3.visible(viz.ON)
						
						
						
			if(how_many.selection==7): #for 8
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						yellow_female3.visible(viz.ON)
						yellow_female4.visible(viz.ON)
						yellow_male1.visible(viz.ON)
						yellow_male2.visible(viz.ON)
						yellow_male3.visible(viz.ON)
						yellow_male4.visible(viz.ON)
					
						
			if(how_many.selection==8): #for 9
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						yellow_female3.visible(viz.ON)
						yellow_female4.visible(viz.ON)
						yellow_male1.visible(viz.ON)
						yellow_male2.visible(viz.ON)
						yellow_male3.visible(viz.ON)
						yellow_male4.visible(viz.ON)
						yellow_male5.visible(viz.ON)
						
						
			if(how_many.selection==9): #for 9
						yellow_female1.visible(viz.ON)
						yellow_female2.visible(viz.ON)
						yellow_female3.visible(viz.ON)
						yellow_female4.visible(viz.ON)
						yellow_male1.visible(viz.ON)
						yellow_male2.visible(viz.ON)
						yellow_male3.visible(viz.ON)
						yellow_male4.visible(viz.ON)
						yellow_male5.visible(viz.ON)
						yellow_male6.visible(viz.ON)
	#else:
				#viz.quit()
def stupid():
	dialog.visible(viz.TOGGLE)
	viztask.schedule(select_menu)

viztask.schedule(select_menu)

vizact.onkeydown('l',stupid)
