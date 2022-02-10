import pyglet
import random
import pyglet.gl
from pyglet import gl

SIRKA = 1015
VYSKA = 700

#lopta
VELKOST_LOPTY = 20
RYCHLOST = 200

#palky
TLSTKA_PALKY = 70
VYSKA_PALKY = 10
RYCHLOST_PALKY = RYCHLOST * 1.5

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

def stisk_klavesnice(symbol, modifikatory):
    from pyglet.window import key
    if symbol == key.D:
        stisknutie_klaves.add(("vpravo", 0))
    if symbol == key.A:
        stisknutie_klaves.add(("vlavo", 0))

def pusti_klavesnice(symbol, modifikatory):
    from pyglet.window import key
    if symbol == key.D:
        stisknutie_klaves.discard(("vpravo", 0))
    if symbol == key.A:
        stisknutie_klaves.discard(("vlavo", 0))


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


    #vykresli palku
    for x, y in [(-50,-50), (507.5,10)]:
        vykresli_obdlznik(
            x - TLSTKA_PALKY,
            y - VYSKA_PALKY //2,
            x + TLSTKA_PALKY,
            y + VYSKA_PALKY //2

    )
    #bricky 1.rad
    brick1 = vykresli_obdlznik(115,600,20,550)
    brick2 = vykresli_obdlznik(225, 600, 130, 550)
    brick3 = vykresli_obdlznik(335, 600, 240, 550)
    brick4 = vykresli_obdlznik(445, 600, 350, 550)
    brick5 = vykresli_obdlznik(555, 600, 460, 550)
    brick6 = vykresli_obdlznik(665, 600, 570, 550)
    brick7 = vykresli_obdlznik(775, 600, 680, 550)
    brick8 = vykresli_obdlznik(885, 600, 790, 550)
    brick9 = vykresli_obdlznik(995, 600, 900, 550)

    #bricky 2.rad
    brick10 = vykresli_obdlznik(115, 485, 20, 535)
    brick11 = vykresli_obdlznik(225, 485, 130, 535)
    brick12 = vykresli_obdlznik(335, 485, 240, 535)
    brick13 = vykresli_obdlznik(445, 485, 350, 535)
    brick14 = vykresli_obdlznik(555, 485, 460, 535)
    brick15 = vykresli_obdlznik(665, 485, 570, 535)
    brick16 = vykresli_obdlznik(775, 485, 680, 535)
    brick17 = vykresli_obdlznik(885, 485, 790, 535)
    brick18 = vykresli_obdlznik(995, 485, 900, 535)

    #bricky 3.rad
    brick19 = vykresli_obdlznik(115, 470, 20, 420)
    brick20 = vykresli_obdlznik(225, 470, 130, 420)
    brick21 = vykresli_obdlznik(335, 470, 240, 420)
    brick22 = vykresli_obdlznik(445, 470, 350, 420)
    brick23 = vykresli_obdlznik(555, 470, 460, 420)
    brick24 = vykresli_obdlznik(665, 470, 570, 420)
    brick25 = vykresli_obdlznik(775, 470, 680, 420)
    brick26 = vykresli_obdlznik(885, 470, 790, 420)
    brick27 = vykresli_obdlznik(995, 470, 900, 420)

    #vykresli skore
    score=nakresli_text(str(skore[0]),x=ODSADENIE_TEXTU,y = VYSKA- ODSADENIE_TEXTU - VELKOST_FONTU,pozice_x='left')

    print(stisk_klavesnice)


window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
    on_key_press=stisk_klavesnice,
    on_key_release=pusti_klavesnice,
)

pyglet.app.run()
