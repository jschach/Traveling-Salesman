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
    def __init__(self, cities):
        self.cities = cities
        self.route = []
        self.num_cities = cities.get_NUM_OF_CITIES()
        self.MAX_DISTANCE = self.cities.get_DISTANCE() * (self.cities.get_DISTANCE() - 1)
        # initialize route
        # route might be useless, decide what to do later
        for x in range(0, self.cities.get_NUM_OF_CITIES()):
            self.route.append(x)

    # creates a random new permutation based on
    # the previous cities collected
    # returns the permutation created
    def new_random_permutation(self):
        visited = []
        self.route = []
        # reset boolean array
        for x in range (0, self.num_cities):
             visited.append(False)
        # create new random permutation with no repetitions
        for x in range(0, self.num_cities):
            z = random.randint(0, self.num_cities - 1)
            while (visited[z] == True):
                   z = random.randint(0, self.num_cities - 1)
            self.route.append(z)
            visited[z] = True

    # creates a copy of a new member from
    # an existing member
    def new_member(self, Member):
        cities = Member.copy_cities(self.num_cities)

    def get_cities(self):
        return self.cities

    # scores the fitness of the member array
    # using the total distance between points
    def get_fitness(self, cities):
        """
        :param cities:
        :return score:
        :rtype: int
        """
        cities = Cities.copy_cities(self.cities)
        score = cities.get_total_distance()
        return score

    def __str__(self):
        return repr(self.route)