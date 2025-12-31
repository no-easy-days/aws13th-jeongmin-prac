

print("# 실습1: 변수 선언 (기초)")
name = "정민"
age = 27
num = 7
print(f"{name}님의 나이는 {age}세 입니다.\n좋아하는 숫자는 {num} 입니다")

print("\n# 실습 2: 값 교환 (기초)")
first = "A"
second = "B"
first, second = second, first
print(f"A=>{first}, B=>{second}")

print("\n# 실습 3: 복합 연산 (기초)")
balance = 10000
balance -= 3000
balance *= 2
print(balance)

print("\n# 실습 4: 오류 수정 (응용)")
# 변수명에 숫자시작 X 예약어 X 띄어쓰기 X
second_place = "은메달 "
user_name = "홍길동 "
grade = "1학년"
print(second_place + user_name + grade)

print("\n# 실습 5: 자료형 확인하기(기초)")
it_is_int = 42
it_is_float = 3.14
it_is_bool = True
it_is_str = "Hello"
it_is_tuple = (1, 2, 3)
it_is_list = [1, 2, 3]
it_is_dictionary = {"a": 1, "b": 2, "c": 3}
it_is_set = {"a", "b", "c"}
print(f"it_is_int = {type(it_is_int)}")
print(f"it_is_float = {type(it_is_float)}")
print(f"it_is_bool = {type(it_is_bool)}")
print(f"it_is_str = {type(it_is_str)}")
print(f"it_is_tuple = {type(it_is_tuple)}")
print(f"it_is_list = {type(it_is_list)}")
print(f"it_is_dictionary = {type(it_is_dictionary)}")
print(f"it_is_set = {type(it_is_set)}")

print("\n# 실습 6: 형변환 연습(기초)")
def isint2():
    for num in range(2):
        while True:
            value = input(f"{num+1}번째 정수 입력 : ")
            try:
                num1 = int(value)
                print(f"입력된 정수 = {num1}")
                break
            except ValueError:
                print(f"정수만 입력하세요")
isint2()

print("\n# 실습 7: 자기소개 프로그램 (응용)")
user_name = input("이름 : ")
user_age = input("나이 : ")
user_height = input("키 : ")
print(f"안녕하세요 저는 {user_name}입니다. \n제 나이는 {user_age}세 이고, 키는 {user_height}입니다. "
      f"\n 내년에는 {int(user_age)+1}세 이겠네요")

print("\n# 실습 8: 계산기 만들기 (심화)")
num1 = int(input("숫자 1 입력 : "))
num2 = int(input("숫자 2 입력 : "))
calc = input("+ , - , * , / , % 중 하나 입력 : ")

if calc == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
if calc == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
if calc == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
if calc == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
if calc == "%":
    print(f"{num1} % {num2} = {num1 % num2}")