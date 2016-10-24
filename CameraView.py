import bge

def Main():

	# get the window dimensions
	import Rasterizer
	width = Rasterizer.getWindowWidth()
	height = Rasterizer.getWindowHeight()

	# get the current scene
	scene = bge.logic.getCurrentScene()
	# and use it to get a list of the objects in the scene
	objList = scene.objects
	# get the two player cameras, called cam1 and cam2
	playermaincam = objList["Camera"]

	# set player viewports with player1 at the right, player 2 at the left
	playermaincam.setViewport( 0, 0, width, height)

	# finally, we turn on the use of both viewports
	playermaincam.useViewport = True

# this is needed if this module is called as a script!
Main()
