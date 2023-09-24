"""
    При поступлении в университет абитуриенты указывают список приоритетов образовательных программ,
на которые они хотели бы попасть. Все абитуриенты университета были ранжированы и выстроены по рейтингу
(рейтинг некоторых абитуриентов может совпадать). На каждой образовательной программе есть контрольные
цифры приёма — сколько абитуриентов может быть зачислено на это программу.

    Вам необходимо справедливо распределить абитуриентов по программам.
Для каждого абитуриента должно выполняться следующее: все места на более желаемых им программах,
чем та, на которую он поступил (или на всех программах из списка абитуриента, если он не поступил никуда),
заняты людьми с рейтингом выше чем у этого абитуриента.

"""

n, k = map(int, input().split())

possible_seats = {}
res = [-1] * n
inp = list(map(int, input().split()))
for i in inp:
    possible_seats[k] = i
    k += 1

abiturs = []
k = 1
for i in range(n):
    inp = list(map(int, input().split()))
    inp.insert(0, k)
    abiturs.append(inp)
    k += 1

sorted_abiturs = sorted(abiturs, key=lambda x: (x[1], x[0]))

for abitur in sorted_abiturs:
    for possible_seat in abitur[3:]:
        if possible_seats[possible_seat] > 0:
            possible_seats[possible_seat] -= 1
            res[abitur[0] - 1] = possible_seat
            break

print(res)
