from abc import ABC, abstractmethod
from .player import Player
from .game_display.input_tools import *
import click
class Choice:
    """
    Class representing the choices that the user sees on the screen coupling it with the corresponding functionality.
    """
    def __init__(self, name, method, args, menu):
        """
        Initializes Choice
        """
        self.name = name
        #Method should be a method that is invoked when the choice is requested by the user
        self.method = method
        #args should be a tuple
        if args==None:
            self.args = ()
        else:
            self.args = args
        #Menu is the menu that the choice requires when the game moves to the appropriate screen
        #If it's None, no changes are necessary
        self.menu = menu
    def __str__(self):
        return "Name:{} Method:{} Menu:{}".format(self.name,self.method,self.menu)

class Game(ABC):
    """
    Generic Abstract Game Class
    """
    END_GAME = 0
    COMPUTER_NAME = "Computer"
    def __init__(self, display, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.menu = None
        self.prev_menu = None
        self.display = display

    def start(self):
        """
        Plays the game. While still_playing is True keep playing.
        Note that it calls self.tick(). 
        """
        still_playing = True
        while still_playing:
            still_playing = self.tick() 

    def tick(self):
        """
        Invokes the game's logic.
        Returns False if the user has requested to end the game. True otherwise.
        """
        #choice = self.display.actions_menu(self.menu)
        choice = enter_next_action("Enter next action: ", self.menu, self.display)
        if choice.menu != None:
            self.prev_menu = self.menu
            self.menu = self.menus[choice.menu]
        #calls the appropriate method for choice 
        choice.method(*tuple(choice.args))
        return choice.method!=self.end_game

    def save_game(self):
        """
        Saves the game to be reloaded at a future time
        """
        pass

@click.command()
def cli():
    click.echo("Ascii Game")

if __name__ == '__main__':
    cli()
