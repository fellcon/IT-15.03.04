def heapsort(list):
    build_max_heap(list)
    for index in range(len(list) - 1, 0, -1):
        list[0], list[index] = list[index], list[0]
        max_heapify(list, index=0, size=index)
def parent(index):
    return (index - 1) // 2
def left(index):
    return 2 * index + 1
def right(index):
    return 2 * index + 2

def build_max_heap(list):
    length = len(list)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(list, index=start, size=length)
        start = start - 1

def max_heapify(list, index, size):
    l = left(index)
    r = right(index)
    if (l < size and list[l] > list[index]):
        largest = l
    else:
        largest = index
    if (r < size and list[r] > list[largest]):
        largest = r
    if (largest != index):
        list[largest], list[index] = list[index], list[largest]
        max_heapify(list, largest, size)


list = input('Введите числа: ').split()
list = [int(x) for x in list]
heapsort(list)
print('Отсортированные числа: ', end='')
print(list)