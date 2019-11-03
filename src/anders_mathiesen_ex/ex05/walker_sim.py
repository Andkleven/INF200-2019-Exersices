# -*- coding: utf-8 -*-

__author__ = 'Anders Mathiesen'
__email__ = 'andermat@nmbu.no'


import random


def walk_multiple_times(times):
    walk_list = []
    for _ in range(times):
        walk.go_home()
        walk_list.append(walk.get_steps())
        walk.reset()
    return walk_list


class Walker:
    """
     Simulate a student’s way home to Pentagon after a hard night at Samfunnet
    """
    def __init__(self, x0, home):
        self.home = home
        self.x = x0
        self.x0 = x0
        self.steps = 0

    def move(self):
        """
        a method move to take one step
        """
        self.steps += 1
        if random.randint(0, 1):
            self.x += 1
        else:
            self.x -= 1

    def is_at_home(self):
        """
        a method is_at_home to check whether the student is at home
        :return:
        boolean
        true if you are home else false
        """
        if self.x == self.home:
            return True
        return False

    def get_position(self):
        """
        a method get_position to access the students current position
        :return:
        int
        true if you are home else false
        """
        return self.x

    def get_steps(self):
        """
        a method get_steps to access the number of steps the student has taken in total
        :return:
        int
        steps take to go home
        """
        return self.steps

    def reset(self):
        """
        a method get_steps to access the number of steps the student has taken in total
        :return:
        int
        steps take to go home
        """
        self.x = self.x0
        self.steps = 0

    def go_home(self):
        """
        simulate a walk home
        """
        while not self.is_at_home():
            self.move()


class Simulation:
    """
     Simulate a person way home
    """
    def __init__(self, start, home, seed):
        self.start = start
        self.position = self.start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        """
       Simulate single walk from start to home, returning number of steps.

       Returns
       -------
       int
           The number of steps taken
       """
        steps_take = 0
        while self.position != self.home:
            if random.randint(0, 1):
                self.position += 1
            else:
                self.position -= 1
            steps_take += 1
        return steps_take

    def run_simulation(self, num_walks):
        """
       Run a set of walks, returns list of number of steps taken.

       Arguments
       ---------
       num_walks : int
           The number of walks to simulate

       Returns
       -------
       list[int]
           List with the number of steps per walk
       """
        list_of_steps = [self.single_walk() for _ in range(num_walks)]
        return list_of_steps




if __name__ == "__main__":
    for _ in range(2):
        test = Simulation(0, 10, 12345)
        print(test.run_simulation(20))
        test = Simulation(10, 0, 12345)
        print(test.run_simulation(20))
    test = Simulation(0, 10, 54321)
    print(test.run_simulation(20))
    test = Simulation(10, 0, 54321)
    print(test.run_simulation(20))