# off_by_one_000
https://dreamhack.io/wargame/challenges/9

- Vulnerability

버퍼의 경계 검사 과정에서 1바이트 오차가 발생하는 Off-by-One 취약점이 존재합니다. 이를 통해 버퍼 뒤에 인접한 데이터나 함수 포인터를 조작할 수 있습니다.

- Exploit

쉘을 실행하는 getshell 함수의 주소(0x80485db)를 64번 반복하여 입력했습니다. 이를 통해 취약점으로 인해 발생하는 메모리 침범 영역을 유효한 주소로 덮어써서 함수 호출 흐름을 조작하여 쉘이 실행되도록 구성했습니다.

<img width="1668" height="2154" alt="image" src="https://github.com/user-attachments/assets/5c4b0d3b-544f-46a4-9fed-3ff6e0dbf995" />


# off_by_one_001
https://dreamhack.io/wargame/challenges/10

- Vulnerability

데이터를 입력받는 과정에서 경계값을 잘못 계산하여 발생하는 Off-by-One 취약점이 존재합니다. 이 취약점으로 인해 버퍼 바로 뒤에 위치한 변수의 값을 널(NULL) 바이트로 덮어쓸 수 있습니다.

- Exploit

버퍼의 크기인 20바이트(0x14)를 가득 채워 입력했습니다. 이를 통해 인접한 변수의 첫 번째 바이트를 0으로 조작함으로써, 프로그램의 로직을 우회하여 의도된 코드가 실행되도록 페이로드를 작성했습니다.

<img width="940" height="591" alt="image" src="https://github.com/user-attachments/assets/2a3843d7-d63d-4f15-8d79-d29a077fecb9" />
