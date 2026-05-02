mix-compare
https://dreamhack.io/wargame/challenges/961

Vulnerability
사용자로부터 입력받은 64바이트 길이의 문자열을 총 6개의 검증 함수(check, check_not, check_add, check_dec, check_mul, check_la)를 거쳐 .data 섹션에 저장된 상수 배열과 비교하는 리버싱 문제입니다. 각 함수는 특정 구간의 문자들에 대해 서로 다른 산술 및 비트 연산을 수행합니다.

Exploit
바이너리 분석을 통해 각 검증 함수가 수행하는 연산(덧셈, 나눗셈, 비트 NOT, 인덱스 가산 등)을 파악하고, 비교 대상이 되는 result_bytes 데이터를 추출했습니다. 이후 각 구간별로 연산 과정을 거꾸로 수행하는 역연산 로직을 설계했습니다. 특히 부호 있는 32비트 정수 연산과 비트 반전 시 발생하는 처리를 정확하게 구현하기 위해 ctypes 모듈을 활용하여 원본 플래그 문자열을 복원했습니다.
