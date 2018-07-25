#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/20 16:24
@annotation = ''
"""
MAX_AMOUNT = 10 ** 8
asks = [(8, 88), (9, 90), (11, 88), (12, 70), (14, 20)]
bids = [(13, 7), (9, 90), (8, 88), (3, 70), (1, 20)]
# 559.0 112 12 13 8.008928571428571 13
# 507.0 111 8 9 8 12.567567567567568
max_i = 0
while asks[max_i][0] < bids[0][0]:
    if max_i >= len(asks) - 1:
        break
    max_i += 1

max_j = 0
while asks[0][0] < bids[max_j][0]:
    if max_j >= len(bids) - 1:
        break
    max_j += 1

print(max_i, max_j)
# max_i, max_j = 4,4
best_profit = 0
for i in range(max_i + 1):
    for j in range(max_j + 1):
        def count_profit():
            if asks[i][0] >= bids[j][0]:
                # print(asks[i][0], bids[j][0])
                return 0, 0, 0, 0

            max_amount_buy = 0
            for mi in range(i + 1):
                max_amount_buy += asks[mi][1]

            max_amount_sell = 0
            for mj in range(j + 1):
                max_amount_sell += bids[mj][1]

            max_amount = min(max_amount_buy, max_amount_sell)
            # print(max_amount)

            buy_total = 0
            w_buyprice = 0
            for mi in range(i + 1):
                price = asks[mi][0]
                amount = min(max_amount, buy_total + asks[mi][1]) - buy_total
                if amount <= 0:
                    break
                buy_total += amount
                if w_buyprice == 0:
                    w_buyprice = price
                else:
                    w_buyprice = (w_buyprice * (buy_total - amount) + price * amount) / buy_total

            # print(w_buyprice, buy_total)

            sell_total = 0
            w_sellprice = 0
            for mj in range(j + 1):
                price = bids[mj][0]
                amount = min(max_amount, sell_total + bids[mj][1]) - sell_total
                if amount < 0:
                    break
                sell_total += amount
                if w_sellprice == 0 or sell_total == 0:
                    w_sellprice = price
                else:
                    w_sellprice = (w_sellprice * (sell_total - amount) + price * amount) / sell_total

            # print(w_sellprice, sell_total)

            profit = sell_total * w_sellprice - buy_total * w_buyprice
            assert sell_total == buy_total
            print(max_amount, profit, sell_total, w_buyprice, w_sellprice)
            return profit, sell_total, w_buyprice, w_sellprice


        profit, amount, buy_price, sell_price = count_profit()

        if profit >= 0 and profit > best_profit:
            best_profit = profit
            best_amount = amount
            best_i, best_j = i, j
            best_buy_price, best_sell_price = buy_price, sell_price

print(best_i, best_j)
print(best_profit, best_amount, asks[best_i][0], bids[best_j][0], best_buy_price, best_sell_price)
