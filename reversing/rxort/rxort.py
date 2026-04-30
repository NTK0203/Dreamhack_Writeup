# 1. 목표 문자열
target_str = "C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q"

# 2. 문자열을 아스키코드 정수 리스트로 변환
# C 코드의 'result2' 배열에 해당합니다.
result2 = [ord(char) for char in target_str]

# 3. XOR 연산 되돌리기 (result = result2 ^ 3)
# C 코드의 'result' 배열을 복원합니다.
result = [num ^ 3 for num in result2]

# 4. 순서 뒤집기 연산 되돌리기
# C 코드에서 result 배열은 rot 배열의 역순으로 만들어졌습니다.
# 리스트 슬라이싱 [::-1]을 사용해 간단히 순서를 다시 뒤집습니다.
# 이것이 C 코드의 'rot' 배열에 해당합니다.
rot = result[::-1]

# 5. ROT-13 및 마스킹 연산 되돌리기
# 원래 연산: rot = (input + 13) & 0x7F (이는 128 모듈러 연산과 유사)
# 역연산: input = (rot - 13) % 128
# 파이썬의 % 연산자는 결과가 음수일 때도 올바르게 처리해 주므로 편리합니다.
original_codes = [(val - 13) % 128 for val in rot]

# 6. 정수 리스트를 최종 문자열(플래그)로 변환
flag = "".join([chr(code) for code in original_codes])

print(f"DH{flag}")