def calculate_result(filename):
    import json
    from pprint import pprint

    with open(filename, 'r') as f:
        data = json.load(f)

    pprint(data)
    result = 0
    for i in range(len(data)):
        result += data[i]['score']*data[i]['weight']

    result = round(result, 3)
    return result


file = 'task1.json'
print(calculate_result(file))

