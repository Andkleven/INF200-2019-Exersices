# -*- coding: utf-8 -*-

__author__ = 'Anders Mathiesen, Kristian Kramås'
__email__ = 'andermat@nmbu.no, kristiakr@nmbu.no'


class Board():
    def __init__(self, ladders={1: 39, 8: 2, 36: 16, 43: 19, 49: 30, 65: 17, 68: 14}, snakes={24: -19, 33: -30, 42: -12, 56: -19, 64: -37, 74: -62, 87: -17}, goal=90):
        self.ladders = ladders
        self.snakes = snakes
        self.goal = goal

    def goal_reached(self, current_pos):
        return current_pos <= self.goal

    def position_adjustment(self, current_pos):
        return {**self.snakes, **self.ladders}.get(current_pos, default=0)

