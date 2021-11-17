# Implementing Bubble Sort

def bubble_sort(arr):
    
    for n in range(len(arr)-1):
        
        for i in range(len(arr)-1,n,-1):

            if arr[i] < arr[i-1]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp

       


arr = [23,1,4,3,78,5,3,0]

bubble_sort(arr)

print(arr)
