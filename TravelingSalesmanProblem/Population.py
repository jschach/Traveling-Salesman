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
        self.num_cities = num_cities

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

    # insertion sort to aid in the sorting of the ranking
    # returns where the value was placed in the population list
    def insert(self, index):
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

    # mutate the route by switching three random elements
    def mutate(self, member):
        route = member.get_route()
        first = random.randint(0, len(route))
        second = first
        third = first
        while first == second:
            second = random.randint(0, len(route))
        while third == first or third == second:
            third = random.randint(0, len(route))
        temp = route[first]
        route[first] = route[second]
        route[third] = route[second]
        route[second] = temp
        return route

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
        parent2 = self.population[self.select_parent()]

        # check for best distance between cities of each parents
        # and keep those two cities in the child
        for x in range(0, self.num_cities - 1):
            temp1 = self.cities.get_specified_distance(parent1.get_route()[x], parent1.get_route()[x + 1])
            if temp1 < best_distance:
                best_distance = temp1
                best_two_cities[0] = x
                best_two_cities[1] = x + 1
            temp2 = self.cities.get_specified_distance(parent2.get_route()[x], parent2.get_route()[x + 1])
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
                if parent1.get_route()[x] != best_two_cities[0] and parent1.get_route()[x] != best_two_cities[1]:
                    new_route.append(parent1.get_route()[x])
        elif parent2.get_fitness() <= parent1.get_fitness():
            for x in range(0, len(parent2.get_route())):
                if parent2.get_route()[x] != best_two_cities[0] and parent2.get_route()[x] != best_two_cities[1]:
                    new_route.append(parent2.get_route()[x])

        child.set_route(new_route)
        # THIS METHOD NEEDS EDITING
        # YOU ARE CREATING A MONSTER
        # YOU FILTHY ANIMAL
        return child

def main():
    p = Population(20, 200)
    p.start_population()
    for x in range(0, len(p.population)):
        print(p.population[x])
    p.population[0].new_random_permutation()
    child = p.create_child()
    p.mutate(child)
    p.population[p.POPULATION_SIZE - 1] = child
    for x in range(0, len(p.population)):
        print(p.population[x])


if __name__ == '__main__':
    main()
