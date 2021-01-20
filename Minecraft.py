# Minecraft game
# Using Ursina Module
#

from ursina import *

# Minecraft is a Voxel based game
# Voxel are
class Voxel(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            position = (0,0,0),
            model = 'cube',
            origin_y = 0.5,
            texture  = 'white_cube',
            color= color.white,
            highlight_color = 'color.lime'
        )




app = Ursina()
for x in range(8):           # creating buttons here
    for z in range(8):
        voxel = Voxel()
        

app.run()