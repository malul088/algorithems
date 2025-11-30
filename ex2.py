def create_random_tuples(n, k, types=None):
    import random
    import string

    if types is None:
        types = [int] * k  # Default to int if no types provided

    if len(types) != k:
        raise ValueError("Length of types must be equal to k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            return random.uniform(0.0, 1000.0)
        elif t == str:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"Unsupported type: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result

def merge(a,b,key):
    if is_sorted(a, key) == False or is_sorted(b, key) == False:
        return None
    if not a:
        return b
    if not b:
        return a
    if key(a[0]) <= key(b[0]):
        return [a[0]] + merge(a[1:], b, key)
    else:
        return [b[0]] + merge(a, b[1:], key)
    
def is_sorted(a, key):
    import itertools
    for a1, b1 in itertools.pairwise(a):
        if key(a1) > key(b1):
            return False
    return True

def merge_sorted_lists( lists, key):
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0] 
    mid=len(lists)//2
    left= merge_sorted_lists( lists[:mid], key)
    right= merge_sorted_lists( lists[mid:], key)
    return merge(left,right,key)

def partition_lomuto(a, key):
    x=a[len(a)-1]
    i=-1
    for j in range(0, len(a)-1):
        if key(a[j]) <= key(x):
            i=i+1
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    temp=a[i+1]
    a[i+1]=a[len(a)-1]
    a[len(a)-1]=temp
    return i+1

def partition_hoare (a, key):
    x = a[0]       
    i = -1           
    j = len(a)      

    while True:
        while True:
            j -= 1
            if key(a[j]) <= key(x):
                break

        while True:
            i += 1
            if key(a[i]) >= key(x):
                break
        if i<j:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        else:
            return i


def dual_pivot_partition(a, key):
    if key(a[0]) > key(a[len(a)-1]):
        a[0], a[len(a)-1] = a[len(a)-1], a[0]  
    
    p1 = a[0]
    p2 = a[len(a)-1]

    lt = 1     
    gt = len(a) - 2   
    i = 1     

    while i <= gt:
        if key(a[i]) < key(p1):
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif key(a[i]) > key(p2):
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    a[0], a[lt - 1] = a[lt - 1], a[0]
    a[len(a)-1], a[gt + 1] = a[gt + 1], a[len(a)-1]

    return lt - 1, gt + 1  

               

tuples_list = create_random_tuples(10, 3, [int, float, str])
print("tuples_list")
for t in tuples_list:
    print(t)
print("--------------------------------------------")

tuples_listA = sorted(tuples_list, key=lambda t: t[0])
tuples_listB = sorted(tuples_list, key=lambda t: t[1])
tuples_listC = sorted(tuples_list, key=lambda t: t[2])

for t in tuples_listA:
    print(t)
print("--------------------------------------------")
for t in tuples_listB:
    print(t)
print("--------------------------------------------")
for t in tuples_listC:
    print(t)

print("--------------------------------------------")
print("--------------------------------------------")
print("--------------------------------------------")

tuples_listB = sorted(tuples_list, key= lambda t: t[0])


merged=merge(tuples_listA, tuples_listB, lambda t: t[0])
for t in merged:
    print(t)
print("--------------------------------------------")

#None checking
'''
tuples_listB = sorted(tuples_list, key=lambda t: t[1])


merged=merge(tuples_listA, tuples_listB, lambda t: t[0])
for t in merged:
    print(t)
print("--------------------------------------------")
'''
print("-**********************************************8-")


tuples_listA = create_random_tuples(10, 3, [int, float, str])
tuples_listB = create_random_tuples(10, 3, [int, float, str])
tuples_listC = create_random_tuples(10, 3, [int, float, str])
tuples_listA = sorted(tuples_listA, key=lambda t: t[0])
tuples_listB = sorted(tuples_listB, key=lambda t: t[0])
tuples_listC = sorted(tuples_listC, key=lambda t: t[0])

for t in tuples_listA:
    print(t)
print("--------------------------------------------")
for t in tuples_listB:
    print(t)
print("--------------------------------------------")
for t in tuples_listC:
    print(t)

lists=[tuples_listA, tuples_listA, tuples_listC]
lists= merge_sorted_lists(lists, key=lambda t: t[0]) 
for t in lists:
    print(t)
print("--------------------------------------------")

print("-**********************************************8-")
print("-**********************************************8-")
print("-**********************************************8-")
tuples_listA = create_random_tuples(10, 3, [int, float, str])
for t in tuples_listA:
    print(t)
print("--------------------------------------------")
t=partition_lomuto(tuples_listA, key=lambda t: t[0])
print ("pivot is", t)
tuples_listA = sorted(tuples_listA, key=lambda t: t[0])
for t in tuples_listA:
    print(t)
print("--------------------------------------------")


print("-**********************************************8-")
print("-**********************************************8-")
print("-**********************************************8-")
tuples_listA = create_random_tuples(10, 3, [int, float, str])
for t in tuples_listA:
    print(t)
print("--------------------------------------------")
t=partition_hoare(tuples_listA, key=lambda t: t[0])
print ("pivot is", t)
tuples_listA = sorted(tuples_listA, key=lambda t: t[0])
for t in tuples_listA:
    print(t)
print("--------------------------------------------")

print("-**********************************************8-")
print("-**********************************************8-")
print("-**********************************************8-")
tuples_listA = create_random_tuples(10, 3, [int, float, str])
for t in tuples_listA:
    print(t)
print("--------------------------------------------")

p1, p2=dual_pivot_partition(tuples_listA, key=lambda t: t[0])
print(p1,p2)
tuples_listA = sorted(tuples_listA, key=lambda t: t[0])
for t in tuples_listA:
    print(t)
print("--------------------------------------------")

