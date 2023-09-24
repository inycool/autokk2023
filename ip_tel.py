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
import pyautogui
import time
# i = pyautogui.locateCenterOnScreen("tactclient.png")
# pyautogui.click(i)
# print(pyautogui.position())
# pyautogui.screenshot('pa1.png',region=(164, 92,42,24))
# pyautogui.screenshot('c1.png')
num1=pyautogui.locateCenterOnScreen('c1.png')
time.sleep(1)
pyautogui.click(num1)
num2=pyautogui.locateCenterOnScreen('c2.png')
time.sleep(1)
pyautogui.leftClick(num2)
num3=pyautogui.locateCenterOnScreen('c3.png')
time.sleep(1)
pyautogui.click(num3)
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
