def maxArray(arr, n):
    if n == 1:
        return arr[0]
        
    return max(arr[n-1], maxArray(arr, n-1))
