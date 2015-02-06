import Cities
import random

__author__ = 'Jenna'

class Member:
    """
    Uses and creates new member objects to be used
    in the genetic algorithm operation.
    """

    # constructor to create member, taking a Cities object
    # initializes path field
    def __init__(self, num_cities):
        self.cities = Cities(num_cities)
        self.route = []
        self.visited = []
        self.MAX_DISTANCE = Cities.DISTANCE * (num_cities - 1)
        # initialize route
        # route might be useless, decide what to do later
        for x in range(0, len(self.cities)):
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

    # scores the fitness of the member array
    # using the total distance between points
    def get_fitness(self, Member):
        score = Member.get_total_distance()
        return score
