import Member
import Cities
import random

__author__ = 'Jenna'


class Population:
    """
    Runs the genetic algorithm.
    """

    # creates a population of 1,
    # just like my love life
    def __init__(self, num_cities):
        self.population = []
        self.cities = Cities.Cities(num_cities)
        self.POPULATION_SIZE = num_cities
        self.population_ranking = []

    # fills in the rest of the population array
    # with many random members for starting population
    def start_population(self):
        for x in range(0, self.POPULATION_SIZE):
            member = Member.Member(self.cities)
            member.new_random_permutation()
            self.population.append(member)

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
        mother_index = self.select_parent()
        father_index = self.select_parent()
        while mother_index <= father_index:
            mother_index = self.select_parent()

    # insertion sort to aid in the sorting of the ranking
    # THERE NEEDS TO BE FITNESS COMPARISON, NOT MEMBER COMPARISON
    def insertion_sort(self, array):
        """

        :param array:
        :type array: list
        :return:
        """
        for x in range(1, len(array)):
            current = array[x].get_fitness(array[x])
            current_member = array[x]
            pos = x
            next_fit = array[x].get_fitness(array[pos - 1])

            while pos > 0 and next_fit > current:
                array[pos] = array[pos - 1]
                pos -= 1
            array[pos] = current_member
        return array

    # getter method for population ranking that
    # sorts the ranking before returning it
    def get_population_ranking(self):
        ranking = self.insertion_sort(self.population_ranking)
        return ranking

    # create a child member
    def create_child(self, parent1, parent2):
        child = Member.Member(len(parent1))
        return child

def main():
    p = Population(3)
    p.start_population()
    p.population[0].new_random_permutation()
    p.insertion_sort(p.population)
    for x in range(0, len(p.population)):
        print(p.population[x])

if __name__ == '__main__':
    main()
