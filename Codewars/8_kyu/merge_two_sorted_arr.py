"""Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays."""

def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))


print(merge_arrays([1,3,5,7,9], [10,8,6,4,2]))
