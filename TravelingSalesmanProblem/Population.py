import Member.py
import Cities.pv
import random

__author__ = 'Jenna'


class Population:
    """ Runs the genetic algorithm.
    """

    # creates a population of 1,
    # just like my love life
    def __init__(self, num_cities):
        self.population = []
        self.start_member = Member(15)
        self.population.append(self.start_member)
        self.POPULATION_SIZE = 199
        self.population_ranking = []

    # fills in the rest of the population array
    # with many random members for starting population
    def start_population(self):
        for x in range(0, self.POPULATION_SIZE):
            self.population.append\
                (self.start_member.new_permutation())

    # selects a random parent with the probability of choosing
    # a better parent over a worse parent (1*n/sum(POPULATION_SIZE)
    # where n = POPULATION_SIZE-- starting from the best ranked parent
    def select_parent(self):
        num1 = random.randint(0, self.POPULATION_SIZE - 1)
        num2 = random.randint(0, self.POPULATION_SIZE)
        # selects the lower ranked parent
        if num1 <= num2:
            return num1
        else:
            return num2

    # selects the parents from the select_parent method
    def get_parents(self):
        mother_index = self.population.select_parent()
        father_index = self.population.select_parent()
        while mother_index <= father_index:
            mother_index = self.population.select_parent()

    def get_population_ranking(self):
        return 0