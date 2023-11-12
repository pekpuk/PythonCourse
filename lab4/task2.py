def csv_to_json(filename):
    import csv
    import json

    with open(filename, 'r') as f:
        lines = [line for line in csv.DictReader(f)]
        for line in lines[:]:
            print(json.dumps(line, ensure_ascii=False, indent=4))

    return 0


file = 'task2.csv'
csv_to_json(file)
