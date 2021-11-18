# Implementing Quick Sort


def quick_sort(arr):
    
    sort_help(arr,0,len(arr)-1)



def sort_help(arr,first,last):

    if first < last:

        splitpoint = partition(arr,first,last)

        sort_help(arr,first,splitpoint-1)
        sort_help(arr,splitpoint+1,last)

def partition(arr,first,last):

    pivotevalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotevalue:
            leftmark += 1

        while arr[rightmark] >= pivotevalue and leftmark <=rightmark:
            rightmark -= 1


        if rightmark < leftmark:
            done = True

        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark
            

arr = [2,5,4,6,7,3,1,4,12,11]
quick_sort(arr)
print(arr)