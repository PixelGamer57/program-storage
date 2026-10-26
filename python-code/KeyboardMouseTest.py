import keyboard as k
import pyautogui as p
import math as m
p.FAILSAFE=False

speed = 50
rot = 0

while(True):
    if(k.is_pressed('left')):
        rot -= 0.1
    if(k.is_pressed('right')):
        rot += 0.1
    if(k.is_pressed('up')):
        p.move(speed * m.cos(m.radians(rot)), speed * m.sin(m.radians(rot)))
    if(k.is_pressed('down')):
        p.move(-speed * m.cos(rot), -speed * m.sin(rot))
        
    if(k.is_pressed('k')):
        p.click()
    if(k.is_pressed('l')):
        p.rightClick()