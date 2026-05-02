Tcache Poisoning
https://dreamhack.io/wargame/challenges/358
- Vulnerability

해제된 청크의 데이터를 수정할 수 있는 Use After Free(UAF) 취약점이 존재합니다. 이를 이용해 청크의 key 필드를 조작함으로써 tcache의 중복 해제 방지 로직을 우회하고 Double Free를 유발할 수 있습니다.

- Exploit

Double Free를 통해 tcache bin에 사이클을 형성한 후, tcache poisoning 기법으로 stdout 영역에 메모리를 할당받아 libc 베이스 주소를 유출했습니다. 계산된 주소를 바탕으로 다시 한번 poisoning 기법을 사용하여 __free_hook을 원샷 가젯(One-gadget)의 주소로 변조한 뒤, free를 호출하여 쉘을 획득했습니다.

<img width="1668" height="2154" alt="image" src="https://github.com/user-attachments/assets/b45deac7-ad5f-488d-a52f-4ea54c0b0f59" />
