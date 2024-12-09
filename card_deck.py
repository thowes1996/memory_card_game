"""
    Tom Howes
    CS 5001 - Fall 24
    Final Project
"""


import turtle
import card

class CardDeck:
    """ This class is used to simulate a deck of cards with a list. It can 
        add cards, return its size, return a card at a given index, reset 
        all cards to be face-down, check if cards have been flipped over 
        and check if the flipped cards match, removing them from the deck.
    """

    def __init__(self):
        """ Creates two lists to represent all cards and flipped cards """
        self.cards = []
        self.flipped_cards = []

    def add_card(self, card):
        """ Adds a card to the list (or deck) of cards """
        self.cards.append(card)
    
    def get_length(self):
        """ Returns the size of the card deck """
        return len(self.cards)
    
    def get_card(self, index):
        """ Returns card at a certain index """
        return self.cards[index]
    
    def reset_cards(self):
        """ Set all cards to not flipped """
        for card in self.cards:
            card.reset_flip()
        self.flipped_cards = []
    
    def check_flipped(self):
        """ Check if cards are flipped and add them to flipped cards list """
        for card in self.cards:
            if card.get_flipped() == True and card not in self.flipped_cards:
                self.flipped_cards.append(card)
        return len(self.flipped_cards)
    
    def check_match(self):
        """ Check if flipped cards match by their number 
            and if so, remove them from deck 
        """
        if self.flipped_cards[0].get_number() == \
            self.flipped_cards[1].get_number():
            self.flipped_cards[0].matched()
            self.flipped_cards[1].matched()
            self.cards.remove(self.flipped_cards[0])
            self.cards.remove(self.flipped_cards[1])
            return True
    
    def check_win(self):
        """ Check if deck is empty and if it is the player has won! """
        if len(self.cards) == 0:
            return True
    
    def __str__(self):
        return self.cards