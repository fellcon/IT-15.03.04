import random
count1 = 0
count0 = 0
scount = 1

lst = [random.randint(0, 1) for i in range(16)]
print(lst)
for i in lst:
    if i == 1:
        count1 += 1
    else:
        count0 += 1

n = len(lst)
sv = []
sl = []
c = 1
sv.append(lst[0])
for i in range(1, n):
    if lst[i] == lst[i-1]:
        c += 1
    else:
        sl.append(c)
        c = 1
        sv.append(lst[i])
sl.append(c)
for i in range(len(sv)):
    print(sv[i], " - ", sl[i], sep="")



print(count1,count0)

def percentage(x, y):
    if not x and not y:
        print("x = 0%\ny = 0%")
    else:
        fin = 100/ (x + y)
        x *= fin
        y *= fin
        print('Нули = {}%\nЕдиницы = {}%'.format(x,y))
percentage(count0,count1)
