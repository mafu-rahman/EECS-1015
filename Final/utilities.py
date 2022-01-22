#####################
# EECS1015 - York University
# Final Exam - utilities.py
# Name: Mahfuz Rahman
# Student ID: 217847518
# E-mail address: mafu@my.yorku.ca
#####################

from random import randint

# variable for task 1
lyrics = """It might seem crazy what I'm 'bout to say
Sunshine she's here, you can take a break
I'm a hot air balloon that could go to space
With the air, like I don't care baby by the way
Huh, because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do."""

# variable for task2
nameDict = {"Kai":19, "Bailey":19, "Su":21, "Mahesh":18, "Abdullah":18,
            "Dirk":17, "Franck":18, "Ollie":19, "Parsa":19, "Svetlana":24, "Jol":20, "Abbo":21,
            "Xavier":18, "Sarah":17, "Ming":19, "Seonjoo":20, "Pravel":22, "Urzula":22, "Javier":19,
            "Beatrice":20, "Olivia":21, "Bosko":17, "Katja":23, "Maxim":18, "Cameron":17, "Priya":18}

# variable for task3
raster = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

# variable for task 4
numList = [21, 20, 29, 16, 16, 19, 26, 19, 26, 23, 19, 25, 16, 18, 18, 18, 21, 15, 18,
           14, 22, 17, 32, 30, 22, 28, 26, 17, 19, 16, 17, 17, 19, 21, 20, 17, 18, 34, 23,
           18, 23, 22, 17, 22, 16, 11, 21, 26, 20, 27]


class listStats:
    def __init__(self, numList, corruption_level):
        self.numList_copy = numList.copy()
        self.corrupt = corruption_level

        for i in range(0, len(numList)):
            self.corruption_chance = randint(1, 100)

            if self.corruption_chance <= self.corrupt:
                self.another_random_num = randint(1, 100)

                if self.another_random_num > 50:
                    self.numList_copy[i] = -1
                else:
                    self.numList_copy[i] = 100

    def computeMean(self, numlist):
        sum = 0
        mean = 0
        for i in numlist:
            sum += i    # Adding the items in the numList
            mean = sum/(len(numlist))

        print("Standard Mean:   %.2f" % mean)

    def computeTrimmedMean(self, numlist):
        numlist.sort()
        trimmed_list = numlist[10: (len(numlist) - 10)]     # Removing the first 10 items and last 10 items from the list
        sum = 0
        mean = 0

        for i in trimmed_list:
            sum += i
            mean = sum/(len(trimmed_list))

        print("Trimmed Mean:    %.2f"%mean)

    def computeMedian(self, numlist):
        numlist.sort()
        mid = (len(numlist)) // 2
        print("Median: %11d" % numlist[mid])

    def printStatistics(self):
        print(f"\nCorruption Level {self.corrupt}%")
        print(self.numList_copy)

        self.computeMean(self.numList_copy)
        self.computeTrimmedMean(self.numList_copy)
        self.computeMedian(self.numList_copy)