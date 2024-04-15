# Algorithms
# Linear Search
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result1 = linear_search(numbers1, 10)
verify(result1)

# Binary Search
def binary_search(list, target):
    first = 0
    last = len(list) - 1
     
    while first <= last:
        middle = (first + last) // 2
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            first = middle + 1
        elif list[middle] > target:
            last = middle - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result2 = binary_search(numbers2, 10)
verify(result2)
    
# Recursive Binary Search
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False # <-- base stop condition
    else:
        middle = len(list) // 2
        if list[middle] == target:
            return True # <-- base stop condition
        else:
            if list[middle] < target:
                return recursive_binary_search(list[middle+1:], target)
            else:
                return recursive_binary_search(list[:middle], target)

def verify(result):
    print("Target found: ", result)

numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result3 = recursive_binary_search(numbers3, 15)
verify(result3)


