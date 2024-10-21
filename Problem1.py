#Midterm Exam
#Problem1.py
#Name: Skye Beraz  
#Date: 10/20/2024

def listSum(myList):
  """Returns the sum (addition) total of the numbers in the list"""
  sum = 0
  for i in range(len(myList)):
    sum = sum + myList[i]
  return sum

def listMax(myList):
  """Returns the value of the largest element of a list"""
  max = myList[0]
  for i in myList:
    if i > max:
        max = i
  return max

def listMin(myList):
  """Returns the value of the smallest element of a list"""
  min = myList[0]
  for i in myList:
    if i < min:
        min = i
  return min

def listAverage(myList):
  """Returns the average value of the numbers in the list"""
  totalSum = listSum(myList)
  length = len(myList)
  ave = totalSum / length
  return ave

def listAverageDropLowest(myList):
  """Returns the average of a list but excludes the smallest value if __name__ == '__main__':
      the list in the calculation""" 
  newList = myList
  newList.remove(listMin(myList))
  ans = listSum(newList) / len(newList)
  return ans

#Test your new functions in this main
def main():
  myList = [1, 2, 3, 4]
  total = listSum(myList)
  ave = listAverage(myList)

  print("The total of the list is %d and the average is %.2f" %(total, ave))

  aveDropLow = listAverageDropLowest(myList)

  print("The average is %.2f if we drop the lowest value." %(aveDropLow))


if __name__ == '__main__':
  main()
