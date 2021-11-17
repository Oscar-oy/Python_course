# Implementing selection sort

def selection_sort(arr):

    
    for i in range (len(arr)-1,0,-1):

        max = 0

        for k in range(1,i+1):
            if arr[k] > arr[max]:
                max = k


        temp = arr[i]
        arr[i] = arr[max]
        arr[max] = temp
       


arr = [2,1,5,23,0,3,7,-1]
selection_sort(arr)
print(arr)