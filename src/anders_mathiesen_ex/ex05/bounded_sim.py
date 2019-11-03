# -*- coding: utf-8 -*-

__author__ = 'Anders Mathiesen'
__email__ = 'andermat@nmbu.no'


from walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    """
    Initialise the walker

    Arguments
    ---------
    start : int
        The walker's initial position
    home : int
        The walk ends when the walker reaches home
    left_limit : int
        The left boundary of walker movement
    right_limit : int
        The right boundary  of walker movement
    """
    def __init__(self, start, home, left_limit, right_limit):
        super().__init__(start, home)
        self.steps_to_go_home = None
        while left_limit < self.get_position() < right_limit:
            self.move()
            if self.is_at_home():
                self.steps_to_go_home = self.get_position()
                break
        self.reset()

        def __repr__(self):
            return "<Test a:%s>" % (self.steps_to_go_home)




class BoundedSimulation(Simulation):
    """
    Initialise the simulation

    Arguments
    ---------
    start : int
        The walker's initial position
    home : int
        The walk ends when the walker reaches home
    seed : int
        Random generator seed
    left_limit : int
        The left boundary of walker movement
    right_limit : int
        The right boundary  of walker movement
    """
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.steps_to_go_home = 0
        self.steps_to_go_home = self.single_walk()
        if right_limit < max(self.list_of_position) and left_limit > min(self.list_of_position):
            return None
        else:
            self.steps_to_go_home

        def __repr__(self):
            return "<Test a:%s>" % (self.steps_to_go_home)



if __name__ == "__main__":
    left_boundaries = [0, -10, -100, -1000, -10000]

    for left_boundarie in left_boundaries:
        test = BoundedWalker(0, 20, left_boundarie, 20)
        print(repr(test.steps_to_go_home))
        # test2 = BoundedSimulation(0, 20, 21, left_boundarie, 20)
        # print(repr(test2.steps_to_go_home))

