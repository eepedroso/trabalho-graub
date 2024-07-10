# Shell sort in python
import filas
import time
import timeit

def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


data = filas.SR6
size = len(data)
shellSort(data, size)
for i in range(10):
    result = timeit.timeit(stmt='shellSort(data, size)', globals=globals(), number=1)

    print(result*1000000000,)
    
