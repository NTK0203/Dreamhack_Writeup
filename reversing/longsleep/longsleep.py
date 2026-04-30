import hashlib

# 해시할 입력 문자열
input_string = "I will evolve into SUPER FLAG!!!!"

# 1. 입력 문자열을 바이트 형태로 변환 (UTF-8 인코딩)
input_bytes = input_string.encode('utf-8')

# 2. SHA-256 해시 객체를 생성하고, 바이트 데이터를 넣어 해시 계산
sha256_hash = hashlib.sha256(input_bytes).hexdigest()

# 3. 결과 출력
print(sha256_hash)