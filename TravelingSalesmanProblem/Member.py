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
        for x in range(0, len(cities)):
            self.route.append(-1)
        # initialize boolean visited array
        for x in range (0, len(cities)):
            self.visited.append(False)
    
