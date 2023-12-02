from selenium import webdriver
import pyautogui
import time
import keyboard
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import simpledialog

def get_episode_number(): #if written 0 then I want to keep watching from where I have stop watching
    root = tk.Tk()
    root.withdraw()
    episode_number = simpledialog.askinteger("Episode Number", "Enter the episode number you want to start from / keep watching with 0:", minvalue=0)
    return episode_number

def anime_shit(ep_num):
    chrome_options = Options()
    browser = webdriver.Chrome(options=chrome_options)
    me = ep_num
    hello = str(me)
    browser.get("https://animeisrael.website/watch/fulllink/op/fulllinkop-"+hello+".php")
    browser.fullscreen_window()


    while True:
        if keyboard.is_pressed('l'):
            me += 1
            hello = str(me)
            temp = "https://animeisrael.website/watch/fulllink/op/fulllinkop-" + hello + ".php"
            browser.set_script_timeout(0.5)
            browser.get(temp)
            browser.fullscreen_window()
            time.sleep(2)
            pyautogui.doubleClick(960, 648)
            time.sleep(1)
            pyautogui.click(960, 648)
            pyautogui.press('f')
        if keyboard.is_pressed('esc'):
            with open ('C:\helper\ez.txt','w') as file:
                me+=1
                file.write(str(me))
                break


def main():
    ep_num = get_episode_number()
    if ep_num == 0:
        with open('C:\helper\ez.txt') as file:
            D = file.read()
            ep_num = int(D)
    anime_shit(ep_num)


if __name__ == '__main__':
    main()
