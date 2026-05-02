basic_heap_overflow
https://dreamhack.io/wargame/challenges/66

- Vulnerability

데이터가 할당된 힙 영역에서 입력값의 길이를 검사하지 않아, 할당된 버퍼의 크기를 초과하여 데이터를 입력할 수 있는 Heap Buffer Overflow 취약점이 존재합니다.

- Exploit

힙 영역에 할당된 버퍼와 함수 포인터 사이의 거리인 40바이트(0x28)만큼 쓰레기 값을 채운 뒤, 뒤따라오는 함수 포인터를 get_shell 함수의 주소(0x804867b)로 덮어씌워 쉘이 실행되도록 페이로드를 작성했습니다.
<img width="940" height="330" alt="image" src="https://github.com/user-attachments/assets/3454158d-4e53-4291-8fde-956c040bdfe1" />
