# CSV 읽기(기본)
import csv

with open("users.csv") as f:
    reader = csv.reader(f)

    header = next(reader)
    print(f"컬럼 : {header}")

    for r in reader:
        print(r)