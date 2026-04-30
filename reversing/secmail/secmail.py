import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

HTML_FILE_NAME = "secure-mail.html"

# WebDriver 설정 (chromedriver.exe가 같은 폴더에 있어야 함)
driver = webdriver.Chrome()

# 로컬 HTML 파일의 절대 경로를 가져옴
file_path = "file://" + os.path.abspath(HTML_FILE_NAME)

try:
    # 000000부터 999999까지 모든 조합 시도
    for i in range(1000000):
        password = f"{i:06d}" # 숫자를 6자리 문자열로 변환 (예: 123 -> "000123")
        
        # HTML 파일 열기
        driver.get(file_path)

        # 100번 시도할 때마다 진행 상황 출력
        if i % 100 == 0:
            print(f"[*] 시도 중: {password}")

        try:
            # 1. 비밀번호 입력창 찾기 (id가 'pass'인 요소)
            password_input = driver.find_element(By.ID, "pass")
            
            # 2. 버튼 찾기 (태그 이름이 'button'인 요소)
            confirm_button = driver.find_element(By.TAG_NAME, "button")

            # 3. 비밀번호 입력 및 버튼 클릭
            password_input.send_keys(password)
            confirm_button.click()
            
            # 4. 성공 여부 확인 (경고창이 뜨는지 확인)
            time.sleep(0.05) 
            
            alert = driver.switch_to.alert
            # 'Wrong' 경고창이 있으면 확인을 누르고 다음 번호로 넘어감
            alert.accept()

        except NoAlertPresentException:
            print("\n==============================")
            print(f"성공, 비밀번호: {password}")
            
            # 성공 시 페이지 내용이 flag로 바뀌므로, 바뀐 내용을 가져옴
            flag_content = driver.find_element(By.TAG_NAME, 'body').text
            print(f"메일 내용: {flag_content}")
            print("==============================")
            break # 성공했으므로 반복문 종료
            
except Exception as e:
    print(f"\n오류 발생: {e}")

finally:
    # 5초 후 브라우저 창 닫기
    print("\n[+] 5초 후에 종료")
    time.sleep(5)
    driver.quit()