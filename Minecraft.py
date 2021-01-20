# Minecraft game
# Using Ursina Module
#

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# Minecraft is a Voxel based game
# Voxel are used to store the data in case of mine craft terrain data.
class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.white,
            highlight_color=color.lime)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)



app = Ursina()
for x in range(10):  # creating buttons here
    for z in range(10):
        voxel = Voxel(position=(z, 0, x))

# creating a player controller or player
player = FirstPersonController()

app.run()
