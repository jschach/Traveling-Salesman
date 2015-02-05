import Cities.py
import random

__author__ = 'Jenna'

class Member:
    """ Uses and creates new member objects to be used
    in the genetic algorithm operation.
    """

    # constructor to create member, taking a Cities object
    # initializes path field
    def __init__(self, cities):
        self.cities = cities
        self.route = []
        self.visited = []
        # initialize route
        # route might be useless, decide what to do later
        for x in range(0, len(cities)):
            self.route.append(-1)



    # creates a random new permutation based on
    # the previous cities collected
    # returns the permutation created
    def new_permutation(self):
        temp = []
        # reset boolean array
        for x in range (0, len(self.cities)):
            self.visited.append(False)
        # create new random permutation with no repetitions
        for x in range(0, len(self.cities)):
            z = random.randint(0, len(self.cities))
            while self.visited[z] == True:
                z = random.randint(0, len(self.cities))
            self.visited[z] = True

    def select_parents(self):