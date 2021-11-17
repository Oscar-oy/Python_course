
# Implementing Insertion Sort

def insertion_sort(arr):

    for i in range(1,len(arr)):
        position = i
        value = arr[i]
        while position >= 0 and arr[position-1] > value:
            arr[position] = arr[position-1]
            position = position-1

        arr[position] = value
            
                
        