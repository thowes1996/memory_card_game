"""
    Tom Howes
    CS 5001 - Fall 24
    Final Project
"""

import turtle

class Leaderboard:
    """ This class handles the leaderboard, it can add new leaders,
        update the leaderboard UI in real-time and write the leaderboard
        to a txt file
    """

    def __init__(self):
        """ Creates the trutle pen that updates the leaderboard """
        self.leaderboard = []
        self.high_scores = turtle.Turtle()
        self.high_scores.hideturtle()
        self.high_scores.pencolor("blue")
        self.high_scores.up()
    
    def add_leaders(self, player, score):
        """ Adds a new leader to the list """
        self.leaderboard.append((player, score))
    
    def get_leaderboard(self):
        return self.leaderboard
    
    def update_leaderboard(self):
        """ Sorts the leaderboard list and then writes the first 8 scores, 
            removing any additional scores and then the sorted 
            leaderboard of length 8 is assigned to the objects 
            leaderboard list
        """
        self.high_scores.clear()
        self.high_scores.setpos(350, 310)
        self.high_scores.setheading(270)
        sorted_leaderboard = sorted(self.leaderboard, key= lambda x: x[1])
        while len(sorted_leaderboard) > 8:
            sorted_leaderboard.pop()
        for player in sorted_leaderboard:
            self.high_scores.fd(48)
            self.high_scores.write(f"{player[0]}:   {player[1]}", \
                                   align="center", font=("Tsuki", 12))
        self.leaderboard = sorted_leaderboard
    
    def write_leaderboard(self):
        """ Writes the leaderboard to a txt file """
        with open("leaders.txt", "w") as ldb:
            for player in self.leaderboard:
                ldb.write(f"{player[0].title()} {player[1]}\n")

    def __str__(self):
        """ Prints each player in the leaderboard and their score """
        ldrs = ""
        for player in self.leaderboard:
            ldrs +=  f"{player}: {str(self.leaderboard[player])}\n"
        return ldrs
    
    def __eq__(self, other):
        if len(self.leaderboard) != len(other):
            return False
        for score in self.leaderboard:
            if score not in other:
                return False
        return True

class Status:
    """ Class that keeps track of and writes moves/matches
        for the current player 
    """

    def __init__(self, status: dict):
        """ Stores the dictionary of player moves/matches
            in the object's attribute 
        """
        self.status = status
        self.scores = turtle.Turtle()
        self.scores.hideturtle()
        self.scores.up()
    
    def update_status(self):
        """ Updates status periodically with new moves/matches data """
        self.scores.clear()
        self.scores.setpos(-320, -230)
        self.scores.setheading(0)
        self.scores.pencolor("black")
        for key in self.status:
            self.scores.write(f"{self.status[key]}", font=("Tsuki", 12))
            self.scores.fd(100)
    
    def __str__(self):
        return f"Moves: {self.status["Moves"]} Matches: \
            {self.status["Matches"]}"