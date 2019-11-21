# -*- coding: utf-8 -*-

"""
Extended set of tests for PA02.
"""

__author__ = 'Anders Mathiesen, Kristian Kramås'
__email__ = 'andermat@nmbu.no, kristiakr@nmbu.no'


import src.pa02.chutes_simulation as cs
import pytest


class TestBoard:
    """
    Additional tests for Board class.
    """
    pass


class TestPlayer:
    """
    Additional tests for Player class.
    """
    def test_position_positive(self):
        """position positive after move"""
        b = cs.Board()
        p = cs.Player()
        p.move()
        assert(p.position > 1)

    def function(self):
        """description"""
        pass

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

