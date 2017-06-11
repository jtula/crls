#!/bin/python3
import math

def merge(a, p, q, r):
    '''
    Merge sort (CLRS, pag. 31).
    Time complexity: O(nlgn)
    Space complexity: O(n)
    '''
    n = r + 1
    b = [None] * n    
    i = p

    for i in range(n):
        b[i] = a[i]        

    for j in range(q + 1, n):
        b[r + q + 1 - j] = a[j]
    
    i = p
    j = r
    
    for k in range(p, n):
        if b[i] <= b[j]:
            a[k] = b[i]
            i = i + 1
        else:
            a[k] = b[j]
            j = j - 1

    
def merge_sort(a, p, r):
    if p < r:
        q = math.floor( (p + r) / 2 )
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


def main():
    a = [5, 2, 4, 6, 1, 3]
    print('Array: ', a)
    p = 0
    r = len(a) - 1
    merge_sort(a, p, r)
    print('Merge sort: ', a)



if __name__=="__main__":
    main()