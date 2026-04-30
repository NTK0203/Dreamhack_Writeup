# 🛡️ Dreamhack_Writeup study
이 리포지토리는 보안 학습 플랫폼 드림핵(Dreamhack)의 워게임 문제를 풀이하며 시스템 해킹과 리버싱을 독학한 기록을 담고 있습니다. 드림핵의 시스템 해킹, 리버스 엔지니어링 학습 트랙을 완료 하였으며 해당 강의에 나왔던 문제도 포함되어 있습니다.

# 🛠️ Tech Stacks
Languages: C, Python (Pwntools)

Platform: Dreamhack (드림핵)

Tools: GDB (pwndbg), Checksec, IDA-free

# 💡 Study Details
1. Pwn
기본적인 시스템 구조를 이해하고, 이를 바탕으로 다양한 메모리 취약점을 분석하며 보호 기법(ASLR, NX, Canary 등)을 우회하는 페이로드를 설계했습니다.
주요 학습 내용: Stack/Heap Buffer Overflow, ROP, Format String Bug, Use-After-Free 등
구성: 직접 작성한 익스플로잇 스크립트(.py)와 간략한 문제 내용이 포함되어 있습니다.

2. Reversing
컴파일된 바이너리를 IDA를 통한 디컴파일링과 디버거를 통한 어셈블리 수준 정적 분석하고, 디버거로 동적인 레지스터와 메모리 흐름을 관찰하여 플래그를 획득하는 과정을 학습했습니다.
주요 학습 내용: 어셈블리 코드 분석, 암호화 알고리즘 복호화, 안티 디버깅 우회 등

- 그외의 [리버싱 입문, 조성문 저자]로 학습한 기록 및 드림핵 기록 블로그: https://neworld0203.tistory.com/category/%EB%B3%B4%EC%95%88%EA%B3%B5%EB%B6%80 

# 📦 Repository Structure
```text
┣ 📂 pwn
 ┃ ┣ 📂 rao
 ┃ ┃ ┣ 📜 rao.py        # Exploit Script
 ┃ ┃ ┗ 📜 README.md     # 문제 링크 및 내용
 ┃ ┗ 📜 ... (총 23개 항목)
 ┣ 📂 reversing
 ┃ ┣ 📂 rev-basic-9
 ┃ ┗ 📜 ... (총 12개 항목)
 ┗ 📜 README.md
```
