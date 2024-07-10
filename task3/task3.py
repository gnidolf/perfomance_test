import json
import os
import sys


def update_values(tests, values_dict):
    for test in tests:
        if 'value' in test:
            test['value'] = values_dict.get(test['id'], '')
        if 'values' in test:
            update_values(test['values'], values_dict)


def create_report(values_path, tests_path, report_path):
    with open(values_path, 'r') as v_file:
        values_data = json.load(v_file)
    with open(tests_path, 'r') as t_file:
        tests_data = json.load(t_file)
    
    values = {item['id']: item['value'] for item in values_data['values']}

    update_values(tests_data['tests'], values)

    with open(report_path, 'w') as r_file:
        json.dump(tests_data, r_file, indent=2)


if len(sys.argv) < 4:
    print('Недостаточно аргументов')
    sys.exit()
elif not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
    print('Файл не сущесвует')
    sys.exit()
else:
    values_path, tests_path, report_path = sys.argv[1], sys.argv[2], sys.argv[3]

create_report(values_path, tests_path, report_path)
