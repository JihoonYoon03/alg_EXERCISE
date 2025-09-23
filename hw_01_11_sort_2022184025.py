array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     268, 
]

def down_heap(arr, root, size):
    left = root * 2 + 1
    if left >= size:
        return
    child = left
    right = root * 2 + 2
    if right < size:
        if arr[left] < arr[right]:
            child = right
    if arr[root] < arr[child]:
        arr[root], arr[child] = arr[child], arr[root]
        down_heap(arr, child, size)


def sort_heap(arr):
    print(f'before: {arr}')
    n = len(arr)
    for i in range((n-1) // 2, -1, -1):
        down_heap(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        down_heap(arr, 0, i)
    print(f'after : {arr}')
    pass

def main():
    sort_heap(array[:])

if __name__ == '__main__':
    main()