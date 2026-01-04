# CSV 쓰기
import csv

students = [
{'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
{'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
{'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]

with open('students.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['학번', '이름', '학과']  # 컬럼 순서 지정
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()  # 헤더 쓰기
    writer.writerows(students)  # 데이터 쓰기