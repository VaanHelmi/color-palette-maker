import pyglet
from pyglet import shapes
from pyglet import image
import random
import pyperclip
from pyglet import app

rect1 = {
    "lock": False,
    "rgb": (194, 0, 32),
    "hex": "#c20020"
}
rect2 = {
    "lock": False,
    "rgb": (25, 33, 255),
    "hex": "#1921ff"
}
rect3 = {
    "lock": False,
    "rgb": (224, 211, 88),
    "hex": "#e0d358"
}
rect4 = {
    "lock": False,
    "rgb": (82, 173, 68),
    "hex": "#52ad44"
}

window = pyglet.window.Window(600, 550)
batch = pyglet.graphics.Batch()
windowColor = shapes.Rectangle(0, 0, 600, 550, color=(255, 255, 255), batch=batch)

# Lock button 1
lockText1Border = shapes.Rectangle(55, 474, 75, 26, color=(238, 202, 226), batch=batch)
lockText1 = pyglet.text.Label('Lock', font_name='Consolas', color=(0, 0, 0, 255), font_size=14,
                                x=65, y=489, anchor_x='left', anchor_y='center', batch=batch)

# Lock button 2
lockText2Border = shapes.Rectangle(195, 474, 75, 26, color=(238, 202, 226), batch=batch)
lockText2 = pyglet.text.Label('Lock', font_name='Consolas', color=(0, 0, 0, 255), font_size=14,
                                x=205, y=489, anchor_x='left', anchor_y='center', batch=batch)

# Lock button 3
lockText3Border = shapes.Rectangle(335, 474, 75, 26, color=(238, 202, 226), batch=batch)
lockText3 = pyglet.text.Label('Lock', font_name='Consolas', color=(0, 0, 0, 255), font_size=14,
                                x=345, y=489, anchor_x='left', anchor_y='center', batch=batch)

# Lock button 3
lockText4Border = shapes.Rectangle(475, 474, 75, 26, color=(238, 202, 226), batch=batch)
lockText4 = pyglet.text.Label('Lock', font_name='Consolas', color=(0, 0, 0, 255), font_size=14,
                                x=485, y=489, anchor_x='left', anchor_y='center', batch=batch)

# Button for color change
button = shapes.Rectangle(260, 510, 80, 30, color=(238, 202, 226), batch=batch)
textButton = pyglet.text.Label("Randomize", font_name='Consolas', color=(0, 0, 0, 255), font_size=12, 
                                x=261, y=526, anchor_x='left', anchor_y='center', batch=batch)

# Boxes for colors
rect1Border = shapes.Rectangle(29, 119, 122, 352, color=(0, 0, 0), batch=batch)
rectangle1 = shapes.Rectangle(30, 120, 120, 350, color=rect1["rgb"], batch=batch)

rect2Border = shapes.Rectangle(169, 119, 122, 352, color=(0, 0, 0), batch=batch)
rectangle2 = shapes.Rectangle(170, 120, 120, 350, color=rect2["rgb"], batch=batch)

rect3Border = shapes.Rectangle(309, 119, 122, 352, color=(0, 0, 0), batch=batch)
rectangle3 = shapes.Rectangle(310, 120, 120, 350, color=rect3["rgb"], batch=batch)

rect4Border = shapes.Rectangle(449, 119, 122, 352, color=(0, 0, 0), batch=batch)
rectangle4 = shapes.Rectangle(450, 120, 120, 350, color=rect4["rgb"], batch=batch)

# RGB texts
rgb1Text = pyglet.text.Label(str(rect1["rgb"]), font_name='Consolas', color=(0, 0, 0, 255), font_size=12,
                         x=30, y=100, anchor_x='left', anchor_y='center', batch=batch)

rgb2Text = pyglet.text.Label(str(rect2["rgb"]), font_name='Consolas', color=(0, 0, 0, 255), font_size=12,
                        x=170, y=100, anchor_x='left', anchor_y='center', batch=batch)

rgb3Text = pyglet.text.Label(str(rect3["rgb"]), font_name='Consolas', color=(0, 0, 0, 255), font_size=12,
                        x=310, y=100, anchor_x='left', anchor_y='center', batch=batch)

rgb4Text = pyglet.text.Label(str(rect4["rgb"]), font_name='Consolas', color=(0, 0, 0, 255), font_size=12,
                        x=450, y=100, anchor_x='left', anchor_y='center', batch=batch)

# Hex texts
hex1Text = pyglet.text.Label(str(rect1["hex"]), font_name='Consolas', color=(0, 0, 0, 255), font_size=12,
                         x=75, y=45, anchor_x='center', anchor_y='center', batch=batch)

hex2Text = pyglet.text.Label(str(rect2["hex"]), font_name='Consolas', color=(0, 0, 0, 255), font_size=12,
                        x=215, y=45, anchor_x='center', anchor_y='center', batch=batch)

hex3Text = pyglet.text.Label(str(rect3["hex"]), font_name='Consolas', color=(0, 0, 0, 255), font_size=12,
                        x=355, y=45, anchor_x='center', anchor_y='center', batch=batch)

hex4Text = pyglet.text.Label(str(rect4["hex"]), font_name='Consolas', color=(0, 0, 0, 255), font_size=12,
                        x=495, y=45, anchor_x='center', anchor_y='center', batch=batch)

