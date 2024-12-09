"""
    Tom Howes
    CS 5001 - Fall 24
    Final Project
"""

import turtle
import time

class Message:
    """ This class handles pop up messages for various errors
        and program outcomes e.g. Win, Quit and File not found
    """

    def __init__(self, img):
        """ Message is hidden, moved to default position and then given
            a shape based on the img parameter
        """
        self.message = turtle.Turtle()
        self.message.hideturtle()
        self.message.up()
        self.message.setpos(-100,90)
        self.message.shape(f"gifs/{img}")
    
    def show(self):
        """ Shows the message for 2 seconds """
        self.message.showturtle()
        time.sleep(2)
        self.message.hideturtle()
    
    def __str__(self):
        return self.message.shape()
