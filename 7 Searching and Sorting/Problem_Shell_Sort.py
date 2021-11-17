

# Implementing Shell Sort
def shell_sort(arr):

    subarray = len(arr)//2

    while subarray > 0:
        for start in range(subarray):
            gap_insertion_sort(arr,start,subarray)

        subarray = subarray//2

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):

        value = arr[i]
        position = i

        while position >= gap and arr[position-gap] > value:
            arr[position] = arr[position-gap]
            position = position-gap


        arr[position] = value



arr = [45,67,23,45,21,24,7,2,6,4,90]
shell_sort(arr)
print(arr)
    