# Big O - bubble sort
# (n-2)*(n-1) = O(n^2)

# 0(n * log(n)): Merge Sort, Quick Sort, Timp Sort

def bubble_sort(arr):
    print(arr)
    arr_ = arr
    if not len(arr) > 1:
        return arr_
    
    temp = float()


    for _ in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr_[i] > arr_[i + 1]:
                temp = arr_[i]
                arr_[i] = arr_[i + 1]
                arr_[i + 1] = temp
    
    return arr_

lst = [1, 6, 8, 10, 4, 12, 17, 2, 4]

print(bubble_sort(lst))
