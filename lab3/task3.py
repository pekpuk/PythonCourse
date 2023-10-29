def count_letters(str):
    str = str.lower()
    str1 = "".join(i for i in str if i.isalpha())
    symbols = list(str1)
    dictionary = {}
    dict(dictionary)
    for i in symbols:
        if i not in dictionary:
            dictionary[i] = 0
        dictionary[i] += 1
    return dictionary


def calculate_frequency(dictionary):
    total = sum(dictionary.values())
    for i in dictionary:
        dictionary[i] = round(dictionary[i] / total, 2)
    return dictionary


text = "Привет, приветик?"

print(count_letters(text))
print(calculate_frequency(count_letters(text)))