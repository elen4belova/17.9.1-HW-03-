# ввод последовательности чисел и отдельно любого числа
string = input("Введите последовательность чисел через пробел:\n")
my_num = int(input("Введите еще одно любое число:\n"))

# преобразование введённой последовательности в список-массив
my_array = list(map(int, string.split()))

# функция cортировки списка по возрастанию по алгоритму вставок
def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array

# вызов функции сортировки
sort(my_array)

# функция определения индекса элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу, по алгоритму двоичного поиска
def binary_search(array, num, left, right):
    middle = (right + left) // 2  # находим середину списка
    if array[middle] < num <= array[middle+1]:  # если число между двумя соседними элементами списка,
        return middle  # возвращаем этот индекс
    elif num <= array[middle]:  # если число не больше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, num, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, num, middle + 1, right)

# вывод результата
if my_num > my_array[-1]:
    print(f"Введенное число {my_num} больше всех чисел в последовательности {my_array}.")
elif my_num <= my_array[0]:
    print(f"Все числа последовательности {my_array} не меньше введенного числа {my_num}.")
else:
    # запускаем алгоритм поиска позиции на левой и правой границе
    print(f"Индекс элемента массива {my_array}, который < числа {my_num}, а следующий за ним >= этому числу:")
    print(binary_search(my_array, my_num, 0, len(my_array)-1))

