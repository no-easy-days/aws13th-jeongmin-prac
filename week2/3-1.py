from os.path import split

print("# 실습1: 이메일 주소 분리하기")
user_email = input("이메일 : ").strip().split('@',2)
email = user_email[0]
domain = user_email[1]
print(f"email : {email}\t도메인 : {domain}")

print("# 실습2: 비밀번호 길이 검사")
user_pw = input("비밀번호 (8자리 이상) : ")
if len(user_pw) >= 8:
    print("good")
else:
    print("bad")

print("# 실습3: 3배수")
lst1 = []
for i in range(3,20,3):
    lst1.append(i)
print(lst1)

print("# 실습4: 공통 관심사 찾기")
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]
favorite = []
favorite2 = []
for i in chulsoo:
    if i in younghee:
        favorite.append(i)
print(favorite)

print("# 실습5: 최고점수 학생 찾기")
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}
scores2 = scores.values()
scores2 = sorted(scores2)
print(scores2[-1])

