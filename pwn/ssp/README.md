# ssp_000
https://dreamhack.io/wargame/challenges/32

- Vulnerability

버퍼 오버플로우를 통한 스택 카나리 변조 유도 및 메모리의 임의 주소에 값을 쓸 수 있는 취약점이 존재합니다.

- Exploit

스택 카나리 오염 시 호출되는 __stack_chk_fail 함수의 GOT 엔트리를 get_shell 함수의 주소로 변조했습니다. 이후 의도적으로 버퍼 오버플로우를 발생시켜 카나리 검증 실패를 유도함으로써, 프로그램 종료 대신 쉘이 실행되도록 페이로드를 작성했습니다.
<img width="1668" height="2154" alt="image" src="https://github.com/user-attachments/assets/b91fd04b-a8d0-4573-aeed-76e733614246" />

# ssp_001
https://dreamhack.io/wargame/challenges/33

- Vulnerability

배열 인덱스 입력에 대한 검증 부족으로 발생하는 Out-of-Bounds Read 취약점과 스택 리턴 어드레스를 덮어쓸 수 있는 버퍼 오버플로우 취약점이 존재합니다.

- Exploit

인덱스 조작(OOB Read)을 통해 스택상에 위치한 카나리 값을 읽어 유출했습니다. 유출된 카나리 값을 페이로드에 포함하여 스택 보호 기법을 우회하고, 리턴 어드레스를 getshell 함수의 주소로 변조하여 쉘을 획득했습니다.
