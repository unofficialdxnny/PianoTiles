import pyautogui as pag
import keyboard as kb



print("press enter when over the tile row...")
if kb.read_key('enter'):
    pos = pag.position()
    print(pos)