def quick_sort(line):
    if len(line) <= 1:
        return line
    
    pivot = line[0]
    less = [i for i in line[1:] if i <= pivot]
    more = [i for i in line[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(more)

print(quick_sort([1,3,3,4,5,7,6]))