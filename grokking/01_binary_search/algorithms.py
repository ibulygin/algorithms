from typing import List

def binary_search(numbers: List[int], x: int) -> int:
    numbersCount = len(numbers)

    if numbersCount == 0:
        return None
    
    if numbersCount == 1:
        return 0 if numbers[0] == x else None

    if numbers[0] == x:
        return 0

    if numbers[numbersCount - 1] == x:
        return numbersCount - 1
    
    left = 0
    right = numbersCount - 1
    mid = (left + right) // 2
    
    while right - left > 1:
        if numbers[mid] == x:
            return mid
        
        if numbers[mid] > x:
            right = mid

        if numbers[mid] < x:
            left = mid

        mid = (left + right) // 2

    return None
