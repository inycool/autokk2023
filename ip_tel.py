# 윈도우 관리자 권한 얻어 실행
import sys
import os
import win32com.shell.shell as shell
if sys.argv[-1] != 'asadmin':
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

# 마우스 이동 클릭 >> 이동 클릭OK(TACT)
import subprocess
import pyautogui
import time
import pyperclip

# 외부 프로그램 실행 후 로그인 접속하기
program_path = "C:\Program Files (x86)\FACT_TACT\TACT\TACT_CLIENT2\TACTClient.exe"
subprocess.Popen(program_path)
time.sleep(2)
# import pygetwindow as gw
# window = gw.getWindowsWithTitle("TACT 클라이언트 (Ver 2.4.0.9) ::: Online")[0]
# window.activate()

num1=pyautogui.locateCenterOnScreen('tlo1.png')
pyautogui.click(num1)
num2=pyautogui.locateCenterOnScreen('tlo2.png')
pyautogui.click(num2)
time.sleep(12)
# 마우스 포인터위치 확인, 마우스 위치 스크린샷 저장
# #print(pyautogui.position())
# #pyautogui.screenshot('tlo1.png',region=(1250, 588,39,20))
num3=pyautogui.locateCenterOnScreen('c1.png')
pyautogui.click(num3)
time.sleep(1)
num4=pyautogui.locateCenterOnScreen('c2.png')
pyautogui.click(num4)
# 파일에서 첫 번째 행, 첫 번째 열의 내용 읽어오기

import pandas as pd
csv_file_path='iptest.csv'
# csv파일에서 데이터 읽기
df=pd.read_csv(csv_file_path)
# 데이터 프레임의 첫 열, 첫 행 데이터를 가져오기
data_to_copy=df.iloc[0,0]
# 데이터 클립보드에 복사
pyautogui.write(data_to_copy)

# "연결" 클릭
num5=pyautogui.locateCenterOnScreen('c3.png')
time.sleep(1)
pyautogui.click(num5)
