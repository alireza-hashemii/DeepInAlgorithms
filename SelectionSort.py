def smallest_number(array):
    smallest_index = 0
    smallest_item = array[0]
 
    for item in range(1 ,len(array)):
        if array[item] < smallest_item:
            smallest_index = item
            smallest_item = array[item]
    return smallest_index


def selection_sort(array: list):
    new_arr = []
    copied_array = array.copy()
    for i in range(len(copied_array)):
        smallest = smallest_number(copied_array)
        new_arr.append(copied_array.pop(smallest))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))



#? O(n**2)
#? procedure number 2

def smallest_number(array: list):
    smallest_index = 0
    smallest_number = array[0]
    
    for item in range(1, len(array)):
        if smallest_number > array[item]:
            smallest_number = array[item]
            smallest_index = item
    return smallest_index


def selection_sort(array: list):
    copied_array = array.copy()
    new_arr = []

    while copied_array:
        smallest_item_index = smallest_number(copied_array)
        new_arr.append(copied_array.pop(smallest_item_index))
    return new_arr



