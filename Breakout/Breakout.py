import pyglet
import random
import pyglet.gl
from pyglet import gl

#okno
VYSKA = 700
SIRKA = 1000

#lopta
VELKOST_LOPTY = 40
RYCHLOST = 200

#palka
HRUBKA_PALKY = 10
VYSKA_PALKY =  200
RYHLOST_PLAKY = RYCHLOST * 1,5

#text
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#premenne
pozicia_palky = [VYSKA // 2, VYSKA//2]
pozicia_lopty = [SIRKA//2, VYSKA//2]
rychlost_lopty = [0, 0]
stlacenie_klaves = set()
skore = [0]

window = pyglet.window.Window(width=SIRKA, height=VYSKA)

def vykresli_obdlznik(x1,y1,x2,y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))
    gl.glEnd()


pyglet.app.run()





