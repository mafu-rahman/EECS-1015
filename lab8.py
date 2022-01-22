#########################
# EECS1015: Lab 8
# Name: Mahfuz Rahman
# Student ID: 217847518
# Email: mafu@my.yorku.ca
#########################

import random

class Bacteria:

    total_bac_object = 0      # Used for counting total bacteria objects

    def __init__(self, chance_of_dividing, max_life_span):
        self.chance_of_dividing = chance_of_dividing
        self.max_life_span = max_life_span
        self.life_span = random.randint(1, max_life_span)
        self.status = True      # Variable for bacteria status (Dead/Alive)
        Bacteria.total_bac_object += 1     # Keeping count of total bacteria object


    def live_a_day(self):

        random_number = random.randint(1, 100)

        if self.life_span > 0:      # Checking the life span
            if random_number < self.chance_of_dividing:
                self.life_span -= 1     # Deducing the lifespan
                return Bacteria(self.chance_of_dividing, self.max_life_span)        # Creating new Bacteria Object
            else:
                self.life_span -= 1     # Deducing the lifespan
                return None
        else:
            self.status = False     # Killing the bacteria if lifespan is over

    def is_alive(self):
        return self.status


class Colony:


    def __init__(self, seed):
        self.seed = seed
        self.day = 0
        self.total_new = 0
        self.total_dead = 0

    def live_a_day(self, printDailyReport=True):
        new_bacteria = []       # Used for storing new bacterias
        expired_bacteria = []   # Used for storing expired bacterias

        self.day += 1
        for i in self.seed:
            if i.is_alive() is True:    # Proceeding only if bacteria is alive
                temp = i.live_a_day()   # Storing the extracted bacteria temporarily and checking if it divides
                if temp is not None:
                    new_bacteria.append(temp)
            else:                       # Proceeding if bacteria is dead
                expired_bacteria.append(i)

        self.total_new += len(new_bacteria)         # Length of new_bacteria list are the newly created offsprings
        self.total_dead += len(expired_bacteria)    # Length of expired_bacteria list are the expired bacterias

        for i in expired_bacteria:  # Removing the expired bacterias from the main bacteria object list
            self.seed.remove(i)
        for i in new_bacteria:      # Adding the new bacterias to the main bacteria object list
            self.seed.append(i)

        print("Day %5d Colony Size %6d New Members %6d Expired Members %6d" %(self.day, len(self.seed), len(new_bacteria), len(expired_bacteria)))

    def print_colony_status(self):
        print(f"Experiment Stopped")
        print(f"Colony report at DAY {self.day}")
        print(f"Current Colony population {len(self.seed)} ")
        print(f"Total number of bacteria {self.total_new}")
        print(f"Total deceased bacteria {self.total_dead}")
        print(f"Total number of Bateria objects created so far {Bacteria.total_bac_object}")


    def get_colony_size(self):
        return len(self.seed)


def main():

    prompt = ""
    while prompt != "N":

        num_of_days = int(input("Max num of days to let the colony grow: "))
        starting_bacteria = int(input("Number of starting bacteria: "))
        chance_daily_division = int(input("% chance of daily division [1-100]: "))
        max_life_span = int(input("Maximum lifespan for a bacteria (1 or greater): "))

        bacteria_list = []

        for i in range(starting_bacteria):      # Creating a bacteria list with the user's details
            bacteria_list.append(Bacteria(chance_daily_division,max_life_span))

        colony = Colony(bacteria_list)

        for i in range(num_of_days):

            if colony.get_colony_size() == 0:       # Stopping early if colony has no bacteria
                break
            if colony.get_colony_size() > 50000:    # Stopping early if colony size exceeds 50000
                break

            colony.live_a_day()


        colony.print_colony_status()
        print("")
        prompt = str.upper(input("Try another experiment? (Y/N)"))


if __name__ == "__main__":
    main()