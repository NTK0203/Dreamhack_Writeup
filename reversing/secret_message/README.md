secret message
https://dreamhack.io/wargame/challenges/235

- Vulnerability

플래그 데이터가 특정 압축 알고리즘(Run-Length Encoding, RLE)으로 인코딩되어 있어, 해당 알고리즘의 동작 방식을 정확히 파악하지 못하면 원본 데이터를 복원할 수 없도록 정보가 은닉되어 있습니다.

- Exploit

바이너리 분석을 통해 인코딩된 파일(secretMessage.enc)의 구조를 파악했습니다. 연속된 두 바이트가 동일할 경우, 바로 뒤에 오는 바이트를 반복 횟수로 취급하는 변형된 RLE 알고리즘임을 확인했습니다. 이를 바탕으로 파일을 바이트 단위로 읽어 동일한 바이트 쌍이 나타날 때마다 지정된 횟수만큼 데이터를 반복 추가하는 복호화 스크립트를 작성하여 원본 파일(secretMessage.raw)과 플래그를 복원했습니다.
