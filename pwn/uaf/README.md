uaf_overwrite
https://dreamhack.io/wargame/challenges/357
- Vulnerability

동적 할당된 메모리를 해제한 후에도 해당 메모리를 가리키는 포인터를 초기화하지 않아, 해제된 메모리 영역에 다시 접근하거나 데이터를 쓸 수 있는 Use-After-Free(UAF) 취약점이 존재합니다.

- Exploit

tcache 범위를 벗어나는 크기(0x500)의 청크를 할당하고 해제하여 Unsorted Bin에 배치함으로써 libc 주소를 유출했습니다. 이후 유출된 주소를 바탕으로 계산한 One-gadget을 객체의 함수 포인터 영역에 덮어썼습니다. 최종적으로 해당 함수 포인터가 호출되는 로직을 실행하여 쉘을 획득하도록 페이로드를 작성했습니다.
