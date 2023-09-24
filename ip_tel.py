# import pandas as pd
# # CSV 파일 불러오기
# df = pd.read_excel("testlist.xlsx")
# # 데이터프레임의 상위 몇 개 행 출력 (기본값은 5개)
# print(df.head())

# import os
# import subprocess
# env = os.environ
# newpath = r"C:\Program Files (x86)\FACT_TACT\TACT\TACT_CLIENT2;"+env['PATH']
# env['PATH'] = newpath 
# r = subprocess.run('TACTClient.exe push1.tcl',shell=True, capture_output=True, text=True) 
# # CompletedProcess returned
# print(r.args)
# print(r.returncode)
# print(r.stderr)
# print(r.stdout)

# 마우스 이동 클릭 >> 이동가능,클릭불가(TACT), 웹, 탐색기 정상 클릭됨
import subprocess
import pyautogui
import time
import pyperclip

# 외부 프로그램 실행 후 로그인 접속하기
program_path = "C:\Program Files (x86)\FACT_TACT\TACT\TACT_CLIENT2\TACTClient.exe"
subprocess.Popen(program_path)
time.sleep(2)
import pygetwindow as gw
window = gw.getWindowsWithTitle("TACT 클라이언트 (Ver 2.4.0.8) ::: Online")[0]
window.activate()

num1=pyautogui.locateCenterOnScreen('tlo1.png')
pyautogui.click(num1)
num2=pyautogui.locateCenterOnScreen('tlo2.png')
pyautogui.click(num2)
time.sleep(12)
# 실행 후 마우스이동,클릭하기
# #print(pyautogui.position())
# #pyautogui.screenshot('tlo1.png',region=(1250, 588,39,20))
num3=pyautogui.locateCenterOnScreen('c1.png')
pyautogui.click(num3)
time.sleep(1)
num4=pyautogui.locateCenterOnScreen('c2.png')
pyautogui.click(num4)
# 파일에서 첫 번째 행, 첫 번째 열의 내용 읽어오기
with open("iptest.log", "r") as file:
    first_line = file.readline().strip().split()[0]

# 클립보드에 복사
pyperclip.copy(first_line)
import keyboard
keyboard.press_and_release("ctrl+v")
    
num5=pyautogui.locateCenterOnScreen('c3.png')
time.sleep(1)
pyautogui.click(num5)

# pyautogui.click(x=31,y=264)
# pyautogui.click(x=31,y=264)

# 윈도우 관리자 권한 얻어 실행하는 방법
# import sys
# import os
# import win32com.shell.shell as shell
# if sys.argv[-1] != 'asadmin':
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
