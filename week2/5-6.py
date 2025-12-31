
print("# 실습 4-6-1 : 정렬하기")
cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]
sorted_cities = sorted(cities, key=lambda x: x["population"], reverse=True)
sorted_name = [city["name"] for city in sorted_cities]
print(sorted_name)

print("\n# 실습 4-6-2 : 데이터 변환")
str_numbers = ["10", "20", "30", "40", "50"]
str_numbers = list(map(lambda x: int(x), str_numbers))
print(str_numbers)

print("\n# 실습 4-6-3 : 필터링")
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]
product = list(filter(lambda p : p["discount"] >= 20, products))
print(product)