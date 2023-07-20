def merge_sort(arr):
    length = len(arr)
    if length<=1:
        return 
    
    left_arr = arr[:length//2]
    right_arr = arr[length//2:]

    merge_sort(left_arr)
    merge_sort(right_arr)
    merge(left_arr, right_arr, arr)

    

def merge(left_arr, right_arr, arr):
    i=0 # left_arr idx
    j=0 # right_arr idx
    k=0 # merged array

    while i< len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr [j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k+=1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


if __name__ == '__main__':
    print("hi")