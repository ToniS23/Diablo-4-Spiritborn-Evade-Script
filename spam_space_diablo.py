import pyautogui
import keyboard
import time

spamming = False

def toggle_spam():
    global spamming
    spamming = not spamming
    if spamming:
        print("Spamming started...")
    else:
        print("Spamming stopped...")

keyboard.add_hotkey('space', toggle_spam)

while True:
    if spamming:          
        pyautogui.press('space')
        time.sleep(0.001) # delay between presses
    time.sleep(0.01) # delay for avoiding extreme CPU usage
