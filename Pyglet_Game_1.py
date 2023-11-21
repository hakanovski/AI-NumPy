import pyglet
from pyglet.window import key

# Game window settings
window = pyglet.window.Window(width=400, height=400)
square_size = 30
player_position = [window.width // 2, window.height // 2]

# Drawing the player's square
@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                         ('v2i', (player_position[0] - square_size // 2, player_position[1] - square_size // 2,
                                  player_position[0] + square_size // 2, player_position[1] - square_size // 2,
                                  player_position[0] + square_size // 2, player_position[1] + square_size // 2,
                                  player_position[0] - square_size // 2, player_position[1] + square_size // 2))
                        )

# Handling keyboard events
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        player_position[0] -= square_size
    elif symbol == key.RIGHT:
        player_position[0] += square_size
    elif symbol == key.UP:
        player_position[1] += square_size
    elif symbol == key.DOWN:
        player_position[1] -= square_size

# Run the game
pyglet.app.run()