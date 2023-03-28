tickets = int(input("Введите количество билетов: "))
count = age_low = 0
for i in range(tickets):
    age = int(input("Введите возраст участника конференции: "))
    if 17 < age < 25:
        count += 990
    elif age > 24:
        count += 1390
    else:
        age_low +=1
if tickets - age_low >= 3:
    ammount = count - (count * 0.1)
    print("Итоговая стоимость с учетом скидки: ", round(ammount, 2))
else:
    print("Итоговая стоимость: ", count)
