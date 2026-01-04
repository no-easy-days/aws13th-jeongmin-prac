# 위험한 코드 찾기
# name = input("이름: ")
# age = input("나이: ")
#
# sql = f"INSERT INTO students VALUES ('{name}', {age})"
# cursor.execute(sql)

"""사용자 입력값을 문자열로 SQL 문에 직접 끼워넣음 > 사용자의 입력이 데이터가 아니라 SQL 명령어로 사용될 수 있음
 홍길동'); DROP TABLE students; -- 이런식의 값을 넣게되면
 INSERT INTO students VALUES ('홍길동'); DROP TABLE students; --', 20) 이런식의 결과 값이 생성될 수 있음
"""

# 플레이스홀더를 이용한 안전한 쿼리문
# name = input("이름: ")
# age = input("나이: ")
# sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
# cursor.execute(sql, (name, age))


# 공격 시나리오 분석
# product_name = input("검색할 상품: ")
# sql = f"SELECT * FROM products WHERE name = '{product_name}'"

""" SELECT 문에서 항상 참이되는 조건을 만들기 위해서 ' or '1'='1' 을 입력"""

""" 위험한 코드 > 안전한 코드로 바꾸기 """
# keyword = input("검색어: ")
# sql = f"""
#     SELECT * FROM posts
#     WHERE title LIKE '%{keyword}%'
#     OR content LIKE '%{keyword}%'
#     OR author LIKE '%{keyword}%'
# """

""" 수정한 코드 """
# keyword = input("검색어: ")
# sql = """
# SELECT *
# FROM posts
# WHERE title   LIKE %(kw)s
#    OR content LIKE %(kw)s
#    OR author  LIKE %(kw)s
# """
#
# params = {
#     "kw": f"%{keyword}%"
# }
#
# cursor.execute(sql, params)
""" 문자열 포매팅 삭제, kw 라는 이름 키로 값을 매핑, 같은 값을 여러번 써도 한번만 정의"""