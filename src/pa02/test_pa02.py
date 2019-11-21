# -*- coding: utf-8 -*-

"""
Extended set of tests for PA02.
"""

__author__ = 'Anders Mathiesen, Kristian Kramås'
__email__ = 'andermat@nmbu.no, kristiakr@nmbu.no'


import src.pa02.chutes_simulation as cs
# import pytest


class TestBoard:
    """
    Additional tests for Board class.
    """
    pass

    def test_chutes_go_down(self):
        """se """
        b = cs.Board()
        for position in range(b.goal):
            old_position = position
            if b.chutes[0][0] == position:
                chute = True
            else
                chute = False
            new_position = b.position_adjustment(position)
            if chute:
                assert(new_position < old_position)

    def test_ladders_go_up(self):
        """se """
        b = cs.Board()
        b = cs.Board()
        for position in range(b.goal):
            old_position = position
            if b.ladders[0][0] == position:
                ladder = True
            else
                ladder = False
            new_position = b.position_adjustment(position)
            if ladder:
                assert (new_position > old_position)



class TestPlayer:
    """
    Additional tests for Player class.
    """
    def test_position_positive(self):
        """position positive after move"""
        b = cs.Board()
        p = cs.Player()
        for _ in range(20):
            p.move()
            assert(p.position > 0)

    def test_move_changes_position(self):
        """description"""
        b = cs.Board()
        p = cs.Player()
        for _ in range(20):
            old_position = p.position
            p.move()
            assert (p.position != old_position)


class TestResilientPlayer:
    """
    Additional tests for ResilientPlayer class.
    """
    pass


class TestLazyPlayer:
    """
    Additional tests for LazyPlayer class.
    """
    pass


class TestSimulation:
    """
    Additional tests for Simulation class.
    """
    pass

