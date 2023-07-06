import pyautogui as pag
import keyboard as kb


if kb.read_key('enter'):
    pos = pag.position()
    print(pos)