Long Sleep
https://dreamhack.io/wargame/challenges/635

- Vulnerability

문제 바이너리에서 분석한 특정 데이터의 해시값을 계산해내는 문제입니다.

- Exploit

문제에서 제시된 문자열인 "I will evolve into SUPER FLAG!!!!"를 SHA-256 해시 알고리즘을 통해 변환하여 플래그를 도출했습니다. 파이썬의 hashlib 라이브러리를 활용하여 해당 문자열을 바이트 형태로 인코딩한 뒤, SHA-256 해시 객체에 입력하여 16진수 형태의 다이제스트를 출력하는 방식으로 페이로드를 구성했습니다.
