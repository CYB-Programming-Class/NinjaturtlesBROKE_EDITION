from ninja_turtle import NinjaTurtle
import turtle

# this is the main method, the central control system
# where we'll call all our other methods


def main():
    # create screen
    wn = turtle.Screen()
    wn.setup(500, 500, 0, 0)
    wn.bgcolor("black")

    # create turtles
    bob = NinjaTurtle('red', 4)
    bill = NinjaTurtle('blue', 5)
    setup(bob, bill)
    attack(bob, bill)

    wn.exitonclick()


def setup(t1, t2):
    t1.penup()
    t2.penup()
    # move to opposite sides of canvas
    t1.setx(-200)
    t2.setx(200)
    # turn towards center
    t2.setheading(180)


def attack(t1, t2):
    # have turtles go forward until they meet
    while(t1.distance(t2) > 10):
        t1.forward(1)
        t2.forward(1)
        # note: the turtles are running on the same thread so you can't
        # have them go at the same time, so we create the illusion by having
        # each of them take turns taking small steps
    # TODO: determine which turtle won the battle
    # TODO: have the losing turtle blink in defeat, using loss method
    # TODO: have the winner do a victory dance, using victory dance method
    t1.loss()


main()
# ^^ here we actually call our main method
# so something actually happens
