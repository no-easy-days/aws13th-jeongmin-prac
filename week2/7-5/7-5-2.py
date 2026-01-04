from datetime import datetime
import os


class DiaryManager:
    def __init__(self, folder='diary'): # 생성자 매서드, 객체 생성시 자동 실행 및 folder 기본값 = diary로 지정
        self.folder = folder
        os.makedirs(folder, exist_ok=True) # os 모듈의 폴더 생성 매서드, 이미 존재하는 폴더명이면 오류없이 진행 "True"

    def write_diary(self, content, date = datetime.now().strftime('%Y-%m-%d')): # Content와 date를 매개변수로 지정, date 미입력시 현재 시간으로 값 지정

        filename = f"{self.folder}/diary_{date}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"일기 저장: {filename}")

    def read_diary(self, date): # 날짜를 기준으로 작성된 일기 조회
        filename = f"{self.folder}/diary_{date}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"{date} 날짜의 일기가 없습니다."

    def list_diaries(self):
        """모든 일기 목록 보기"""
        files = [f for f in os.listdir(self.folder) if f.startswith('diary_')]
        files.sort()
        return files


# 사용 예시
diary = DiaryManager()
diary.write_diary("오늘 파일 입출력을 배웠다!")
diary.write_diary("어제는 파일 입출력을 배웠다!","2026-01-05")
print(diary.read_diary(datetime.now().strftime('%Y-%m-%d')))
print(diary.read_diary("2026-01-05"))
print("일기 목록:", diary.list_diaries())