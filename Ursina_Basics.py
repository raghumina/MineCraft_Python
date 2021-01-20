# Basics of Ursina and game development form it

# Modules used Ursina,

# Tool and Languages used: Python, PyCharm, GitHub

# lets import libraries form Ursina

from ursina import *  #


# to create a cube for game we need to create a class for it as it haves all control regarding it.
class Test_Cube(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            color=color.white,
            texture='cube',
            rotation=Vec3(45, 45, 45)
        )


# Creating a class for button

class Test_Button(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="cube",
            texture="brick",
            color=color.blue,
            highlight_color=color.red,
            pressed_color=color.lime
        )


def update():
    if held_keys['a']:  # to apply key control on game any key on keyword can be used.
        test_square.x -= 4 * time.dt  # time to control the movement of entities and window according to our requirements.


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

# to add texture or png in our game
sans_texture = load_texture("mino.png")
sans = Entity(mode="quad", texture=sans_texture)

test_cube = Test_Button()

app.run()  # ran it
# by running app we can see the game board or window and frames.
