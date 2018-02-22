from turtle import Turtle
import time


class NinjaTurtle(Turtle):
    # inherits from ^^ Turtle

    # This is the constructor. It's what's run whenever
    # you create a new ninja turtle
    def __init__(self, color, skill_level):
        # call parent class constructor
        # this sets up all the basic turtle stuff
        Turtle.__init__(self)

        # make standard turtle more ninja-like
        self.shape("turtle")
        self.speed("fastest")

        # set instance variables
        # (stuff that's unique to each ninja turtle)
        self.color(color)
        self.mad_skills = skill_level

    def loss(self):
        # blink once
        self.hideturtle()
        time.sleep(.1)
        self.showturtle()
        # TODO: have the turtle blinks 5 times

    def victory_dance(self):
        self.forward(3)
        # TODO: create a victory dance
