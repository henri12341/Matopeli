import turtle
import random

class Mato():
    mato = turtle.Turtle()
    mato.speed(0)
    mato.shape("circle")
    mato.color("green")
    mato.penup()
    mato.goto(0, 0)
    dx = 20
    dy = 0

    madon_osat = []
    madon_osat.append(mato)


    def mato_oikealle(self):
        self.dx = 20
        self.dy = 0

    def mato_vasemmalle(self):
        self.dx = -20
        self.dy = 0

    def mato_ylos(self):
        self.dx = 0
        self.dy = 20

    def mato_alas(self):
        self.dx = 0
        self.dy = -20

    def liiku(self):
        i = len(self.madon_osat) - 1
        while i > 0:
            self.madon_osat[i].goto(self.madon_osat[i-1].xcor(), self.madon_osat[i-1].ycor())
            i -= 1
        self.madon_osat[0].goto(self.madon_osat[0].xcor() + self.dx, self.madon_osat[0].ycor() + self.dy)

    def liiku2(self):
        liikutettava_madon_osa = self.madon_osat.pop(1)
        liikutettava_madon_osa.goto(self.madon_osat[0].xcor(), self.madon_osat[0].ycor())
        self.madon_osat.append(liikutettava_madon_osa)
        self.madon_osat[0].goto(self.madon_osat[0].xcor() + self.dx, self.madon_osat[0].ycor() + self.dy)

    def tapa_mato(self):
        for mato in self.madon_osat:
            mato.hideturtle()
        self.madon_osat = []
        self.mato.showturtle()
        self.madon_osat.append(self.mato)
        self.lisaa_osa()
        self.lisaa_osa()
        self.lisaa_osa()
        self.mato.goto(0,0)

    def mene(self, x, y):
        self.mato.goto(x, y)

    def get_xcor(self):
        return self.mato.xcor()

    def get_ycor(self):
        return self.mato.ycor()

    def lisaa_osa(self):
        madon_pituus = len(self.madon_osat) - 1
        uusi_mato = turtle.Turtle()
        uusi_mato.speed(0)
        uusi_mato.shape("circle")
        uusi_mato.color("green")
        uusi_mato.penup()
        uusi_mato.goto(self.madon_osat[madon_pituus].xcor() , self.madon_osat[madon_pituus].ycor())
        self.madon_osat.append(uusi_mato)

def alku_syotti():
    syotti = turtle.Turtle()
    syotti.speed(0)
    syotti.shape("square")
    syotti.color("red")
    syotti.penup()
    syotti.goto(100, 100)
    return syotti

def main():
    window = turtle.Screen()
    window.title("Matopeli")
    window.bgcolor("white")
    window.setup(width=400, height=400)
    window.tracer(1, 1)

    mato = Mato()
    mato.lisaa_osa()
    mato.lisaa_osa()
    mato.lisaa_osa()

    syotti = alku_syotti()

    window.listen()
    window.onkeypress(mato.mato_oikealle, "Right")
    window.onkeypress(mato.mato_vasemmalle, "Left")
    window.onkeypress(mato.mato_ylos, "Up")
    window.onkeypress(mato.mato_alas, "Down")

    pisteet = 0
    teksti = turtle.Turtle()
    teksti.penup()
    teksti.goto(150, -185)
    teksti.write(pisteet)


    #Main game loop
    while True:
        window.update()
        mato.liiku2()
        if mato.get_xcor() < syotti.xcor() + 20 and mato.get_xcor() > syotti.xcor() - 20 and mato.get_ycor() < syotti.ycor() + 20 and mato.get_ycor() > syotti.ycor() - 20:
            mato.lisaa_osa()
            x = random.randint(-200+20, 200-20)
            y = random.randint(-200+20, 200-20)
            syotti.goto(x, y)
            pisteet += 1
            teksti.clear()
            teksti.write(pisteet)

        if pisteet > 14:
            window.delay(50)
        elif pisteet > 10:
            window.delay(60)
        elif pisteet > 5:
            window.delay(70)
        else:
            window.delay(80)


        if mato.get_xcor() < -200 or mato.get_xcor() > 200 or mato.get_ycor() > 200 or mato.get_ycor() < -200:
            mato.tapa_mato()
            window.delay(50)
            teksti.clear()
            pisteet = 0
            teksti.write(pisteet)


        for i in range(1, len(mato.madon_osat)):
            if mato.get_xcor() == mato.madon_osat[i].xcor() and mato.get_ycor() == mato.madon_osat[i].ycor():
                mato.tapa_mato()
                window.delay(50)
                teksti.clear()
                pisteet = 0
                teksti.write(pisteet)
                break
main()
