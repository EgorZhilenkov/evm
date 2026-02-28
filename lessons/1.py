def intersection(arr1, arr2):
    return set(arr1) | set(arr2)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(intersection(list1, list2))