rop
https://dreamhack.io/wargame/challenges/354
- Vulnerability

사용자 입력 과정에서 버퍼의 크기를 검증하지 않아 스택 카나리를 유출하고 리턴 어드레스를 덮어쓸 수 있는 스택 버퍼 오버플로우 취약점이 존재합니다.

- Exploit

먼저 버퍼 오버플로우를 이용해 스택 카나리 값을 유출했습니다. 이후 가젯을 활용하여 write 함수로 read 함수의 GOT 주소를 출력해 libc 베이스 주소를 계산했습니다. 이어서 read 함수로 read 함수의 GOT를 system 함수의 주소로 덮어쓰고 바로 뒤에 "/bin/sh" 문자열을 작성한 뒤, 변조된 read 함수를 호출하여 system("/bin/sh")이 실행되도록 ROP 체인을 구성했습니다.
