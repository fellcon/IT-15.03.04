import math

while True:
    s = input('Знаки операций: +,-,*,/,**,math.log(x, Base), math.ceil: ')
    if s in ('+', '-', '*', '/', '**', 'math.log(x, Base)', 'math.ceil'):
        if s == 'math.ceil':
            z = float(input('z ='))
        elif s == 'math.ceil':
            print('%.3f' % (math.ceil(z)))
        else:
            print('Введите первый элемент:')
            x = float(input('x ='))
            print('Введите второй элемент:')
            y = float(input('y ='))
            if s == '+':
                print('%.3f' % (x + y))
            elif s == '-':
                print('%.3f' % (x - y))
            elif s == '*':
                print('%.3f' % (x * y))
            elif s == '/':
                if y != 0:
                    print('%.3f' % (x / y))
                else:
                    print('Нельзя делить на 0.')
            elif s == '**':
                print('%.3f' % (x ** y))
            elif s == 'math.log(x, Base)':
                print('%.3f' % (math.log(x, y)))
    else:
        print('Неверный знак.')


