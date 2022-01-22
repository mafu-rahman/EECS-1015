#########################
# EECS1015: Lab 9
# Name: Mahfuz Rahman
# Student ID: 217847518
# Email: mafu@my.yorku.ca
#########################

class MinMaxList:

    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult=False/True):

        if len(self.listData) == 0:     # Inserting item if list is empty
            self.listData.append(item)
            print(f"Item ({item}) inserted at location 0")
            MinMaxList.printList(self)


        elif item >= self.listData[-1]:     # Inserting item at the last index if item is largest in the list
            self.listData.append(item)
            print(f"Item ({item}) inserted at location {len(self.listData)-1}")
            MinMaxList.printList(self)

        else:
            for i in range(len(self.listData)+1):    # Extracting each item in the list and comparing it

                if item <= self.listData[i]:
                    self.listData.insert(i, item)

                    if printResult == True:
                        print(f"Item ({item}) inserted at location {i}")
                        MinMaxList.printList(self)

                    break

    def getMin(self):
        result = self.listData[0]
        del self.listData[0]
        return result

    def getMax(self):
        result = self.listData[-1]
        del self.listData[-1]
        return result

    def printList(self):
        print(self.listData)