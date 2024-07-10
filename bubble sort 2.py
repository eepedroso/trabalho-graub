# Bubble sort in Python
import filas
import time
import timeit
def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = filas.FC2


bubbleSort(data)

#print('Sorted Array in Ascending Order:')
#print(data)
for i in range(10):
    result = timeit.timeit(stmt='bubbleSort(data)', globals=globals(), number=1)

    print(result*1000000000,)