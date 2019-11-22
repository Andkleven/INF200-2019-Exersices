# -*- coding: utf-8 -*-

"""
Extended set of tests for PA02.
"""

__author__ = 'Anders Mathiesen, Kristian Kramås'
__email__ = 'andermat@nmbu.no, kristiakr@nmbu.no'

import random
import src.pa02.chutes_simulation as cs


class TestBoard:
    """
    Additional test(s) for Board class.
    """
    pass

    def test_chutes_go_down(self):
        """chutes go down"""
        b = cs.Board()
        for position in range(b.goal):
            old_position = position
            if b.chutes[0][0] == position:
                chute = True
            else:
                chute = False
            new_position = b.position_adjustment(position)
            if chute:
                assert(new_position < old_position)

    def test_ladders_go_up(self):
        """ladders go up"""
        b = cs.Board()
        for position in range(b.goal):
            old_position = position
            if b.ladders[0][0] == position:
                ladder = True
            else:
                ladder = False
            new_position = b.position_adjustment(position)
            if ladder:
                assert (new_position > old_position)


class TestPlayer:
    """
    Additional test(s) for Player class.
    """
    def test_position_positive(self):
        """position positive after move"""
        b = cs.Board()
        p = cs.Player(b)
        for _ in range(b.goal):
            p.move()
            assert(p.position > 0)

    def test_move_changes_position(self):
        """position changes on move"""
        b = cs.Board()
        p = cs.Player(b)
        for _ in range(b.goal):
            old_position = p.position
            p.move()
            assert (p.position != old_position)

    def test_move_positive(self):
        """move is positive without ladders and chutes"""
        b = cs.Board()
        b.ladders = []
        b.chutes = []
        p = cs.Player(b)
        for _ in range(b.goal):
            old_position = p.position
            p.move()
            assert(p.position > old_position)


class TestResilientPlayer:
    """
    Additional test(s) for ResilientPlayer class.
    """

    def test_resilient_player_is_better(self):
        """checks if resilient players are faster on average"""
        b = cs.Board()
        b.ladders = []
        p = cs.Player(b)
        pr = cs.ResilientPlayer(b, 100)

        p_wins = 0
        pr_wins = 0

        random.seed(12345)

        for _ in range(10000):
            p_count = 0
            pr_count = 0
            p.position = 0
            pr.position = 0

            while p.position < b.goal:
                p.move()
                p_count += 1

            while pr.position < b.goal:
                pr.move()
                pr_count += 1

            if pr_count < p_count:
                pr_wins += 1
            elif p_count < pr_count:
                p_wins += 1

        if p_wins > 0:
            # This factor can be adjusted using statistics,
            # but we won't in this case.
            factor = 2.0
            assert(pr_wins/p_wins > factor)
        elif pr_wins == 0:
            assert False


class TestLazyPlayer:
    """
    Additional test(s) for LazyPlayer class.
    """

    def test_lazy_player_is_worse(self):
        """checks if lazy players are slower on average"""
        b = cs.Board()
        b.chutes = []
        p = cs.Player(b)
        pl = cs.LazyPlayer(b, 100)

        p_wins = 0
        pl_wins = 0

        random.seed(12345)

        for _ in range(10000):
            p_count = 0
            pl_count = 0
            p.position = 0
            pl.position = 0

            while p.position < b.goal:
                p.move()
                p_count += 1

            while pl.position < b.goal:
                pl.move()
                pl_count += 1

            if pl_count < p_count:
                pl_wins += 1
            elif p_count < pl_count:
                p_wins += 1

        if pl_wins > 0 and p_wins > 0:
            # This factor can be adjusted using statistics,
            # but we won't in this case.
            factor = 1.3
            assert (p_wins/pl_wins > factor)
        else:
            assert False

