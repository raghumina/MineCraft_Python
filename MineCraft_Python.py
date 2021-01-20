# A sample MineCraft game

# Modules used Ursina,

# Tool and Languages used: Python, PyCharm, GitHub

# lets import libraries form Ursina

from ursina import *  #

def update():
    if held_keys['a']:  # to apply key control on game any key on keyword can be used.
        test_square.x -=4 * time.dt   # time to control the movement of entities and window according to our requirements.


# we have to create an instance for the game for example board
app = Ursina()  # created an instance named app

# we have to create an entity
# in Ursina entity's are like building blocks of game they can be anything for example
# Squares, Boxes, Sounds, Circles and Various shapes.
# We can create them according to our need and can modify them also.

# Lets create them
test_square = Entity(model="cube", color=color.green, scale=(1, 4),
                     position=(5, 4))  # scale is used for  positioning of entitiy on game window.
# Here we use model to define shapes.


app.run()  # ran it
# by running app we can see the game board or window and frames.
