import random
import copy
import array
import binascii
from array import *

__author__ = 'Jenna'

# copy method to create another cities object
# with the same attributes
def copy_cities(Cities):
    return copy.copy(Cities)

class Cities:
    """ Class initializes the city objects, used for the
    generations in the genetic algorithm. Each cities object contains
    a number of cities and the distance between each in the order
    of which they come in the array.
    """

    # constructor for Cities creates list of cities
    def __init__(self, items):
        # field for max distance allowed between two cities
        self.DISTANCE = 50
        self.NUM_OF_CITIES = items
        self.distance_matrix = {}
        self.create_distances()


    def get_NUM_OF_CITIES(self):
        return self.NUM_OF_CITIES

    # generates the distances between each city
    def create_distances(self):
        # put random distances into HALF of the matrix for cities
        # to generate no differing distances between any two cities
        for x in range(0, self.NUM_OF_CITIES):
            for y in range(0, self.NUM_OF_CITIES):
                temp = random.randint(1, self.DISTANCE)
                self.distance_matrix[(x, y)] = temp
                if x == y:
                    self.distance_matrix[(x, y)] = 0
                print(self.distance_matrix[(x, y)])
        print(self.distance_matrix)

    # gets matrix of distances
    def get_matrix(self):
        return self.distance_matrix

    # gets max distance between cities
    def get_DISTANCE(self):
        return self.DISTANCE

    # gets the distance from a specified city to another
    def get_specified_distance(self, city1, city2):
        if city1 <= -1 or city1 > self.NUM_OF_CITIES:
            raise LookupError("city1 is out of range")

        if city2 > self.NUM_OF_CITIES:
            raise LookupError("city2 is out of range")
        return self.distance_matrix[(city1, city2)]

    # gets the distance between all points of the
    # Cities object
    def get_total_distance(self):
        distance = 0
        for x in range(0, self.NUM_OF_CITIES):
            for y in range(0, self.NUM_OF_CITIES):
                distance += self.distance_matrix[(x, y)]
        return distance


def main():
    c = Cities(5)

if __name__ == '__main__':
    main()