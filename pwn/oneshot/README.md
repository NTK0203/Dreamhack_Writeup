oneshot
https://dreamhack.io/wargame/challenges/34

- Vulnerability

프로그램 실행 중 libc 내의 stdout 주소가 유출되며, 사용자 입력 과정에서 버퍼의 크기를 검사하지 않아 스택의 리턴 어드레스를 덮어쓸 수 있는 스택 버퍼 오버플로우 취약점이 존재합니다.

- Exploit

유출된 stdout 주소를 기반으로 libc 베이스 주소와 One-gadget의 주소를 계산했습니다. 이후 스택 버퍼 오버플로우를 발생시켜 리턴 어드레스를 원샷 가젯의 주소로 변조했습니다. 이때 가젯이 성공적으로 실행될 수 있도록 스택의 특정 위치를 널 바이트로 채우는 조건을 만족시켜 쉘을 획득했습니다.
