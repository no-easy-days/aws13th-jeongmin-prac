# CSV 필터링
import csv

with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        # row는 딕셔너리! 컬럼명으로 접근 가능
        print(f"{row['이름']} ({row['나이']}세)")