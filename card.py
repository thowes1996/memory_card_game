"""
    Tom Howes
    CS 5001 - Fall 24
    Final Project
"""

import turtle

path = "gifs/"

class Card:
    """
    This class imitates a card.
    It allows you to return the "number" (or ID) of the card,
    check if the card is flipped, place the card at an
    (x,y) coordinate, return the position, flip the card face down
    or face up or hide the card if it has been matched.
    """

    def __init__(self, number):
        """ Creates a card, giving it a default card back shape,
            giving it a number and setting it face down
        """
        self.card = turtle.Turtle()
        self.card.shape(f"{path}card_back.gif")
        self.card.up()
        self.number = number
        self.flipped = False
    
    def get_number(self):
        """ Number can be used to ID the card and assign
            it an image
        """
        return self.number
    
    def get_flipped(self):
        """ Checks if card flipped or not """
        return self.flipped
    
    def place(self, x, y):
        """ Places the card at the given x, y coordinate """
        self.card.setpos(x, y)
    
    def get_position(self):
        """ Returns x, y coordinate """
        return self.card.pos()
    
    def update_image(self, cards):
        """ Show front of card (based on number) and set to flipped """
        if self.flipped == True:
            return
        self.card.shape(cards[self.number])
        self.flipped = True

    def reset_flip(self):
        """ Show card back and set to not flipped """
        if self.flipped == True:
            self.card.shape(path + "card_back.gif")
            self.flipped = False
    
    def matched(self):
        """ When matched, hide cards """
        self.card.hideturtle()
        
    def __str__(self):
        """ Print function """
        return f"Card number: {self.number}"

