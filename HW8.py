# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

in_string = input('Введите строку: ')
s_length = len(in_string)
out_set = set()


def my_hash(word):
    hash = ''
    for el in word:
        hash += str(ord(el))
    return int(hash[::-1]) ** 2


for n in range(s_length):
    for k in range(s_length):
        if n >=k+1:
            continue
        else:
            out_set.add(in_string[n:k+1])

print(out_set)

for elem in out_set:
    print(f'{elem} - {my_hash(elem)}')
