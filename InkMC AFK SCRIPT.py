import pyautogui
import time

while True:
    try:
        print("Taking screenshot")
        screenshot = pyautogui.screenshot()
        print("Screenshot taken")

        print("Locating 'back.png'")
        location = pyautogui.locateCenterOnScreen('back.png')
        print(f"'back.png' location: {location}")

        if location:
            print("Found 'back' image")
            pyautogui.click(location)
            time.sleep(1)

            print("Moving to and clicking Direct Connection")
            pyautogui.moveTo(950, 996)
            pyautogui.click(x=950, y=996)
            print("Clicked Direct Connection")
            time.sleep(1)

            print("Moving to Server IP Tab")
            pyautogui.moveTo(x=947, y=250)
            time.sleep(1) 
            print("Clicking Server IP Tab")
            pyautogui.click()
            time.sleep(1) 

            print("Typing 'inkmc.pl'")
            pyautogui.typewrite('inkmc.pl', interval=0.1)
            time.sleep(2)
            print("Typed 'inkmc.pl'")

            print("Moving to and clicking second coordinates")
            pyautogui.moveTo(x=947, y=493)
            time.sleep(1)
            pyautogui.click(x=947, y=493)
            time.sleep(10)
            print("Clicked second coordinates")

            print("Right-clicking")
            pyautogui.rightClick(x=950, y=406)
            time.sleep(3) 

            print("Clicking third coordinates")
            pyautogui.click(x=950, y=406)

        print("Pausing before next iteration")
        time.sleep(15)

    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(45)

