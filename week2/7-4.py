# --------------------------------------------------------------------------------------
# from datetime import datetime
# print("\n# 실습 7-4-1 : import 기본사용")
#
# import datetime
# today = datetime.date.today()
# print(today)
# --------------------------------------------------------------------------------------
# print("\n# 실습 7-4-2 : from import 사용")
# from math import sqrt as s, pow as p
# print(s(16))
# print(p(2,10))
# --------------------------------------------------------------------------------------
# print("\n# 실습 7-4-3 : as 사용")
# import random as rd
# print(rd.randint(1, 100))
# print(rd.randint(1, 100))
# --------------------------------------------------------------------------------------
# print("\n# 실습 7-4-4 : pip 명령어")
# 터미널 > pip install requests
# 터미널 > pip install pandas==2.0.0
# 터미널 > freeze > requirements.txt
# --------------------------------------------------------------------------------------
# print("\n# 실습 7-4-5 : 가상환경 명령어(mac 기준)")
# 터미널 > mkdir my_app
# 터미널 > cd my_app
# 터미널 > python3 -m venv venv # 가상환경 생성
# 터미널 > source venv/bin/activate # 가상환경 활성화
# (venv) my_app % 로 터미널 앞에 표시됨
# (venv) my_app % deactivate # 가상환경 비활성화
# --------------------------------------------------------------------------------------
print("\n# 실습 7-4-6 : 실무 시나리오(mac 기준)")
# 터미널 > mkdir weather_app
# 터미널 > cd weather_app
# 터미널 > python3 -m venv venv
# 터미널 > python3 -m pip install requests python-dotenv
# 터미널 > python3 -m pip freeze > requirments.txt