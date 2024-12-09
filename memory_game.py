"""
    Tom Howes
    
    CS 5001 - Fall 24
    Final Project

    This is the Main Driver File for my Memory Card Matching Game
    Read Design.txt for information about the programming design
    and how to use it correctly.
"""

import turtle
import gameboard
import card
from random import randint
import os
import card_deck
import time
import stats
import message

path = "gifs/"

def intro_sequence(screen):
    """ Function to show logo and title text on splash screen """
    screen.register_shape("logo.gif")
    logo = turtle.Turtle()
    logo.shape("logo.gif")
    intro = turtle.Turtle()
    intro.hideturtle()
    intro.up()
    intro.setpos(0, 200)
    intro.write("Tom's Card Game", align="center", \
                font=("Courier New", 50, "bold"))
    return logo, intro

def read_leaderboard(leaderboard):
    """ Function to update leaderboard dict from txt file """
    try:
        with open("leaders.txt", "r") as ldb:
            for line in ldb:
                line = line.split(" ")
                leaderboard.add_leaders(line[0].title(), int(line[1]))
    except FileNotFoundError:
        leaderboard_error = message.Message("leaderboard_error.gif")
        leaderboard_error.show()
        return

def init_button(button, x, y, shape):
    """ Function to create and place button """
    button.up()
    button.shape(path + shape)
    button.setpos(x, y)
    button.showturtle()

def winning_sequence(name, leaderboard, status):
    """ When a player has won, shows winning message, updates leaderboard UI
        and writes updated leaderboard to txt file
    """
    win_message = message.Message("winner.gif")
    win_message.show()
    player_score = [name, status["Moves"]]
    leaderboard.add_leaders(player_score[0], player_score[1])
    leaderboard.update_leaderboard()
    leaderboard.write_leaderboard()
    time.sleep(1)
    quit()

def load_cards(config_file, playing_cards):
    """ Function that loads cards from config file to list of playing cards.
        The user can leave it blank to default to a standard deck of cards 
        or, if the input is not a valid file, it will also be the default
        option.
    """
    try:
        with open(config_file, "r") as cards:
            for img in cards:
                file = path + img.strip()
                if os.path.isfile(file):
                    playing_cards.append(file)
    except FileNotFoundError:
        no_file_message = message.Message("file_error.gif")
        no_file_message.show()
        load_cards("playing_cards.cfg")


def add_positions(x, y, num_cards, positions):
    """ Function to update dictionary of positions with x, y tuples """
    index = 0
    for i in range(3):
        for j in range(4):
            positions[index] = (x, y)
            x += 155
            index += 1
        x = -345
        y -= 172
    
    # Number and arrangement of positions changes 
    # based selected number of cards
    if num_cards == 10:
        del positions[8]
        del positions[11]
    if num_cards == 8:
        del positions[8], positions[9], positions[10], positions[11]
    
def place_cards(positions, deck):
    """ Function that randomly places the 
        'shuffled' deck of cards in positions 
    """
    for i in range(deck.get_length()):
        # Randomize num until it is in positions dict
        num = randint(0, 11)
        while num not in positions:
            num = randint(0, 11)
        # Place card at that position and delete from dict
        deck.get_card(i).place(positions[num][0], positions[num][1])
        del positions[num]


def main():

    # Create screen object and maximize
    screen = turtle.Screen()
    screen.setup(width = 1.0, height = 1.0)

    # Intro Sequence for Splash Screen
    logo, intro = intro_sequence(screen)

    # Initialize objects and data structures to be used by the program
    status = {"Moves": 0, "Matches": 0}
    playing_cards = []
    leaderboard = stats.Leaderboard()
    player_status = stats.Status(status)
    game = gameboard.Gameboard()
    deck = card_deck.CardDeck()
    config_button = turtle.Turtle()
    config_button.hideturtle()
    quit_button = turtle.Turtle()
    quit_button.hideturtle()


    # Register shapes, saving them in a list of gifs
    gifs = []
    for filename in os.listdir(path):
        screen.register_shape(f"{path}{filename}")
        gifs.append(filename)

    time.sleep(2)
    logo.hideturtle()

    # Get valid user input for name and card deck to start game
    player_name = ""
    while player_name == "":
        player_name = screen.textinput("NAME", "Enter Player Name:").title().strip(" ")
    config_file = screen.textinput("DECK",\
                                    "Enter Config File (Leave Blank For Default):")
    if config_file == "":
        config_file = "playing_cards.cfg"

    # Get valid user input for size of deck
    num_cards = int(screen.textinput("CARDS", "Enter Number of Cards (8, 10 or 12):"))
    while (num_cards != 8 and num_cards != 10 and num_cards != 12):
        num_cards = int(screen.textinput("CARDS", \
                                         "Invalid Value, Try Again (8, 10 or 12):"))
    
    intro.clear()

    # load up leaderboard txt -> list and active cards config_file -> list
    read_leaderboard(leaderboard)
    load_cards(config_file, playing_cards)

    # Draw background frames for card area, status & leaderboard
    screen.bgcolor("green")
    game.draw_status()
    game.draw_play_frame()
    game.draw_leaderboard_frame()

    # Add quit and settings buttons    
    init_button(quit_button, x = 300, y = -240, shape="quitbutton.gif")
    init_button(config_button, x = 405, y = -240, shape="settings.gif")

    # Update status and leaderboard to reflect most recent stats
    leaderboard.update_leaderboard()
    player_status.update_status()

    # Generate random order of pairs of cards
    chosen = []
    while len(chosen) < num_cards // 2: 
        number = randint(0, 5)
        if number not in chosen:
            chosen.append(number)

    # Initialize pairs of cards based on random order
    for i in range(len(chosen)):
        deck.add_card(card.Card(number=chosen[i]))
        deck.add_card(card.Card(number=chosen[i]))

    # Create dictionary of x, y coordinates to place cards
    positions = {}
    x, y = (-345, 260)
    add_positions(x, y, num_cards, positions)


    # randomize card positioning and place them accordingly
    place_cards(positions, deck)

    ### Handle button and card clicks ###
    
    def card_clicked(x, y):
        """ Function to get position of cards and handle score updates """
        # Register card clicks
        for i in range(deck.get_length()):
            (cardx, cardy) = deck.get_card(i).get_position()
            if (x + 49) > cardx > (x - 49) and (y - 72) < cardy < (y + 72):
                # flip clicked card
                deck.get_card(i).update_image(playing_cards)
        # if 2 cards are flipped check if they match
        if deck.check_flipped() >= 2:
            time.sleep(0.5)
            # if they match increment status of matches and remove cards
            if deck.check_match():
                status["Matches"] += 1
            # unflip all cards
            deck.reset_cards()
            status["Moves"] += 1
            # update status writing
            player_status.update_status()
            # check if the player has won and initiate win sequence
            if deck.check_win():
                winning_sequence(player_name, leaderboard, status)

    screen.onclick(card_clicked)

    def leave_game(x, y):
        """ Function to handle quit button clicks and leave the game """
        if 271 < x < 327 and -259 < y < -220:
            quit_message = message.Message("quitmsg.gif")
            quit_message.show()
            screen.bye()
            quit()
    quit_button.onclick(leave_game)

    def config_deck(x, y):
        """ Function to allow user to change deck gifs by 
            clicking the settings button 
        """
        if 380 < x < 427 and -264 < y < -213:
            config_file = screen.textinput("DECK", \
                                           "Enter Name of Config File: ")
            playing_cards.clear()
            load_cards(config_file, playing_cards)
    
    config_button.onclick(config_deck)  

    turtle.mainloop()
    
if __name__ == "__main__":
    main()