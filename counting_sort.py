#!/bin/python3

def counting_sort(a, b, k):
    '''
    Counting sort (CLRS, pag. 194).
    Time complexity: O(n + k)
    Space complexity: O(k)
    '''
    c = [0] * (k + 1)
    
    for j in range(len(a)):
        c[a[j]] = c[a[j]] + 1
    
    
    for i in range(1, k + 1):
        c[i] = c[i] + c[i - 1]
    
    for j in range(len(a) - 1, -1, -1):        
        b[c[a[j]] - 1] = a[j]        
        c[a[j]] = c[a[j]] - 1    


def main():
    a = [2, 5, 3, 0, 2, 3, 0, 3]
    print('Array: ', a)
    
    b = [None] * len(a)
    k = max(a)
    counting_sort(a, b, k)
    print('Quicksort: ', b)



if __name__=="__main__":
    main()
