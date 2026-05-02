hook
https://dreamhack.io/wargame/challenges/52
- Vulnerability

프로그램에서 제공하는 임의 주소 쓰기 기능을 통해 특정 메모리 영역의 값을 변조할 수 있는 취약점이 존재합니다. 특히, 동적 할당 해제 시 호출되는 __free_hook을 덮어써 프로그램의 실행 흐름을 조작할 수 있습니다.

- Exploit

실행 시 제공되는 stdout 주소를 이용해 libc 베이스 주소와 __free_hook의 주소를 계산했습니다. 이후 임의 주소 쓰기를 통해 __free_hook을 쉘을 실행하는 특정 주소로 변조하여, free 함수가 호출될 때 의도한 코드가 실행되도록 페이로드를 작성했습니다.
