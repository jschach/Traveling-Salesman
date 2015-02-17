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
        self.MAX_DISTANCE = 50\
                            * (50 - 1)
        # initialize route
        # route might be useless, decide what to do later
        for x in range(0, self.cities.get_NUM_OF_CITIES()):
            self.route.append(x)

    def set_route(self, route):
        self.route = route

    def get_route(self):
        return self.route

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
            while visited[z] is True:
                   z = random.randint(0, self.num_cities - 1)
            self.route.append(z)
            visited[z] = True

        # mutate the route by switching three random elements
    def mutate(self):
        route = self.get_route()
        first = random.randint(0, len(route) - 1)
        second = first
        third = first
        while first == second:
            second = random.randint(0, len(route) - 1)
        while third == first or third == second:
            third = random.randint(0, len(route) - 1)
        temp = route[first]
        temp2 = route[second]
        route[first] = route[third]
        route[second] = temp
        route[third] = temp2
        self.set_route(route)

    # creates a copy of a new member from
    # an existing member
    def new_member(self, Member):
        new_mem = Member(self.cities)
        return new_mem

    def get_cities(self):
        return self.cities

    # scores the fitness of the member array
    # using the total distance between points
    def get_fitness(self):
        score = 0
        y = 1
        for x in range(0, self.num_cities - 1):
            score += self.get_cities().get_specified_distance(self.route[x], self.route[y])
            y += 1
        score += self.get_cities().get_specified_distance(self.route[self.num_cities - 1], self.route[0])
        return score




    def __str__(self):
        return repr(self.route)