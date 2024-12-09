"""
    Tom Howes
    CS 5001 - Fall 24
    Final Project
"""

import turtle

class Gameboard:
    """ This class is used to draw the game UI including
        the real-time player status, leaderboard and main
        play frame
    """

    def __init__(self):
        """ Initializes the pen to draw the game UI """
        self.gb = turtle.Turtle()
        self.gb.up()
        self.gb.hideturtle()
        self.gb.speed(0)
        self.gb.pensize(5)
    
    def draw_status(self):
        """ Draws the status box at the bottom """
        self.gb.setpos(-425, -300)
        self.gb.fillcolor("white")
        self.gb.begin_fill()
        self.gb.down()
        for i in range(2):
            self.gb.fd(650)
            self.gb.left(90)
            self.gb.fd(100)
            self.gb.left(90)
        self.gb.end_fill()
        self.gb.up()
        self.gb.setpos(-416, -200)
        self.gb.write("Status", font=("Tsuki", 15))
        self.gb.setpos(-380, -230)
        self.gb.write("Moves:", font=("Tsuki", 12))
        self.gb.setpos(-290, -230)
        self.gb.write("Matches:", font=("Tsuki", 12))
    
    def draw_leaderboard_frame(self):
        """ Draws the frame for the leaderboard """
        self.gb.setpos(275, -170)
        self.gb.pencolor("blue")
        self.gb.fillcolor("white")
        self.gb.begin_fill()
        self.gb.down()
        for i in range(2):
            self.gb.fd(150)
            self.gb.left(90)
            self.gb.fd(480)
            self.gb.left(90)
        self.gb.up()
        self.gb.end_fill()
        self.gb.setpos(350, 310)
        self.gb.write("Leaderboard", align="center", font=('Tsuki', 15))
    
    def draw_play_frame(self):
        """ Draws the frame for the main play area """
        self.gb.setpos(-425, -170)
        self.gb.pencolor("black")
        self.gb.fillcolor("mediumspringgreen")
        self.gb.begin_fill()
        self.gb.down()
        for i in range(2):
            self.gb.fd(650)
            self.gb.left(90)
            self.gb.fd(520)
            self.gb.left(90)
        self.gb.up()
        self.gb.end_fill()    
