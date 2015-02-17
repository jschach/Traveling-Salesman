__author__ = 'Jenna'

import Member
import Cities
import Population

class Menu:
    """
    Interface for the genetic algorithm. Have fun!
    """
    def __init__(self):
        self.summary = "***********************************\n* " \
                       "The traveling salesman travels  *"\
                       "\n* to several cities on his route. *\n* " \
                       "What is the most efficient path *"\
                       "\n* for him to take to travel?      *"\
                       "\n***********************************\n"
        self.select_cities = "Please select the number of cities: "
        self.select_mutation_rate = "Please enter the mutation rate in decimal" \
                                    " form (must be less than 1.0): "
        self.select_population_size = "Please specify the population size: "
        self.generate_new_distances = "Would you like to generate new distances?"
        self.num_cities = 0
        self.mutation_rate = 0
        self.pop_size = 0
        self.generate = 'n'

    # runs the genetic algorithm after getting input from the user
    def run(self):
        # get user input before running program
        print(self.summary)
        self.num_cities = 10
        print(self.select_population_size)
        self.pop_size = int(input())
        print(self.select_mutation_rate)
        self.mutation_rate = float(input())
        print(self.generate_new_distances)
        self.generate = str(input())
        self.cities = Cities.Cities(self.num_cities)



        # use user input to create population object
        # and use them in the algorithm
        p = Population.Population(self.num_cities, self.pop_size,
                                  self.mutation_rate, self.cities)
        if self.generate == 'y':
            p.get_cities().generate_distances()
        else:
            p.get_cities().create_distances()

        for x in range(0, 1000):
            p.run_algorithm()
            # top = p.get_population()[0]
            # print("First place is: ", top, " with ", top.get_fitness())
        for x in range(0, self.pop_size - 1):
            print(p.get_population()[x], " with ", p.get_population()[x].get_fitness())

def main():
    m = Menu()
    m.run()


if __name__ == '__main__':
    main()