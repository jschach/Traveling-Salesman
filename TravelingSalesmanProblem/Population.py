import Member.py
import Cities.pv

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

    # fills in the rest of the population array
    # with many random members for starting population
    def start_population(self):



    def select_parents(self):
