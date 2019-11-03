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
    def __init__(self, x0, home):
        self.home = home
        self.x = x0
        self.x0 = x0
        self.steps = 0

    def move(self):
        self.steps += 1
        if random.randint(0, 1):
            self.x += 1
        else:
            self.x -= 1

    def is_at_home(self):
        if self.x == self.home:
            return True
        return False

    def get_position(self):
        return self.x

    def get_steps(self):
        return self.steps

    def reset(self):
        self.x = self.x0
        self.steps = 0

    def go_home(self):
        while not self.is_at_home():
            self.move()


class Simulation:
    def __init__(self, start, home, seed):
        self.start = start
        self.position = self.start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        steps_take = 0
        while self.position != self.home:
            if random.randint(0, 1):
                self.position += 1
            else:
                self.position -= 1
            steps_take += 1
        return steps_take

    def run_simulation(self, num_walks):
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