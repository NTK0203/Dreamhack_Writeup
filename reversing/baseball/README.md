baseball
https://dreamhack.io/wargame/challenges/105

- Vulnerability

표준 Base64 인코딩 알고리즘을 사용하지만, 인덱싱에 사용되는 문자 테이블이 변조되어 있어 일반적인 방식으로는 디코딩이 불가능합니다.

- Exploit

제공된 평문 데이터(text_in)와 인코딩된 데이터(text_out)를 비트 단위로 비교 분석하여 변조된 64글자의 테이블을 복원했습니다. 이후 복원된 테이블을 사용하여 flag_out의 각 문자를 인덱스로 역치환하고, 비트 연산을 통해 원래의 바이트 데이터로 복원하여 플래그를 획득했습니다.

<img width="923" height="298" alt="image" src="https://github.com/user-attachments/assets/fb63d887-502f-48db-82da-049511a61350" />
