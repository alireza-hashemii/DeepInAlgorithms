def binary_search(array, item):
    low = 0
    high = len(array) - 1
   
    
    while low <= high:
        mid = (high + low) // 2
        guess = array[mid]
        if guess == item:
            return f"It is found in {mid}th position."
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
    return None

print(binary_search([i for i in range(100)],67))
# O(logn)