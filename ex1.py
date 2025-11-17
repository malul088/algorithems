#min and max
filename = "data.txt"
mini = float('inf')
maxi = float('-inf')
with open(filename, "r") as f:
    for line in f:
        num = int(line.strip())  

        
        if num < mini:
                mini = num
        if num > maxi:
                maxi = num

print(f"min={mini}")
print(f"max={maxi}")


#insertion sort

filename = "data.txt"
arr = []

with open(filename, "r") as f:
    for line in f:
        arr.append(int(line.strip()))

for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key
for num in arr:
    print(num)

print()
#merge sort
    
filename = "data.txt"
arr = []

with open(filename, "r") as f:
    for line in f:
        arr.append(int(line.strip()))

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr=merge_sort(arr)
for num in arr:
    print(num)