copyImg = image.load("copyIcon.png")

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == 1 and y > 500:
        clickRandomizeButton(x, y, button)
    elif button == 1 and y > 470:
        lockButton(x, y)
    elif button == 1 and y < 120:
        copyColor(x, y)

def clickRandomizeButton(x, y, button):
    if x in range(260, 340) and button == 1:
        if y in range(510, 540):
            randomizeColors()

def randomizeColors():
    for rectangleNum in range(1, 5):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        if rectangleNum == 1 and rect1["lock"] == False:
            rect1["rgb"] = color
        elif rectangleNum == 2 and rect2["lock"] == False:
            rect2["rgb"] = color
        elif rectangleNum == 3 and rect3["lock"] == False:
            rect3["rgb"] = color
        elif rectangleNum == 4 and rect4["lock"] == False:
            rect4["rgb"] = color

def lockButton(x, y):
    if x in range(55, 130):
        if y in range(474, 500):
            if rect1["lock"] == False:
                rect1["lock"] = True
                lockText1.text = "Unlock"
            elif rect1["lock"] == True:
                rect1["lock"] = False
                lockText1.text = "Lock"
    elif x in range(195, 270):
        if y in range(474, 500):
            if rect2["lock"] == False:
                rect2["lock"] = True
                lockText2.text = "Unlock"
            elif rect2["lock"] == True:
                rect2["lock"] = False
                lockText2.text = "Lock"
    elif x in range(335, 410):
        if y in range(474, 500):
            if rect3["lock"] == False:
                rect3["lock"] = True
                lockText3.text = "Unlock"
            elif rect3["lock"] == True:
                rect3["lock"] = False
                lockText3.text = "Lock"
    elif x in range(475, 550):
        if y in range(474, 500):
            if rect4["lock"] == False:
                rect4["lock"] = True
                lockText4.text = "Unlock"
            elif rect4["lock"] == True:
                rect4["lock"] = False
                lockText4.text = "Lock"

def copyColor(x, y):
    if x in range(75, 94):
        if y in range(56, 84):
            code = str(rect1["rgb"])
            pyperclip.copy(code)
        elif y in range(5, 33):
            code = str(rect1["hex"])
            pyperclip.copy(code)

    elif x in range(215, 234):
        if y in range(56, 84):
            code = str(rect2["rgb"])
            pyperclip.copy(code)
        elif y in range(5, 33):
            code = str(rect2["hex"])
            pyperclip.copy(code)

    elif x in range(355, 374):
        if y in range(56, 84):
            code = str(rect3["rgb"])
            pyperclip.copy(code)
        elif y in range(5, 33):
            code = str(rect3["hex"])
            pyperclip.copy(code)

    elif x in range(495, 514):
        if y in range(56, 84):
            code = str(rect4["rgb"])
            pyperclip.copy(code)
        elif y in range(5, 33):
            code = str(rect4["hex"])
            pyperclip.copy(code)           

def changeNewColors():
    if rect1["lock"] == False:
        rect1Color = rect1["rgb"]
        rectangle1.color = rect1Color

    if rect2["lock"] == False:
        rect2Color = rect2["rgb"]
        rectangle2.color = rect2Color

    if rect3["lock"] == False:
        rect3Color = rect3["rgb"]
        rectangle3.color = rect3Color

    if rect4["lock"] == False:
        rect4Color = rect4["rgb"]
        rectangle4.color = rect4Color

def rgbToHex():
    r1, g1, b1 = rect1["rgb"]
    rect1["hex"] = ('#{:02x}{:02x}{:02x}'.format(r1, g1, b1))
    
    r2, g2, b2 = rect2["rgb"]
    rect2["hex"] = ('#{:02x}{:02x}{:02x}'.format(r2, g2, b2))

    r3, g3, b3 = rect3["rgb"]
    rect3["hex"] = ('#{:02x}{:02x}{:02x}'.format(r3, g3, b3))

    r4, g4, b4 = rect4["rgb"]
    rect4["hex"] = ('#{:02x}{:02x}{:02x}'.format(r4, g4, b4))

def changeRgbTexts():
    text1 = str(rect1["rgb"])
    rgb1Text.text = text1

    text2 = str(rect2["rgb"])
    rgb2Text.text = text2

    text3 = str(rect3["rgb"])
    rgb3Text.text = text3

    text4 = str(rect4["rgb"])
    rgb4Text.text = text4

def changeHexText():
    text1 = str(rect1["hex"])
    hex1Text.text = text1

    text2 = str(rect2["hex"])
    hex2Text.text = text2

    text3 = str(rect3["hex"])
    hex3Text.text = text3

    text4 = str(rect4["hex"])
    hex4Text.text = text4

@window.event
def on_draw():
    window.clear()
    batch.draw()
    changeNewColors()
    rgbToHex()
    changeRgbTexts()
    changeHexText()

    # RGB Copies
    copyImg.blit(75, 56)
    copyImg.blit(215, 56)
    copyImg.blit(355, 56)
    copyImg.blit(495, 56)
    # Hex Copies
    copyImg.blit(75, 5)
    copyImg.blit(215, 5)
    copyImg.blit(355, 5)
    copyImg.blit(495, 5)

app.run()
