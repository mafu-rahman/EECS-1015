####
# EECS1015: Lab 5
# Name: Mahfuz Rahman
# Student ID: 217847518
# Email: mafu@my.yorku.ca
####

import random

names = ("Masha", "Kevin", "Ruigang", "Vlad", "Ramesh", \
         "Aditi", "Caroline", "Panos", "Chuck", "Grani", \
         "Rutha", "Stan", "Qiong", "Alexi", "Carlos")
cities = ("Toronto", "Ottawa", "Hamilton")

testDict = {"Richard": "Toronto", "Jia-Tao": "Toronto", "Justin": "Ottawa", "Lars": "Ottawa"}

def getRandomItem(x):
    return x[random.randint(0, len(x)-1)]       # Getting random item from the tuple passed

def createNameDictionary():
    citizens = {}
    for a in range(len(names)):
        citizens[names[a]] = getRandomItem(cities)      # Assigning cities to people randomly
    return citizens

def fromCity(dict, city):
    city_list = []
    for a in dict:      # Variable a extracts the keys of dictionary as well helps in iterating the loop
        if (dict[a] == city):   # Checking the values of dictionary with the city name
            city_list.append(a)
    return city_list

def removePeopleFrom(dict, city):
    dict_copy = dict.copy()     # Making a copy of the dictionary for using in the loop as the dict parameter gets modified
    for a in dict_copy:
        if (dict[a] == city):
            del dict[a]

def printNameDict(dict,city):
    serial=1        # This variable will be used for numbering
    for a in city:  # Extracting the city name
        print(f"People from {a}:")
        if a in dict.values():      # Checking if the city is in the dictionary
            for b in dict:          # Extracting the dictionary key
                if dict[b] == a:    # Checking if value of extracted key(b) equals to the city(a)
                    print(f"{serial}.{b}")
                    serial=serial+1
            serial=1
        else:       # If city is not in dictionary
            print("*None*")

def main():
    print("Part 1 - Testing functions with `testDict' ")
    print("Testing getRandomItem() function")
    print(cities)
    print("Item = "+ getRandomItem(cities))

    print("Testing fromCity() function")
    print(fromCity(testDict, "Toronto"))
    print(fromCity(testDict, "Ottawa"))

    print("Testing printNameDict() function")
    printNameDict(testDict, ("Toronto", "Ottawa"))

    print("Testing removePeopleFrom() function")
    removePeopleFrom(testDict, "Ottawa")
    printNameDict(testDict, ("Toronto", "Ottawa"))


    print("\nPart 2 - Main\n")

    citizens = createNameDictionary()
    printNameDict(citizens,cities)

    for a in cities:
        print(f"{a} List:")
        print(fromCity(citizens,a))

    print("Removing all people from Toronto...")
    removePeopleFrom(citizens,"Toronto")
    print("Removing all people from Hamilton...")
    removePeopleFrom(citizens,"Hamilton")
    printNameDict(citizens,cities)

    input()

if __name__ == '__main__':
    main()