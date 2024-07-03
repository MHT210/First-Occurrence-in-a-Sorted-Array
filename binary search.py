
def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            if arr[mid] >= target:
                mid -= 1
                if arr[mid] < target or mid == -1:
                    mid += 1
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

    #  0  1  2  3  4  5  6  7  8  9
arr = [1, 2, 2, 3, 3, 3, 3, 3, 4, 5]
target = 2
result = find_first_occurrence(arr, target)
if result == -1:
    print(f'{target} not found in list')
else:
    print(f'found the first occurrence of {target} in list at index {result}')
