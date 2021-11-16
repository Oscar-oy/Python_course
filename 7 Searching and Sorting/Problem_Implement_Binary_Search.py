# Recursive Way

def binary_search(arr,num):
    if len(arr) > 0:
        mid = len(arr)//2

        if num < arr[mid]:
            return binary_search(arr[:mid], num)

        elif num > arr[mid]:
            return binary_search(arr[mid+1:], num)

        elif num == arr[mid]:
            return True
    else:
        return False

arr = [1,2,3,4,5]
print(binary_search(arr,6))


# Not recursive

def iter_binary_search(arr,num):

    while len(arr) > 0:

        mid = len(arr)//2

        if num == arr[mid]:
            return True

        else:
            if num > arr[mid]:
                arr = arr[mid+1:]

            elif num < arr[mid]:
                arr = arr[:mid]

    return False


print(iter_binary_search(arr,34))