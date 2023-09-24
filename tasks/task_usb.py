"""
    Вася подсчитал, что у него есть m гаджетов, которые нужно подключить к USB и всего n USB-портов на компьютере.
В ближайшем интернет-магазине продаются разветвители с одного USB на два за c2 рублей и USB-хабы с одного USB на 5 по
c5 рублей.
ЫЫ
    Разветвители и хабы можно подключать друг к другу и к USB-портам компьютера. Определите, какое минимальное
количество рублей нужно потратить Васе, чтобы подключить все USB устройства. При этом можно обеспечить возможность
подключить и больше m гаджетов, главное минимизировать цену.
"""


def should_i_buy_hub_or_splits(mod, c_hub, c_split):
    if mod <= 0:
        return 0
    else:
        if c_hub < (mod - 1) * c_split:
            return c_hub
        else:
            return (mod - 1) * c_split


n = int(input())
m = int(input())
c2 = int(input())
c5 = int(input())

res = 0
need = m - n

if need <= 0:
    pass
else:
    need += 1

if c5 / 4 < c2:
    d = need // 4
    res += c5 * d
    need -= 4 * d
    res += should_i_buy_hub_or_splits(need, c5, c2)
else:
    res = (need - 1) * c2

print(res)
