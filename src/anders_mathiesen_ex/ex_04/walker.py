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


if __name__ == "__main__":
    distances_home = [1, 2, 5, 10, 20, 50, 100]
    for distance_home in distances_home:
        walk = Walker(0, distance_home)
        print(walk_multiple_times(5))
