cmd_center
https://dreamhack.io/wargame/challenges/117

- Vulnerability
  
프로그램에서 system 함수를 호출할 때 사용하는 명령문 버퍼에 입력 값의 길이를 제한하지 않아 발생하는 버퍼 오버플로우 취약점이 존재합니다. 이를 통해 기존 실행되도록 설정된 명령어 뒤에 사용자가 원하는 명령어를 추가로 삽입할 수 있습니다.

- Exploit

기존 명령어(ifconfig)가 저장되는 버퍼의 크기인 32바이트(0x20)를 쓰레기 값으로 채운 뒤, ; /bin/sh를 입력하여 시스템 명령어를 조작했습니다. 이를 통해 의도된 명령어 실행 이후 쉘이 실행되도록 페이로드를 작성했습니다.
<img width="940" height="761" alt="image" src="https://github.com/user-attachments/assets/94154a94-4b35-46c1-97f8-612fc2565785" />
