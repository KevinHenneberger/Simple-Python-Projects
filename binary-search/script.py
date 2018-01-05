def binary_search(arr, t):
    
    l = 0
    r = len(arr) - 1

    while (l <= r):

        m = (r + l) // 2

        if (arr[m] == t):
            return m
        elif (arr[m] < t):
            l = m + 1
        elif (arr[m] > t):
            r = m - 1

    return -1

def main():

    arr = [5, 9, 7, 1, 3, 2, 9, 8, 2, 9]
    arr.sort()    

    print(arr)

    t = int(input("Element: "))

    print(binary_search(arr, t))    

main()
