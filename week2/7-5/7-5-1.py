# [실습 7.1-1] 텍스트 파일 통계
line = [
    "안녕하세요 저는 윤정민 입니다.\n",
    "텍스트 파일 생성 및 통계 프로그램 연습중입니다.\n",
    "테스트용 문장입니다 바보 메롱."
]

with open("text_file.txt", "w", encoding="utf-8") as f:
    f.writelines(line)


with open("text_file.txt", "r", encoding="utf-8") as f:
    content = ""
    for line in f:
        content += line

print(f"가져온 텍스트\n\n{content}\n")
print(f"총 텍스트 줄 수: {(content).count("\n")+1}줄") # 이래도 되나..
print(f"총 텍스트 수: {len(content)}타")

words = content.split()
max_cnt = max(len(word) for word in words)
# max_cnt = 0
# count = 0
# for i in range(0, len(content)):
#     if content[i] != " ":
#         count += 1
#     elif max_cnt <= count:
#         max_cnt = count
#         count = 0
#
# if count > max_cnt:
#     max_cnt = count

print(f"가장 긴 단어 : {max_cnt}자")
print(f"전체 단어 : {words}")
print(f"전체 단어 수 : {len(words)}")
