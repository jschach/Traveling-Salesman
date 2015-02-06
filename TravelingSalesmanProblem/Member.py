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
        self.cities = Cities.Cities(num_cities)
        self.route = []
        self.visited = []
        self.num_cities = num_cities
        self.MAX_DISTANCE = self.cities.get_DISTANCE() * (num_cities - 1)
        # initialize route
        # route might be useless, decide what to do later
        for x in range(0, num_cities):
            self.route.append(-1)

    # creates a random new permutation based on
    # the previous cities collected
    # returns the permutation created
    def new_random_permutation(self):
        temp = []
        # reset boolean array
        for x in range (0, self.num_cities):
            self.visited.append(False)
        print(len(self.visited))
        # create new random permutation with no repetitions
        for x in range(0, self.num_cities):
            z = random.randint(0, self.num_cities - 1)
            print(z, "<<< randomly generated")
            print(self.visited[z], "<<< is z visited")
            while (self.visited[z] == True):
                   z = random.randint(0, self.num_cities - 1)
            self.visited[z] = True

    # creates a copy of a new member from
    # an existing member
    def new_member(self, Member):
        cities = Member.copy_cities(self.num_cities)


    # scores the fitness of the member array
    # using the total distance between points
    def get_fitness(self, Member):
        score = Member.get_total_distance()
        return score

