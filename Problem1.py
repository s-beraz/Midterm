#Midterm Exam
#Problem1.py
#Name:
#Date:

def listSum(myList):
    """Returns the sum (addition) total of the numbers in the list"""

    return 0

def listMax(myList):
    """Returns the value of the largest element of a list"""

    return 0

def listMin(myList):
    """Returns the value of the smallest element of a list"""

    return 0

def listAverage(myList):
    """Returns the average value of the numbers in the list"""

    return 0

def listAverageDropLowest(myList):
    """Returns the average of a list but excludes the smallest value if __name__ == '__main__':
        the list in the calculation"""

    return 0

#Test your new functions in this main
def main():
    testList = [1, 2, 3, 4]
    total = listSum(testList)
    ave = listAverage(testList)

    print("The total of the list is %d and the average is %.2f" %(total, ave))

    totalDropLow = listAverageDropLowest(testList)

    print("The average is %.2f if we drop the lowest value." %(totalDropLow))


if __name__ == '__main__':
    main()
