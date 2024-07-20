# sum function
def sum_numbers(array = None):
    if array is None:
        array = []
    else:
        array = array.copy()

    temp = 0
    for i in array:
        temp += i
    return temp


# sum function using D&C
def sum_numbers_dc(array: list):
    if len(array) == 0:
        return 0
    
    elif len(array) == 1:
        return array[0]
    
    else:
        temp , *array = array
        return temp + sum_numbers_dc(array)

# QuickSort

def quick_sort(array:list):
    if len(array) < 2:
        return array
    else: 
        pivot = array[0]
        lesser = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]
        return quick_sort(lesser) + pivot + quick_sort(greater)