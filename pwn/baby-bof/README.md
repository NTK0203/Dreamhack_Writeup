baby-bof
https://dreamhack.io/wargame/challenges/974
- Vulnerability

사용자로부터 입력받은 count에 대한 경계 검사가 존재하지 않아, name 배열의 범위를 벗어나 메모리에 값을 쓸 수 있는 buffer overflow 취약점이 존재합니다.

- Exploit

64비트 환경의 스택 구조상 name 배열(16바이트)과 SFP(8바이트)를 지나면 Return Address가 위치합니다. 따라서 count를 4로 입력하여 인덱스 3에 위치한 Return Address를 win 함수의 주소로 덮어씀으로써, 함수 종료 시 win 함수가 호출되어 플래그가 출력되도록 페이로드를 작성했습니다.
<img width="1668" height="2154" alt="image" src="https://github.com/user-attachments/assets/9ebf4262-333e-4b78-b929-cd872c5a326d" />
