import pyautogui
import time

for i in range(16):
    pyautogui.click(1895, 175+i*52)
    time.sleep(0.5)

#各色を0~15で示し、
#pyautogui.click(1895, 175+number*52)
#をすれば、色を選択できる