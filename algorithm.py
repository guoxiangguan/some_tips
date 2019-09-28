import random
def q_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        l_array = [i for i in array[1:] if i <= pivot]
        r_array = [i for i in array[1:] if i > pivot]
        return q_sort(l_array) + [pivot] + q_sort(r_array)

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left_array = merge_sort(array[:mid])
        right_array = merge_sort(array[mid:])
        return merge(left_array, right_array)

def merge(array1, array2):
    i = 0
    j = 0
    res = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1
    res.extend(array1[i:])
    res.extend(array2[j:])
    return res

def max_heap(array):
    parent = len(array)
    while 0 <= parent:
        l_child = 2 * parent + 1
        r_child = 2 * parent + 2
        tmp = parent
        if l_child < len(array) and array[tmp] < array[l_child]:
            tmp = l_child
        if r_child < len(array) and array[tmp] < array[r_child]:
            tmp = r_child
        if tmp != parent:
            array[tmp], array[parent] = array[parent], array[tmp]
            parent = tmp
        else:
            parent -= 1
    return array

def heap_sort(array):
    if len(array) <= 1:
        return array
    for i in range(len(array))[::-1]:
        array[:i+1] = max_heap(array[:i+1])
        array[0], array[i] = array[i],array[0]
    return array

def insert_sort(array):
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        j = i
        while 0 < j and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array

def bubble_sort(array):
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        for j in range(1, len(array)-i):
            if array[j - 1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]

    return array


def test_sort():
    l = [random.randint(1, 100) for i in range(10)]
    print('l: ', l)
    print('qsort_l: ', q_sort(l))
    print('merge_sort: ', merge_sort(l))
    # print('max_heap: ', max_heap(l))
    print('heap_sort: ', heap_sort(l))
    print('insert_sort: ', insert_sort(l))
    print('bubble_sort: ', bubble_sort(l))

def max_length_common_sequence(X='12345', Y='134789'):
    length_X = len(X)
    length_Y = len(Y)
    if not X or not Y:
        return []
    dp = [[0 for j in range(length_Y+1)] for i in range(length_X+1)] # dp[i][j]: 前 i 和前 j 的公共子序列
    for i in range(1, length_X+1):
        for j in range(1, length_Y+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[length_X][length_Y]

print(max_length_common_sequence('abcdefgh', 'abcpol'))