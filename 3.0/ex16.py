# https://contest.yandex.ru/contest/45468/problems/16/
#
# 16. Очередь с защитой от ошибок Ограничение времени	1 секунда Ограничение памяти	64Mb Ввод	стандартный ввод
# или input.txt Вывод	стандартный вывод или output.txt Научитесь пользоваться стандартной структурой данных queue
# для целых чисел. Напишите программу, содержащую описание очереди и моделирующую работу очереди, реализовав все
# указанные здесь методы.
#
# Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После
# выполнения каждой команды программа должна вывести одну строчку.
#
# Возможные команды для программы:
#
# push n
# Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.
#
# pop
# Удалить из очереди первый элемент. Программа должна вывести его значение.
#
# front
# Программа должна вывести значение первого элемента, не удаляя его из очереди.
#
# size
# Программа должна вывести количество элементов в очереди.
#
# clear
# Программа должна очистить очередь и вывести ok.
#
# exit
# Программа должна вывести bye и завершить работу.
#
# Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы один элемент.
# Если во входных данных встречается операция front или pop, и при этом очередь пуста, то программа должна вместо
# числового значения вывести строку error.
#
# Формат ввода
# Вводятся команды управления очередью, по одной на строке
#
# Формат вывода
# Требуется вывести протокол работы очереди, по одному сообщению на строке
#
# Пример 1
# Ввод	Вывод
# push 1
# front
# exit
# ok
# 1
# bye
# Пример 2
# Ввод	Вывод
# size
# push 1
# size
# push 2
# size
# push 3
# size
# exit
# 0
# ok
# 1
# ok
# 2
# ok
# 3
# bye
# Пример 3
# Ввод	Вывод
# push 3
# push 14
# size
# clear
# push 1
# front
# push 2
# front
# pop
# size
# pop
# size
# exit
# ok
# ok
# 2
# ok
# ok
# 1
# ok
# 1
# 1
# 1
# 2
# 0
# bye



