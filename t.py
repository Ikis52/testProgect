c = 1000
while c != 6:
 print(c)
 c = c - 7
print('виктор корнеплод')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
oper = input('Введите операцию (+, -, *, /): ')

if oper == '+':
    print(a + b)
elif oper == '-':
    print(a - b)
elif oper == '*':
    print(a * b)
elif oper == '/' and b != 0:
    print(a / b)
else:
    print('Error')
