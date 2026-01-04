# JSON 수정 및 저장
import json

with open('config.json') as json_file:
    config = json.load(json_file)

config['debug'] = "True"

if "notifications" not in config["features"]:
    config["features"].append("notifications")

with open('config_update.json',"w",encoding="utf-8") as json_file:
    json.dump(config,json_file,ensure_ascii=False,indent=4)