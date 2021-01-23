# Minecraft game
# Using Ursina Module
#

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

grass_texture = load_texture("grass_block.png")
stone_texture = load_texture("stone_block.png")
brick_texture = load_texture("brick_block.png")
dirt_texture = load_texture("dirt_block.png")


# Minecraft is a Voxel based game
# Voxel are used to store the data in case of mine craft terrain data.
class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='block',
            origin_y=0.5,
            texture='grass_texture',
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.lime)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxeloxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)


app = Ursina()
for x in range(12):  # creating buttons here
    for z in range(12):
        voxel = Voxel(position=(z, 0, x))

# creating a player controller or player
player = FirstPersonController()

app.run()
