import pyautogui
import keyboard
import time

#On my screen
y = 610
x1 = 690
x2 = 870
x3 = 1040
x4 = 1240

i=0

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Start")

while not keyboard.is_pressed('q'):
    if pyautogui.pixel(x1, y)[0] < 5:
        i=i+1
        pyautogui.click(x1, y)

    if pyautogui.pixel(x2, y)[0] < 5:
        i=i+1
        pyautogui.click(x2, y)

    if pyautogui.pixel(x3, y)[0] < 5:
        i=i+1
        pyautogui.click(x3, y)

    if pyautogui.pixel(x4, y)[0] < 5:
        i=i+1
        pyautogui.click(x4, y)
    print(i)

#En esta pagina
#https://www.1001juegos.com/juego/dont-tap-the-white-tile-piano-tiles