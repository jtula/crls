#!/bin/python3

def insertion_sort(a):
    '''
    Insertion sort (CLRS, pag. 18).
    Time complexity: O(n^2)
    Space complexity: O(1)
    '''
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


def main():
    a = [5, 2, 4, 6, 1, 3]
    print('Array: ', a)
    insertion_sort(a)
    print('Insertion sort: ', a)



if __name__=="__main__":
    main()