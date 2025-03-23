from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import math
from time import sleep
import pyautogui
import datetime
import os
from selenium.common.exceptions import WebDriverException

# 座標の設定
x = 123456
y = 123456

# スクリーンショット保存用のディレクトリ確認
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# WebDriverの設定
service = Service('C:\\Users\\setsu\\Documents\\everyonedraw-auto\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    for i in range(10):
        for j in range(10):
            try:
                url = "https://everyonedraw.com/46/" + str(x+i) + "/" + str(y+j)
                
                driver.get(url)
                sleep(3)
                
                screen_width, screen_height = pyautogui.size()
                center_x = screen_width // 2
                center_y = screen_height // 2
                
                pyautogui.click(center_x, center_y)
                
                # スクリーンショットを撮る
                now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = f"screenshots/{x+i}_{y+j}_{now}.png"
                driver.save_screenshot(screenshot_path)
                
                sleep(0.5)
                
            except Exception as e:
                # エラー発生時にスクリーンショットを撮る
                now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                error_screenshot = f"screenshots/error_{x+i}_{y+j}_{now}.png"
                try:
                    driver.save_screenshot(error_screenshot)
                except:
                    pass
                print(f"エラーが発生しました: {str(e)}")
                
finally:
    # ループ終了後、ドライバーを終了
    driver.quit()

