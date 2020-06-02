import pyautogui
import threading
import time

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def clicky():
    pyautogui.click()

set_interval(clicky, 0.5)