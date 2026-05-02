Format String Bug
https://dreamhack.io/wargame/challenges/356
- Vulnerability

printf 함수 호출 시 사용자가 제어할 수 있는 입력값이 포맷 스트링으로 전달되어 메모리의 원하는 위치에 값을 읽거나 쓸 수 있는 포맷 스트링 버그 취약점이 존재합니다.

- Exploit

포맷 스트링을 이용해 스택상의 주소를 유출하여 PIE 베이스 주소와 전역 변수 changeme의 주소를 계산했습니다. 이후 %n 포맷 스트링을 사용하여 changeme 변수의 값을 1337로 변조함으로써 플래그를 출력하도록 페이로드를 작성했습니다.
