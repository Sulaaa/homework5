# глобальные переменные
userChoice = 0      # переменная, которая хранит выбор пользователя
# Задание 1: вобъявить переменную, котоая будет хранить 15 значений
valuesArray = ['1.Silver', '2.Gold', '3.Aurum', '4.Nova', '5.Guardian', '6.Master', '7.Global', '8.Heart', '9.Car', '10.Question', '11.Exersizes', '12.Pig', '13.Cow', '14.Games', '15.Messenger']

print('Меню:')
print('1. Вывести на экран все знаения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('6. Выйти')
print('Введите опцию:')
userChoice = int(input())

# Задание 2: в цикле while создать ограничения для ввода опций таким образом, чтобы
# программа принимала только знаенчия, из меню (1-6), в остальных случаях выдвала ошибку.

# Задание 3: Реализовать опцию 1 и 2 из списка меню.
while userChoice != 6:
    # Вывод ошибки, если userChoice больше или меньше 1 или 6
    if userChoice < 1 or userChoice > 6:
        print('Ошибка!')

    print('Введите опцию:', userChoice)

    print('Меню:')
    print('1. Вывести на экран все знаения')
    print('2. Добавить значение')
    print('3. Удалить значение')
    print('4. Найти значение')
    print('5. Отсортировать значения')
    print('6. Выйти')
    print('Введите опцию:')
    userChoice = int(input())

    # Реализуем функцию 1
    if userChoice == 1:
        for i in valuesArray:
            print(i)

    # Реализуем функцию 2
    if userChoice == 2:
        newValue = input('Введите новое значение: ')
        valuesArray.append(newValue)

    # Реализуем функцию 3
    if userChoice == 3:
        delValue = input('Введите значение на удаление: ')
        valuesArray.remove(delValue)

    # Реализуем функцию 4
    if userChoice == 4:
        foundValue = input('Введите значение, которое надо найти: ')
        for i in range(len(valuesArray)) :
            if valuesArray[i] == foundValue:
                print('Значение {} найдено!'.format(foundValue))
                break
            if i == len(valuesArray) - 1:
                print('Значение {} не найдено'.format(foundValue))

    # Реализуем функцию 5, но не указываем ключа, т.к его нет. Сортировка будет проводится так, как предписано в python
    if userChoice == 5:
        valuesArray.sort()