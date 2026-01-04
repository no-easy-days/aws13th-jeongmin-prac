# 실무 시나리오 - 로그분석
import json

with open('logs.json',"r",encoding="utf-8") as json_file:
    logs = json.load(json_file)

errors = []
for log in logs:
    if log['level'] == 'ERROR':
        errors.append(log)

with open('errors.json',"w",encoding="utf-8") as json_file:
    json.dump(errors,json_file,ensure_ascii=False,indent=4)
print(errors)