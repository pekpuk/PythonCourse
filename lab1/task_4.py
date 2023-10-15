visitors = ["User1", "User2", "User1", "User2", "User3", "User4", "User1"]

dict_visitors = {
    "Общие посещения": 0,
    "Уникальные посещения": 0
}
uniqie_visitors = list(set(visitors))


dict_visitors["Общие посещения"] = len(visitors)
dict_visitors["Уникальные посещения"] = len(uniqie_visitors)
print(dict_visitors)