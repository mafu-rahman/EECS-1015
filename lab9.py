#########################
# EECS1015: Lab 9
# Name: Mahfuz Rahman
# Student ID: 217847518
# Email: mafu@my.yorku.ca
#########################

from MinMaxList import MinMaxList
from random import randint

def main():
        aList = MinMaxList([10, 11, 99, 1, 34, 88])

        print("---Insert Item---")
        for i in range(30):
            x = randint(1, 100)
            aList.insertItem(x, True)

        print("---Get Min---")
        for i in range(10):
            print("Min item %d " % aList.getMin())
            aList.printList()

        print("---Get Max---")
        for i in range(10):
            print("Max item %d " % aList.getMax())
            aList.printList()

        input()

if __name__ == "__main__":
    main()