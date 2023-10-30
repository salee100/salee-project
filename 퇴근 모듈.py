import schedule
import pyautogui
import time

def job_that_executes_once():
    pyautogui.moveTo(1242,1047, 3)
    pyautogui.click()
    pyautogui.moveTo(1228,666, 3)
    pyautogui.click()
    pyautogui.moveTo(1272,745, 3)
    pyautogui.click()
    pyautogui.moveTo(1386,681, 3)
    pyautogui.click()
    pyautogui.moveTo(546,411, 3)
    pyautogui.click()
    pyautogui.moveTo(1889,19, 3)
    pyautogui.click()

    return schedule.CancelJob

schedule.every().day.at('17:00').do(job_that_executes_once)

while True:
    schedule.run_pending()
    time.sleep(1)