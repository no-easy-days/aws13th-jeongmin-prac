# CSV -> JSON 변환
import csv
import json

with open('users.csv', 'r', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))


with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(reader, f, ensure_ascii=False, indent=4)
