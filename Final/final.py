#####################
# EECS1015 - York University
# Final Exam - final.py
# Name: Mahfuz Rahman
# Student ID: 217847518
# E-mail address: mafu@my.yorku.ca
#####################

def task0():
    print("\n--- Task 0 ---\n")
    print("""EECS1015 - York University
Final Exam - final.py
Name: Mahfuz Rahman
Student ID: 217847518
Email: mafu@my.yorku.ca""")


from math import sqrt
import utilities


def task1(lyrics):
    print("\n--- Task 1 ---\n")

    lyrics = lyrics.lower().replace("\n", " ").replace(",", "").replace(".", "")  # Replacing lines and removing periods and commas
    words = lyrics.split(" ")
    unique_words = list(set(words)) # Converting to set and then to list again
    unique_words.sort()     # Sorting the list items as set() shuffles the words everytime the program is run
    for i in unique_words:
        count = words.count(i)
        print(" %10s [%i] %s" % (i, count, "*" * count))


def task2(dict):
    print("\n--- Task 2 ---\n")

    invert_dict = {}
    age_values = list(set(dict.values()))   # Obtaining the dictionary values, arranging them using set() and converting back to a list
    name_list = []      # Will use to store people's name with same age

    for i in age_values:
        for j in dict:
            if dict[j] == i:    # Checking if age is same
                name_list.append(j)     # Adding people's name with same age

        invert_dict.update({i: name_list})  # Adding the list of people with the same age key value
        name_list = []  # Resetting the list

    print("---New Dictionary---\n")
    print(invert_dict)

    for i in invert_dict:
        print(f"Age {i}")
        for j in invert_dict[i]:    # Iterating through the people's name list for same age
            print(f"  {j}")


def task3(raster_list):
    print("\n--- Task 3 ---\n")

    choice = "Y"
    while choice.upper() != "N":

        radius = int(input("Enter your circle's radius [1 to 9]: "))
        assert radius > 0 and radius < 10, "Radius should be between 1 to 9 !"

        for i in range(0, 20):
            for j in range(0, 20):
                x = i - 10
                y = j - 10
                if (sqrt((x ** 2) + (y ** 2))) <= radius:
                    raster_list[i][j] = "*"
                else:
                    raster_list[i][j] = " "

        circle = ""
        for i in range(0, 20):
            for j in range(0, 20):
                circle += raster_list[i][j]   # Creating a string of the circle
            circle += "\n"  # Adding a line break at the end of list row
        print(circle)
        choice = input("Try again: Y/N? ")


def task4(numlist):
    print("\n--- Task 4 ---\n")

    obj1 = utilities.listStats(numlist, 0)  # no corruption
    obj2 = utilities.listStats(numlist, 15)  # 15% chance of corruption
    obj3 = utilities.listStats(numlist, 30)  # 30% chance of corruption
    obj1.printStatistics()
    obj2.printStatistics()
    obj3.printStatistics()


def main():
    task0()
    task1(utilities.lyrics)
    task2(utilities.nameDict)
    task3(utilities.raster)
    task4(utilities.numList)

    input('\nPress enter to quit.')  # pause at the end of the program

if __name__ == "__main__":
    main()