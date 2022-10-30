def index_of(container, find_element):
      for i in range(len(container)):
            if container[i] == find_element:
                  return i
a = int(input('Введите: '))
print(index_of([1, 2, 3, 4, 5, 6, 7, 8], a))

def factorial(container, n):
      if n == 1:
            print(container)
            return
      for i in range(n):
            factorial(container, n - 1)
            if n % 2 == 0:
                  container[i], container[n-1] = container[n-1], container[i]
            else:
                  container[0], container[n - 1] = container[n - 1], container[0]
if __name__ == '__main__':
      a = int(input('Введите: '))
      container = [1, 2, 3, 4, 5, 6, 7, 8]
print(factorial(container, len(container)))

def bin_search(data, value):
      n = len(data)
      left = 0
      right = n - 1
      while left <= right:
            middle = (left + right) // 2
            if value < data[middle]:
                  right = middle - 1
            elif value > data[middle]:
                  left = middle + 1
            else:
                  return middle
if __name__ == '__main__':
      data = [1, 2, 3, 4, 5, 6, 7, 8]
      print(bin_search(data, 3))





