
# Implementing Merge sort

def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]

                i += 1

            else:
                arr[k] = righthalf[j]
                j += 1

            k +=1


        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
    print('Mergin  ',arr)



arr = [11,2,5,4,7,56,2,12,23]
merge_sort(arr)

print(arr)