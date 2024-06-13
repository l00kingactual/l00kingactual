def linear_search(arr, target):
    """
    Linear search algorithm to find the target item in a list of items.

    Parameters:
    - arr (list): The list of items to search through
    - target (any): The item to search for

    Returns:
    - int: The index of the target item in the list, or -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage
items = [1, 2, 3, 4, 5, 6]
target = 4
result = linear_search(items, target)
print(result)  # Output: 3
