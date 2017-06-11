#!/bin/python3

def partition(a, p, r):    
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quicksort(a, p, r):
    '''
    Quicksort (CLRS, pag. 170).
    Time complexity: O(n^2)
    Space complexity: O(lgn)
    '''
    if p < r:
        q =  partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)





def main():
    a = [5, 2, 4, 6, 1, 3, 4, 23, 2,1, 23]
    print('Array: ', a)
    p = 0
    r = len(a) - 1
    quicksort(a, p, r)
    print('Quicksort: ', a)



if __name__=="__main__":
    main()