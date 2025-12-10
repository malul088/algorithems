def parent(i):
    return (i-1)//2

def left(i):
    return i*2+1

def right(i):
    return i*2+2

def is_max_heap(arr, i=0, key=lambda x:x):
    for p in range((len(arr) - 2) // 2 + 1):
        l = left(p)
        r = right(p)

        if l < len(arr) and key(arr[p]) < key(arr[l]):
            return False

        if r < len(arr) and key(arr[p]) < key(arr[r]):
            return False
    return True


def max_heapify(arr, i, heap_size, key=lambda x: x):
    l = left(i)
    r = right(i)
    largest = i

    if l< heap_size and arr[l]>arr[largest]:
        largest = l
    if r< heap_size and arr[r]>arr[largest]:
        largest = r
        
    if arr[largest]>arr[i]:
        arr[i],arr[largest]=arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key=key)

def build_max_heap(arr, key=lambda x: x):
    n = len(arr)
    for end in range((n-2)//2, -1, -1):
        max_heapify(arr, end, n, key=key)


def heap_sort(arr, key=lambda x: x):
    build_max_heap(arr)  

i=3
print(parent(i))
print(left(i))
print(right(i))

arr=[50,30,20,15,10,8,2]
print(is_max_heap(arr))

arr = [3, 9, 2, 1, 4, 5]  
build_max_heap(arr)       
print(arr)
