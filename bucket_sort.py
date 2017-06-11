import math
from insertion_sort import *

def bucket_sort(a):
    '''
    Bucket sort (CLRS, pag. 200).
    Time complexity: O(n^2)
    Space complexity: O(n)
    '''
    n = len(a)
    b = [None] * n
    r = []

    for i in range(n):
        b[i] = []
        
    for i in range(n):
        b[math.floor(n*a[i])].append(a[i])    
    
    for i in range(n - 1):
        insertion_sort(b[i])

    for k in b:    
        for m in k:
            r.append(m) 

    return r    

def main():
    a = [.78, .17, .39, .26, .72, .94, .21, .12, .23, .68]
    print('Array: ', a)
    print('Bucket-sort: ', bucket_sort(a))


if __name__=="__main__":
    main()

    
