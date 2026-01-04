import os

# CHUNK_SIZE = 4096 > 큰파일을 읽을때 메모리에 한번에 올라가는것을 막음

def copy_file(src_path, dst_path, chunk_size = 4096):
    """파일 복사 매서드 정의 : 복사될 파일 경로, 복사된 파일 저장 경로, 청크사이즈 기본값 : 4kb"""
    if not os.path.isfile(src_path):
        print(f"원본 파일이 없습니다: {src_path}")
        return
    try:
        with open(src_path, "rb") as src, open(dst_path, "wb") as dst:
            while True:
                chunk = src.read(chunk_size) # 4kb 씩 읽다가
                if not chunk: # EOF > brake
                    break
                dst.write(chunk) # 청크 사이즈만큼 읽고 append 반복
    except Exception as e:
        print(f"파일 처리 중 문제가 발생했습니다: {e}")
        return

    # 파일 사이즈 비교
    src_size = os.path.getsize(src_path)
    dst_size = os.path.getsize(dst_path)
    print(f"복사 성공: {src_path} -> {dst_path}")
    print(f"원본 크기: {src_size} bytes")
    print(f"사본 크기: {dst_size} bytes")
    if src_size == dst_size:
        print("크기 비교 일치")
    else:
        print("크기 비교 불일치")

# 테스트
with open('original.txt', 'w', encoding='utf-8') as f:
    f.write("테스트 파일입니다.\n" * 100)

copy_file('original.txt', 'copied.txt')