import pyglet
from pyglet import app
from pyglet import shapes

window = pyglet.window.Window(600, 550)
batch = pyglet.graphics.Batch()
#  600 / 4 = 150
# 120 ok ? 

# Vaihtuvien värien laatikot vasemmalta oikealle
rectangle1 = shapes.Rectangle(30, 100, 120, 350, color=(255, 22, 20), batch=batch)
rectangle2 = shapes.Rectangle(30, 100, 120, 350, color=(255, 22, 20), batch=batch)
rectangle3 = shapes.Rectangle(30, 100, 120, 350, color=(255, 22, 20), batch=batch)
rectangle4 = shapes.Rectangle(30, 100, 120, 350, color=(255, 22, 20), batch=batch)




@window.event
def on_draw():
    window.clear()
    batch.draw()

app.run()
