list_ = [3, 4.5, 10, None, 4, 5, 10]
count = len(list_)
print("количество значений =", count)
summa = 0
index = 0
for i in range(count):
    if list_[i] == None:
        index = i
    else:
        summa += list_[i]
print("сумма чисел = ", summa)
print("Индекс пустого", index)

list_[index] = round(summa / count, 2)
print(list_)
