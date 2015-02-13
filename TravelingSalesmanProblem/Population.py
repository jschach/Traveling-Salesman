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
    def __init__(self, num_cities, population_size, mutation_rate):
        self.population = []
        self.cities = Cities.Cities(num_cities)
        self.POPULATION_SIZE = population_size
        self.num_cities = num_cities
        self.mutation_rate = mutation_rate
        self.start_population()
        self.population_children = []


    # # gets mutation rate
    # def get_mutation_rate(self):
    #     return self.mutation_rate

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
        num1 = random.randint(0, len(self.population) - 1)
        num2 = random.randint(0, len(self.population))
        # selects the lower ranked parent
        if num1 <= num2:
            return num1
        else:
            return num2

    # insertion sort to aid in the sorting of the ranking
    # returns where the value was placed in the population list
    def insert(self, index):
        previous = index - 1
        current = self.population[index]
        current_fitness = current.get_fitness()

        while previous >= 0 and self.population[previous].get_fitness() \
                > current_fitness:
            self.population[previous + 1] = self.population[previous]
            previous -= 1

        self.population[previous + 1] = current

        return previous + 1

    # getter method for population
    def get_population(self):
        return self.population

    # create a child member
    def create_child(self):
        # initialize local members
        child = Member.Member(self.cities)
        new_route = []
        best_distance = self.cities.get_total_distance()
        # indexes of best cities in one of the parents
        best_two_cities = [0, 0]

        # select the parents
        parent1 = self.population[self.select_parent()]
        parent2 = parent1
        while parent1 == parent2:
            parent2 = self.population[self.select_parent()]


        # check for best distance between cities of each parents
        # and keep those two cities in the child
        for x in range(0, self.num_cities - 1):
            temp1 = self.cities.get_specified_distance(parent1.get_route()[x],
                                                       parent1.get_route()[x + 1])
            if temp1 < best_distance:
                best_distance = temp1
                best_two_cities[0] = x
                best_two_cities[1] = x + 1
            temp2 = self.cities.get_specified_distance(parent2.get_route()[x],
                                                       parent2.get_route()[x + 1])
            if temp2 < best_distance:
                best_distance = temp2
                best_two_cities[0] = x
                best_two_cities[1] = x + 1

        new_route.append(best_two_cities[0])
        new_route.append(best_two_cities[1])

        # put the rest of the cities from the parent with the best fitness
        # into the array
        if parent2.get_fitness() > parent1.get_fitness():
            for x in range(0, len(parent1.get_route())):
                if parent1.get_route()[x] != best_two_cities[0] \
                        and parent1.get_route()[x] != best_two_cities[1] \
                        and len(new_route) < self.num_cities:
                    new_route.append(parent1.get_route()[x])

        elif parent2.get_fitness() <= parent1.get_fitness():
            for x in range(0, len(parent2.get_route())):
                if parent2.get_route()[x] != best_two_cities[0] \
                        and parent2.get_route()[x] != best_two_cities[1]\
                        and len(new_route) < self.num_cities:
                    new_route.append(parent2.get_route()[x])

        child.set_route(new_route)
        return child

    # runs the genetic algorithm once
    def run_algorithm(self):
        num_new_child = int(self.POPULATION_SIZE * .7)
        self.population = self.population[:-num_new_child]
        for x in range(0, num_new_child):
            child = self.create_child()
            rand = random.randint(1, 100)
            if rand <= (self.mutation_rate * 100):
                child.mutate()
            self.population.append(child)
            self.insert(len(self.population) - 1)




def main():
    p = Population(20, 5, 0.5)
    p.run_algorithm()
    for x in range(0, len(p.population)):
        print(p.population[x])
        print(p.population[x].get_fitness())





if __name__ == '__main__':
    main()
