#Exercise 2.3-5 CLRS 3 ed pag. 39
def recursive_binary_search(a, v, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if v == a[mid]:
        return mid
    elif v > a[mid]:
        return recursive_binary_search(a, v, mid + 1, high)
    else:
        return recursive_binary_search(a, v, low, mid - 1)

def main():
    a = [1,2,3,4,5,6,7,8,90]
    print ('searching 89...', recursive_binary_search(a, 90, 0, len(a)))

if __name__=="__main__":
    main()