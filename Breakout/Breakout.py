import pyglet
import random
import pyglet.gl
from pyglet import gl

SIRKA = 1000
VYSKA = 700

#lopta
VELKOST_LOPTY = 20
RYCHLOST = 200

#palky
TLSTKA_PALKY = 70
VYSKA_PALKY = 10
RYCHLOST_PALKY = RYCHLOST * 1.5


#prostred naciata
CIARA_HRUBKA = 20

#font
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#stavove premenne
pozicie_palok = [50,10]
pozicia_lopty = [SIRKA//2, VYSKA//2]
rychlost_lopty = [0, 0]
stisknutie_klaves = set()
skore = [0, 0]


def vykresli_obdlznik(x1,y1,x2,y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))
    gl.glEnd()


def nakresli_text(text, x, y, pozice_x):
    napis = pyglet.text.Label(text,font_size=VELKOST_FONTU,x=x,y=y,anchor_x=pozice_x)
    napis.draw()

def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1, 1, 1)

    # vykresli loptu
    vykresli_obdlznik(
        pozicia_lopty[0] - VELKOST_LOPTY // 2,
        pozicia_lopty[1] - VELKOST_LOPTY // 2,
        pozicia_lopty[0] + VELKOST_LOPTY // 2,
        pozicia_lopty[1] + VELKOST_LOPTY // 2

    )
    gl.glColor3f(255, 255, 1)
    vykresli_obdlznik(pozicia_lopty[0], pozicia_lopty[1], pozicia_lopty[0] + 10, pozicia_lopty[1] + 10)

    #vykresli palky
    for x, y in [(-10,-10), (500,10)]:
        vykresli_obdlznik(
            x - TLSTKA_PALKY,
            y - VYSKA_PALKY //2,
            x + TLSTKA_PALKY,
            y + VYSKA_PALKY //2

    )


    #vykresli skore
    score=nakresli_text(str(skore[0]),x=ODSADENIE_TEXTU,y = VYSKA- ODSADENIE_TEXTU - VELKOST_FONTU,pozice_x='left')






window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
)

pyglet.app.run()
