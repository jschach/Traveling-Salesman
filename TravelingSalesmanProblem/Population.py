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
    def __init__(self, num_cities, population_size):
        self.population = []
        self.cities = Cities.Cities(num_cities)
        self.POPULATION_SIZE = population_size

    # fills in the rest of the population array
    # with many random members for starting population
    def start_population(self):
        for x in range(0, self.POPULATION_SIZE):
            member = Member.Member(self.cities)
            member.new_random_permutation()
            self.population.append(member)
            self.insert(x)

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
    # returns where the value was placed in the population list
    def insert(self, index):
        """
        :param array:
        :type array: list
        :return:
        """
        previous = index - 1
        current = self.population[index]
        current_fitness = current.get_fitness()

        while previous > 0 and self.population[previous].get_fitness() > current_fitness:
            self.population[previous + 1] = self.population[previous]
            previous -= 1

        self.population[previous + 1] = current

        return previous + 1

    # getter method for population
    def get_population(self):
        return self.population

    # create a child member
    def create_child(self, parent1, parent2):
        child = Member.Member(len(parent1))
        # THIS METHOD NEEDS EDITING
        # YOU ARE NOT CREATING THE CHILD YOU WANT
        # YOU FILTHY ANIMAL
        return child

def main():
    p = Population(5, 5)
    p.start_population()
    p.population[0].new_random_permutation()
    for x in range(0, len(p.population)):
        print(p.population[x])
        print(p.population[x].get_fitness())
    print("-------------------------------")
    p.get_population()
    for x in range(0, len(p.population)):
        print(p.population[x])
        print(p.population[x].get_fitness())


if __name__ == '__main__':
    main()
