def bubble_sort(arr):
    # The outer loop iterates through the entire array.
    for i in range(len(arr)):
        # The inner loop compares adjacent elements and swaps them if they are out of order.
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function with an example array
print(bubble_sort([3,2,1,5,4]))
