# tcache_dup
https://dreamhack.io/wargame/challenges/60

- Vulnerability

이미 해제된 힙 메모리를 중복해서 해제할 수 있는 Double Free 취약점이 존재합니다.

- Exploit

동일한 인덱스의 청크를 두 번 해제하여 tcache bin 내부에 사이클을 형성했습니다. 이후 다시 메모리를 할당받는 과정에서 청크의 fd를 puts GOT 주소로 변조하는 tcache Poisoning 기법을 사용했습니다. 최종적으로 할당된 puts GOT 영역을 get_shell 주소로 덮어써 쉘을 획득했습니다.

# tcache_dup2
https://dreamhack.io/wargame/challenges/67

- Vulnerability

해제된 청크의 데이터를 수정할 수 있는 Use After Free(UAF) 취약점과 이를 연계한 Double Free 취약점이 존재합니다.

- Exploit

청크를 한 번 해제한 상태에서 modify 함수를 이용해 데이터를 조작하여 tcache의 중복 해제 방지 로직을 우회하고 Double Free를 수행했습니다. 이를 통해 tcache bin에 사이클을 만든 후, puts GOT 주소를 fd에 삽입하여 해당 위치에 메모리를 할당받았습니다. 이후 puts GOT를 get_shell 주소로 변조하여 페이로드를 완성했습니다.
