#########################
# EECS1015: Lab 7
# Name: Mahfuz Rahman
# Student ID: 217847518
# Email: mafu@my.yorku.ca
#########################

import pytest
from typing import List

def initializeMinMaxList(myList: List[int]) -> None:
    myList.sort()


def insertItem(myList: List[int], item: int) -> None:
    myList.append(item)
    myList.sort()


def getMinMax(myList: List[int], minormax: str) -> int:
    list_length = len(myList)
    assert list_length != 0, "List must not be empty"
    assert minormax.upper() == "MAX" or minormax.upper() == "MIN", "2nd argument must be 'Min' or 'Max' "
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result


def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE. Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()


def test_getMinMaxCase1():
    a = [10, 20]
    initializeMinMaxList(a)

    min = getMinMax(a, "min")
    assert min == 10, "Min should be 10"

    max = getMinMax(a, "max")
    assert max == 20, "Max should be 20"


def test_getMinMaxCase2():
    a = [99]
    initializeMinMaxList(a)

    min = getMinMax(a, "min")
    assert min == 99, "Min should be 99"

    insertItem(a, 99)

    max = getMinMax(a, "max")
    assert max == 99, "Max should be 99"


def test_getMinMaxCase3():
    a = []
    initializeMinMaxList(a)

    insertItem(a, 10)
    insertItem(a, 20)

    min = getMinMax(a, "min")
    assert min == 10, "Min should be 10"

    max = getMinMax(a, "max")
    assert max == 20, "Max should be 20"


def test_getMinMaxRequestError():
    a = [10, 30, 20]
    initializeMinMaxList(a)

    with pytest.raises(AssertionError) as err:
        error = getMinMax(a, "MID")
    assert err.typename == "AssertionError", "Should raise AssertionError!"


def test_getMinMaxEmptyError():
    a = []
    initializeMinMaxList(a)

    with pytest.raises(AssertionError) as err:
        error = getMinMax(a, "MIN")
    assert err.typename == "AssertionError", "Should raise AssertionError!"