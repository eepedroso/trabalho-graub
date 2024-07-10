import time
import random
from random import seed
from random import randint 


def filacrescente(q):
    n = int(q)
    aux = []
    for num in range(n):
        aux.append(num)
    return aux

def filadecresc(q):
    n = int(q)
    aux = []
    for num in range(n):
        a = n - num -1
        aux.append(a)
    return aux




# seed random number generator
seed(1)
# generate some integers

def aleatorios(n):
    aux = []
    q = int(n)
    for _ in range(n):

        value = randint(0, q)
        aux.append(value)
    return aux
    
def aleatoriossr(n):
    q = int(n)
    # resultant random numbers list
    randomList=[]
    # traversing the loop 15 times
    for i in range(q):
    # generating a random number in the range 1 to 100
        r=random.randint(1,100000)
        # checking whether the generated random number is not in the
        # randomList
        if r not in randomList:
        # appending the random number to the resultant list, if the condition is true
            randomList.append(r)
    return randomList


'''FC1 = filacrescente(256)
FC2 = filacrescente(1024)
FC3 = filacrescente(4096)
FC4 = filacrescente(16384)
FC5 = filacrescente(32768)
FC6 = filacrescente(65536)'''

'''FD1 = filadecresc(256)
FD2 = filadecresc(1024)
FD3 = filadecresc(4096)
FD4 = filadecresc(16384)
FD5 = filadecresc(32768)
FD6 = filadecresc(65536)'''

'''RD1 = aleatorios(256)
RD2 = aleatorios(1024)
RD3 = aleatorios(4096)
RD4 = aleatorios(16384)
RD5 = aleatorios(32768)
RD6 = aleatorios(65536)'''

SR1 = aleatoriossr(256)
SR2 = aleatoriossr(1024)
SR3 = aleatoriossr(4096)
SR4 = aleatoriossr(16384)
SR5 = aleatoriossr(32768)
SR6 = aleatoriossr(65536)


#print(RD6)































