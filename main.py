import time
import pyautogui
import keyboard
import win32con
import win32api

tile3_x, tile3_y = 517, 650
tile2_x, tile2_y = 430, 650
tile4_x, tile4_y = 606, 650
tile1_x, tile1_y = 357, 650

time.sleep(5)

print("Script is Running....")

def click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.SetCursorPos((x, y))
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed("e"):
    if pyautogui.pixel(tile1_x, tile1_y)[0] == 0:
        click(tile1_x, tile1_y + 15)

    if pyautogui.pixel(tile2_x, tile2_y)[0] == 0:
        click(tile2_x, tile2_y + 15)

    if pyautogui.pixel(tile3_x, tile3_y)[0] == 0:
        click(tile3_x, tile3_y + 15)

    if pyautogui.pixel(tile4_x, tile4_y)[0] == 0:
        click(tile4_x, tile4_y + 15)
