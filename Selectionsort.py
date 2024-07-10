# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
import filas
import time
import timeit


def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = filas.SR5
size = len(arr)
selectionSort(arr, size)
#print('The array after sorting in Ascending Order by selection sort is:')
#print(arr)
for i in range(10):
    result = timeit.timeit(stmt='selectionSort(arr,size)', globals=globals(), number=1)

    print(result*1000000000,)


