Return Address Overwrite
https://dreamhack.io/wargame/challenges/351

- Vulnerability

scanf 함수를 통해 입력을 받는 과정에서 입력 길이를 제한하지 않아, 스택의 리턴 어드레스를 덮어쓸 수 있는 스택 버퍼 오버플로우 취약점이 존재합니다.

- Exploit

버퍼의 크기(0x30)와 SFP(0x8)를 쓰레기 값으로 채운 뒤, 리턴 어드레스를 쉘을 실행하는 get_shell 함수의 주소(0x4006aa)로 변조하여 쉘을 획득하도록 페이로드를 작성했습니다.
