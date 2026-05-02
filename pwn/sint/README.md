sint
https://dreamhack.io/wargame/challenges/25

- Vulnerability

입력받은 정수의 부호 검사 미흡으로 인해 발생하는 Integer Overflow가 존재합니다. 이를 통해 프로그램 내부의 크기 제한 검사를 우회하고 스택 버퍼 오버플로우를 유발할 수 있습니다.

- Exploit

Size 값으로 0을 입력하여 검사 로직을 우회한 뒤, 발생하는 스택 버퍼 오버플로우를 이용했습니다. 260바이트(0x104)의 버퍼와 4바이트의 SFP를 쓰레기 값으로 채우고, 리턴 어드레스를 get_shell 함수의 주소(0x8048659)로 변조하여 쉘을 획득했습니다.
<img width="940" height="850" alt="image" src="https://github.com/user-attachments/assets/af859e41-2854-4cca-a7ca-cb10e0183ef1" />
