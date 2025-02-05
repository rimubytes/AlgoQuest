def mySqrt_binary_search(x: int) -> int:

    if x == 0:
        return 0
    
    left, right = 1, x
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
            result = mid  # Keep track of the floor value
        else:
            right = mid - 1
    
    return result