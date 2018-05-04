
#Daniel Bandler
#5/4/18
#mySort.py - using insertion sort

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def mySort(A):
    i=1
    while i < len(A):
        x = A[i]
        j = i - 1
        while j>= 0 and j[1] > x:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = x
        i = i+1
    return A
    
if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
