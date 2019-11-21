# -*- coding: utf-8 -*-

"""
An object-oriented implementation of a Snakes & Ladders simulator.
"""

__author__ = 'Anders Mathiesen, Kristian Kramås'
__email__ = 'andermat@nmbu.no, kristiakr@nmbu.no'


import random


class Board:
    """
    Manages all information about ladders, snakes, and the goal.

    Attributes
    ----------
    ladders : list of tuples
        List of snakes (or chutes), giving positions and how many steps up
        the player must move.
    chutes : list of tuples
        List of snakes (or chutes), giving positions and how many steps down
        the player must move.
    goal : int
        Position of goal.
    """
    def __init__(self,
                 ladders=[(1, 39), (8, 2), (36, 16), (43, 19), (49, 30),
                          (65, 17), (68, 14)],
                 chutes=[(24, 19), (33, 30), (42, 12), (56, 19), (64, 37),
                         (74, 62), (87, 17)], goal=90
                 ):
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, current_pos):
        return current_pos <= self.goal

    def position_adjustment(self, current_pos):
        for ladder in self.ladders:
            if ladder[0] == current_pos:
               return ladder[1]
        for chute in self.chutes:
            if chute[0] == current_pos:
               return chute[1]*-1
        return 0


class Player:
    """
    Manages information about player position, including information on which
    board a player “lives”.

    Attributes
    ----------
    board : object
        Which board the player "lives" on.
    position : int
        The players current position.
    """
    def __init__(self, board):
        self.board = board
        self.position

    def move(self):
        """
        The move() method moves the player by implementing a die cast, the
        following move and, if necessary, a move up a ladder or down a chute.
        """
        self.position += random.randint(1, 6)
        self.position += self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    """
    This is a subclass of Player with slightly different moving behavior:
    When a resilient player slips down a chute, he will take extra steps in
    the next move, in addition to the roll of the die. The number of extra
    steps is provided as an argument to the constructor, default is 1.
    Extra steps are taken immediately after the steps prescribed by the die
    and before snakes and ladders are checked.

    Attributes
    ----------
    board : object
        Which board the player "lives" on.
    position : int
        The players current position.
    get_extra_steps : bool
        If the player slipped the last round and will take extra steps.
    extra_steps : int
        Amount of extra steps to be taken.
    """
    def __init__(self, extra_steps=1):
        super().__init__()
        self.get_extra_steps = False
        self.extra_steps = extra_steps

    def move(self):
        self.position += random.randint(1, 6)
        if self.get_extra_steps:
            self.position += self.extra_steps
            self.get_extra_steps = False
        change_in_position = self.board.position_adjustment(self.position)
        if change_in_position < 0:
            self.get_extra_steps = True
        self.position += change_in_position


class LazyPlayer(Player):
    """
    This is a subclass of Player as well. After climbing a ladder, a lazy
    player drops a given number of steps. The number of dropped steps is an
    optional argument to the constructor, default is 1.
    The player never moves backward: if, e.g., the die cast results in 1 step
    and the player is to drop 3 steps, the player does not move -2 steps
    but just stays in place.

    Attributes
    ----------
    board : object
        Which board the player "lives" on.
    position : int
        The players current position.
    get_dropped_steps : bool
        If the player moved up and will drop some steps.
    dropped_steps : int
        Amount of extra steps to be dropped.
    """
    def __init__(self, dropped_steps=1):
        super().__init__()
        self.get_dropped_steps = False
        self.dropped_steps = dropped_steps

    def move(self):
        steps = random.randint(1, 6)
        if self.get_dropped_steps:
            steps -= self.dropped_steps
            if steps < 0:
                steps = 0
            self.get_dropped_steps = False
        self.position += steps
        change_in_position = self.board.position_adjustment(self.position)
        if change_in_position > 0:
            self.get_dropped_steps = True
        self.position += change_in_position


class Simulation(players, randomize_players):
    def __init__(self):
        """
        Initialise the simulation
        """
        pass

    def single_game(self):
        """
        Run a single game

        Returns
        ---------
        best_player : tuple
            Tuple of the winner's moves and type
            moves : int
                Number of moves made
            winner_type : str
                The type of the winner
        """
        pass

    def run_simulation(self, games):
        """
        Runs a given number of games and stores the results in the Simulation
        object.
        """

    def get_results(self):
        """
        Returns all results generated by run_simulation(),
        calls so far as a list of result tuples, e.g.
        [(10, 'Player'), (6, 'ResilientPlayer')].

        Returns
        -------
        moves : int
            Number of moves made
        winner_type : str
            The type of the winner
        """
        pass

    def winners_per_type(self):
        """
        Returns a dictionary mapping player types to the number of wins, e.g.,
        {'Player': 4, 'LazyPlayer': 2, 'ResilientPlayer': 5}

        Returns
        -------
        winners_per_type : dict
            Dictionary mapping player types to the number of wins
        """
        pass

    def durations_per_type(self):
        """
        Returns a dictionary mapping player types to lists of game durations
        for that type, e.g.,
        {'Player': [11, 25, 13],
        'LazyPlayer': [39],
        'ResilientPlayer': [8, 7, 6, 11]}

        Returns
        -------
        durations_per_type : dict
            Dictionary mapping player types to lists of game durations
            for that type
        """
        pass

    def players_per_type(self):
        """
        Returns a dictionary showing how many players of each type
        participate, e.g.,
        {'Player': 3, 'LazyPlayer': 1, 'ResilientPlayer': 0}

        Returns
        -------
        players_per_type : dict
            Dictionary showing how many players of each type
        """
        pass


if __name__ == "__main__":
    pass
