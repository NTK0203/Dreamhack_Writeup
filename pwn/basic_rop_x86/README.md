basic_rop_x86
https://dreamhack.io/wargame/challenges/30

- Vulnerability

32비트 환경에서 입력 길이에 대한 검증이 부족하여 스택의 리턴 어드레스를 제어할 수 있는 스택 버퍼 오버플로우 취약점이 존재합니다.

- Exploit

함수 호출 규약에 따라 스택에 인자를 구성하여 write 함수로 read 함수의 GOT 주소를 leak 했습니다 . pppr 가젯을 사용하여 스택을 정리한 뒤 main 함수로 돌아가 libc 베이스를 기반으로 system("/bin/sh")을 호출하는 페이로드를 실행했습니다.
