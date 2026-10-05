#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
import string

alphabet = " " + string.ascii_lowercase
input = input().split()
output = ''.join([alphabet[int(x)] if x.isnumeric() else x for x in input])
print(output)
