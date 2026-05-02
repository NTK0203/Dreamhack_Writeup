memory_leakage
https://dreamhack.io/wargame/challenges/69
- Vulnerability

입력받은 문자열의 끝에 널(NULL) 문자가 포함되지 않아 발생하며, 이로 인해 출력 함수가 버퍼의 경계를 넘어 뒤에 위치한 데이터를 함께 출력하는 메모리 유출(Memory Leak) 취약점이 존재합니다.

- Exploit

먼저 3번을 호출하여 플래그를 메모리에 로드했습니다. 그 후 name 버퍼의 크기인 16바이트(0x10)를 널 문자 없이 가득 채워 문자열의 경계를 제거했습니다. 이후 2번을 실행하여 name 버퍼 바로 뒤에 위치한 플래그 값이 함께 출력되도록 페이로드를 작성했습니다.
<img width="940" height="664" alt="image" src="https://github.com/user-attachments/assets/0f7c4dd0-4050-4410-80bd-c263493baab0" />
