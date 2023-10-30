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

# 매주 월요일부터 금요일까지 오후 5:00에 작동하도록 스케줄 설정
schedule.every().monday.at('17:00').do(job_that_executes_once)
schedule.every().tuesday.at('17:20').do(job_that_executes_once)
schedule.every().wednesday.at('17:00').do(job_that_executes_once)
schedule.every().thursday.at('17:00').do(job_that_executes_once)
schedule.every().friday.at('17:00').do(job_that_executes_once)

def job_that_executes():
    pyautogui.moveTo(1242,1047, 3)
    pyautogui.click()
    pyautogui.moveTo(1228,666, 3)
    pyautogui.click()
    pyautogui.moveTo(1272,745, 3)
    pyautogui.click()
    pyautogui.moveTo(1386,681, 3)
    pyautogui.click()
    pyautogui.moveTo(360,417, 3)
    pyautogui.click()
    pyautogui.moveTo(1889,19, 3)
    pyautogui.click()
    
    return schedule.CancelJob

# 매주 월요일부터 금요일까지 오후 5:00에 작동하도록 스케줄 설정
schedule.every().monday.at('08:00').do(job_that_executes)
schedule.every().tuesday.at('08:00').do(job_that_executes)
schedule.every().wednesday.at('08:00').do(job_that_executes)
schedule.every().thursday.at('08:00').do(job_that_executes)
schedule.every().friday.at('08:00').do(job_that_executes)


while True:
    schedule.run_pending()
    time.sleep(1)