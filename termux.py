import pyautogui as pag
import time
import keyboard as kb
import os

os.environ['DISPLAY'] = ':1'
os.environ['XDG_RUNTIME_DIR'] = '/data/data/com.termux/files/usr/tmp'

def click(x, y):
    pag.click(x, y)

tile2_x, tile2_y = 162, 781
tile3_x, tile3_y = 280, 781
tile4_x, tile4_y = 395, 781
tile1_x, tile1_y = 55, 781

time.sleep(15)

while not kb.is_pressed("e"):
    if pag.pixel(tile1_x, tile1_y)[0] == 0:
        click(tile1_x, tile1_y + 15)
    if pag.pixel(tile2_x, tile2_y)[0] == 0:
        click(tile2_x, tile2_y + 15)
    if pag.pixel(tile3_x, tile3_y)[0] == 0:
        click(tile3_x, tile3_y + 15)
    if pag.pixel(tile4_x, tile4_y)[0] == 0:
        click(tile4_x, tile4_y + 15)
