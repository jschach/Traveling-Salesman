import random
from array import *

__author__ = 'Jenna'

class Cities:
    """ Class initializes the city objects, used for the
    generations in the genetic algorithm. Each cities object contains
    a number of cities and the distance between each in the order
    of which they come in the array.
    """

    # constructor for Cities creates list of cities
    def __init__(self, items):

        self.city_list = array('i', [])
        for x in range(0, items):
            self.city_list.append(x)
            print(self.city_list[x])
        self.create_distances()


    # constructor used for manipulation of Cities object
    # create new Cities object based on new set of cities
    def __init__(self, list):
        self.city_list = list

    # generates the distances between each city
    def create_distances(self):
        # initialize matrix before filling it with values
        self.distance_matrix = [[0 for x in range(len(self.city_list))] for x in range(len(self.city_list))]
        # put random distances into HALF of the matrix for cities
        # to generate no differing distances between any two cities
        for x in range(0, len(self.city_list)):
            for y in range (0, x):

                self.distance_matrix[x][y] = random.randint(1, 50)
                if x == y:
                    self.distance_matrix[x][y] = 0
        print(self.distance_matrix)

    # gets matrix of distances
    def get_matrix(self, list):
        return list

    # gets the distance from a specified city to another
    def get_distance(self, city1, city2):
        if city1 <= 0 or city1 > len(self.city_list):
            raise LookupError("city1 is out of range")

        if city2 > city1 or city2 > len(self.city_list):
            raise LookupError("city2 is out of range")
        print(self.distance_matrix[city1][city2])
        return self.distance_matrix[city1][city2]

    # gets the number of cities in this particular object
    def get_number_cities(self):
        return len(self.city_list)




def main():
    c = Cities(5)

if __name__ == '__main__':
    main()