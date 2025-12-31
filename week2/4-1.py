import random
# print("# 실습 4-1 : 등급 판정")
# score = int(input("점수 입력 : "))
# while True:
#     if score < 0 or score > 100:
#         score = int(input("점수 다시 입력 : "))
#     elif score >= 90:
#         print(f"{score}점은 A등급 입니다.")
#         break
#     elif score >= 80:
#         print(f"{score}점은 B등급 입니다.")
#         break
#     elif score >= 70:
#         print(f"{score}점은 C등급 입니다.")
#         break
#     elif score >= 60:
#         print(f"{score}점은 D등급 입니다.")
#         break
#     elif score >= 50:
#         print(f"{score}점은 E등급 입니다.")
#         break
#     elif score >= 40:
#         print(f"{score}점은 F등급 입니다.")
#         break
#     else:
#         print(f"{score}점은... 흠...")
#         break
#
print("# 실습 4-2 : 구구단 출력")
몇단 = int(input("구구단 몇단(1~9) 숫자만 입력 : "))
for i in range(1, 10):
    print(f"{몇단} * {i} = {몇단*i}")


print("# 실습 4-3 : 소수 판별")
for i in range(2, 101): # 2부터 100까지
    소수 = True
    for j in range(2,i):
        if i % j == 0:
            소수 = False
            break
    if 소수 is True:
        print(i,end=" ")

print("# 실습 4-4 : 숫자 맞추기")
랜덤 = int(random.randint(1, 100))
트라이 = 1
while True:
    게스넘 = int(input("맞쳐보라(1~100) : "))
    if 랜덤 == 게스넘:
        print(F"ㅊㅋ {트라이}번 시도")
        break
    elif 랜덤 >= 게스넘:
        print("UP")
        트라이 += 1
    elif 랜덤 <= 게스넘:
        print("DOWN")
        트라이 += 1

