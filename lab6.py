######################
# EECS1015: Lab 6
# Name: Mahfuz Rahman
# Student ID: 217847518
# Email: mafu@my.yorku.ca
######################

# data for Task1
rList = [[1, 10, 9, 4, 50],
         [3, 40, 99, 37, 5, 1],
         [8, 11, 10, 94],
         [100, 9, 2, 88, 44],
         [4, 9, 2, 19]]

# data for Task 2
encodedData1 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')],
                [(9, ' '), (3, '8'), (1, 'l')], [(8, ' '), (1, 'j'), (4, '8'), (1, '.')],
                [(7, ' '), (1, '.'), (6, '8'), (1, '.')], [(6, ' '), (1, '.'), (8, '8'), (1, '.')],
                [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
                [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')],
                [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')], [(1, '.'), (21, '8')], [(22, '8')],
                [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
                [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'),
                 (1, "'")],
                [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'),
                 (1, '-'), (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '), (1, 'm'),
                 (1, 'h')]]
encodedData2 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')],
                [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')],
                [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')],
                [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')],
                [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')],
                [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'),
                 (3, ' '), (2, '|'), (17, '.')],
                [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'),
                 (7, '.'), (7, ' '), (3, '.')],
                [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'),
                 (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')],
                [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'),
                 (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')],
                [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'),
                 (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')],
                [(52, '.')]]

# data for Task 3
stringData = "1 H Hydrogen,2 He Helium,3 Li Lithium,4 Be Beryllium,5 B Boron,6 C Carbon,7 N Nitrogen,8 O Oxygen," \
             "9 F Fluorine,10 Ne Neon,11 Na Sodium,12 Mg Magnesium,13 Al Aluminum,14 Si Silicon,15 P Phosphorus," \
             "16 S Sulfur,17 Cl Chlorine,18 Ar Argon,19 K Potassium,20 Ca Calcium,21 Sc Scandium,22 Ti Titanium," \
             "23 V Vanadium,24 Cr Chromium,25 Mn Manganese "


# ---------------- Task 1 ----------------

def printRaggedList(list):
    x=0
    for item in list:
        print(f"Row {x}: {item}")
        x=x+1

def  sortRaggedList(list):
    for item in list:
        item.sort()

# ---------------- Task 2 ----------------

def decodeTupleList(list):
    str = ""
    for item_1 in list:
        for item_2 in range(0, item_1[0]):      # Setting the number of iteration according to the first digit in the list.
            str = str + item_1[1]               # Concatenating the string values accessed from the list.
    return (str)

def printEncodedAsciiImage(list):

    for item in list:       # Extracting the utmost list and passing to the decodeTupleList() function
        print(decodeTupleList(item))

# ---------------- Task 3 ----------------

def buildElementDictionary(list):
    dict = {}
    list_1 = list.split(",")
    for item in list_1:
        list_2 = item.split()       # Splitting the 3 different information i.e. "1", "H", "Hydrogen"

        list_3 = list_2.copy()
        del list_3[1]               # Removing the element symbol that is supposed to be the dictionary key
        list_3.reverse()            # Reversing the list to obtain the desired dictionary value

        dict[list_2[1]] = list_3    # Assigning the Values (Element & Element number) to the Keys (Element Symbols)
    return dict


def printElements(dict):
    for keys in dict:
        list = dict[keys]   # Extracting the dictionary values as a separate list
        print(f"{keys} [{list[0]}] #{list[1]}")


def main():
    print("\nTask 1 - Sorting and printing a ragged list\n")
    print("---List before sorting---\n")
    printRaggedList(rList)
    print("\n---List after sorting---\n")
    sortRaggedList(rList)
    printRaggedList(rList)

    print("\nTask 2 - Decoding ASCII Art")
    print("\n----- Decoded Data 1 -----\n")
    printEncodedAsciiImage(encodedData1)
    print("\n----- Decoded Data 2 -----\n")
    printEncodedAsciiImage(encodedData2)

    print("\nTask 3 - Elements String to Dictionary\n")
    x = buildElementDictionary(stringData)
    print(x)
    printElements(x)

    input()

if __name__ == '__main__':
    main()
