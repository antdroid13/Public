per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму для расчета годового дохода:"))
deposit = [rate * (money / 100) for rate in per_cent.values()]
print(deposit)
print("Максимальная прибыль", max(deposit))