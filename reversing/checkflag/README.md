checkflag
https://dreamhack.io/wargame/challenges/97

- Vulnerability

사용자 입력값과 플래그를 비교하는 과정에서 전체 문자열이 아닌 특정 길이나 버퍼 상태에 따라 부분적인 일치 여부를 확인할 수 있는 로직 취약점이 존재합니다.

- Exploit

먼저 입력값의 길이를 조절하며 서버의 응답(Correct! 여부)을 확인하여 플래그의 정확한 길이를 파악했습니다. 이후 브루트 포스(Brute-force) 방식을 적용하여, 한 바이트씩 문자를 대입하고 슬라이딩 윈도우 방식으로 페이로드를 구성해 전체 플래그를 한 글자씩 복원했습니다.

<img width="923" height="680" alt="image" src="https://github.com/user-attachments/assets/39b91485-1147-49e1-a7e8-068ed3859722" />
