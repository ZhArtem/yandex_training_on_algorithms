"""
https://contest.yandex.ru/contest/45468/problems/24/


24. Покупка билетов Ограничение времени	1 секунда Ограничение памяти	64Mb Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt За билетами на премьеру нового мюзикла выстроилась очередь из N человек,
каждый из которых хочет купить 1 билет. На всю очередь работала только одна касса, поэтому продажа билетов шла очень
медленно, приводя «постояльцев» очереди в отчаяние. Самые сообразительные быстро заметили, что, как правило,
несколько билетов в одни руки кассир продаёт быстрее, чем когда эти же билеты продаются по одному. Поэтому они
предложили нескольким подряд стоящим людям отдавать деньги первому из них, чтобы он купил билеты на всех.

Однако для борьбы со спекулянтами кассир продавала не более 3-х билетов в одни руки, поэтому договориться таким
образом между собой могли лишь 2 или 3 подряд стоящих человека.

Известно, что на продажу i-му человеку из очереди одного билета кассир тратит Ai секунд, на продажу двух билетов — Bi
секунд, трех билетов — Ci секунд. Напишите программу, которая подсчитает минимальное время, за которое могли быть
обслужены все покупатели.

Обратите внимание, что билеты на группу объединившихся людей всегда покупает первый из них. Также никто в целях
ускорения не покупает лишних билетов (то есть билетов, которые никому не нужны).

Формат ввода На вход программы поступает сначала число N — количество покупателей в очереди (1 ≤ N ≤ 5000). Далее
идет N троек натуральных чисел Ai, Bi, Ci. Каждое из этих чисел не превышает 3600. Люди в очереди нумеруются,
начиная от кассы.

Формат вывода
Требуется вывести одно число — минимальное время в секундах, за которое могли быть обслужены все покупатели.

Пример
Ввод	Вывод
5
5 10 15
2 10 15
5 5 5
20 20 1
20 1 1
12
"""


# def get_min_time(t, n):
#     dp = [-1] * (n + 1)
#     dp[1] = t[0][0]
#     if n == 1:
#         return dp[1]
#     dp[2] = min(t[0][0] + t[1][0],
#                 t[0][1])
#     if n == 2:
#         return dp[2]
#     dp[3] = min(t[0][0] + t[1][0] + t[2][0],
#                 t[0][1] + t[2][0],
#                 t[0][0] + t[1][1],
#                 t[0][2])
#     if n == 3:
#         return dp[3]
#     for i in range(4, n + 1):
#         dp[i] = min(dp[i - 1] + t[i - 1][0],
#                     dp[i - 2] + t[i - 2][1],
#                     dp[i - 3] + t[i - 3][2])
#     return dp[n]
#
#
# n = int(input())
# t = [tuple(map(int, input().split())) for _ in range(n)]
#
# print(get_min_time(t, n))


def get_min_time(t, n):
    dp = [0] * (n + 1 + 3)
    for i in range(1, n + 3):
        dp[i] = min(dp[i - 1] + t[i][0],
                    dp[i - 2] + t[i - 1][1],
                    dp[i - 3] + t[i - 2][2])
    return dp[n]


n = int(input())
t = [tuple(float('inf') for _ in range(3))]
for _ in range(n):
    t.append(tuple(map(int, input().split())))
for _ in range(2):
    t.append(tuple(float('inf') for _ in range(3)))

print(get_min_time(t, n))