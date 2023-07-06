import win32api, win32con
import pyautogui as pag
import time
import keyboard as kb

def click (x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
tile2_x, tile2_y = 665,600
tile3_x, tile3_y = 763,600
tile4_x, tile4_y = 861,600
tile1_x, tile1_y = 600,600

time.sleep(3)
while not kb.is_pressed("e"):
    if pag.pixel(tile1_x, tile1_y)[0] == 0:
        click(tile1_x, tile1_y + 15)
    if pag.pixel(tile2_x, tile2_y)[0] == 0:
        click(tile2_x, tile2_y + 15)
    if pag.pixel(tile3_x, tile3_y)[0] == 0:
        click(tile3_x, tile3_y + 15)
    if pag.pixel(tile4_x, tile4_y)[0] == 0:
        click(tile4_x, tile4_y + 15)