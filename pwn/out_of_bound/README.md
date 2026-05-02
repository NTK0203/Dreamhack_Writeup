out_of_bound
https://dreamhack.io/wargame/challenges/11

- Vulnerability

사용자로부터 입력받은 인덱스 값에 대한 경계 검사가 수행되지 않아, 배열 범위를 벗어난 메모리 영역에 접근할 수 있는 Out-of-Bounds 취약점이 존재합니다.

- Exploit

특정 버퍼에 "/bin/sh" 문자열과 해당 버퍼의 주소를 삽입했습니다. 이후 배열의 인덱스로 21을 전달하여 프로그램이 배열 외부의 메모리를 참조하게 함으로써, 결과적으로 system("/bin/sh")이 실행되도록 페이로드를 작성했습니다.
