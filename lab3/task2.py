def find_common_participants(str1, str2, separator):
    # получаем два списка со строками
    list1 = str1.split(separator)
    list2 = str2.split(separator)
    # задаю новый список для результата
    common = []
    # сравниваю элементы списков, совпадающие кладу в результирующий
    for i in list1:
        for j in list2:
            if i == j:
                common.append(i)
    common.sort()
    return common

string1 = "Иванов,Петров,Сидоров,Соколов,Самсонов,Аль"
string2 = "Петров,Плохих,Аль,Хороших,Сидоров"
string3 = "Петров"
string4 = "Плохих"

common_parties = find_common_participants(string1, string2, ',')
print('string1', string1)
print('string2', string2)
print('common parties', common_parties)
