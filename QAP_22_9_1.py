# //////////////////////
error = 'ПЕРЕЗАПУСК ПРОГРАММЫ'

# Функция для определения цифр в строке

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

#########################################################################
# Проверка соответствия указанному в условии ввода данных.

while True:
    sequence_numbers = input('Введите целые числа через пробел: ')
    if " " not in sequence_numbers:
        print("\nВ вводе отсутствуют пробелы (введите числа, согласно условиям ввода.)")
        continue
    elif not is_int(sequence_numbers):
        print('\nВ вводе содержаться не целые числа (введите числа, согласно условиям ввода.)\n')
        print(error)
        continue
    else:
        sequence_numbers = sequence_numbers.split()
        break

while True:
    # user_number = int(input('Введите любое число: '))
    user_number = input('Введите любое число: ')
    if " " in user_number:
        print('\nВ вводе любого числа содержаться пробелы (введите целое число.)\n')
        print(error)
        continue
    elif not is_int(user_number):
        print('\nВ вводе любого числа содержиться не целое число (введите целое число.)\n')
        print(error)
        continue
    else:
        user_number = int(user_number)
        break


# Конвертируем строки в числа

list_sequence_numbers = [int(item) for item in sequence_numbers]

# Сортировка список по возростанию

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


# list_sequence_numbers.sort() # Сортировка по возростанию с помощью встроенной функции
# print(list_sequence_numbers)


list_sequence_numbers = merge_sort(list_sequence_numbers)

# Поиск позиции элемента


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


# Находим индекс позиции элемента, который меньше  введенного пользователем числа, а следующий за ним больше или равен этому числу.

print(f'Упорядоченный список: {list_sequence_numbers}')
max = len(list_sequence_numbers) - 1
if user_number > list_sequence_numbers[max]:
    print(f'''Введенный элемент находится за списком
В списке нет большего элемента
Ближайший меньший элемент: {list_sequence_numbers[max]}, его индекс: {max}''')
elif user_number < list_sequence_numbers[0]:
    print(f'''В списке нет введенного элемента
В списке нет меньшего элемента
Ближайший больший элемент: {list_sequence_numbers[0]}, его индекс: {0}''')
else:
    
    index = binary_search(list_sequence_numbers, user_number, 0, len(list_sequence_numbers))

    if not binary_search(list_sequence_numbers, user_number, 0, len(list_sequence_numbers)):
        rI = min(list_sequence_numbers, key=lambda x: (abs(x - user_number), x))
        ind = list_sequence_numbers.index(rI)
        max_ind = ind + 1
        min_ind = ind - 1
        if rI < user_number:
            print(f'''В списке нет введенного элемента
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_sequence_numbers[max_ind]} его индекс: {max_ind}''')
        else:
            print(f'''Индекс введенного элемента: {binary_search(list_sequence_numbers, user_number, 0, len(list_sequence_numbers))}
В списке нет меньшего элемента
Ближайший больший элемент: {list_sequence_numbers[max_ind]} его индекс: {max_ind}''')
    else:
        if index == max:
            print(f'''Индекс введенного элемента last: {index}
Ближайший меньший элемент: {list_sequence_numbers[max - 1]}, его индекс: {max - 1}
В списке нет большего элемента''')
        else:
            print(f'''Индекс введенного элемента last: {index}
Ближайший меньший элемент: {list_sequence_numbers[index-1]}, его индекс: {index - 1}
Ближайший больший элемент: {list_sequence_numbers[max - 1]}, его индекс: {max - 1}''')
