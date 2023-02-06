import pyautogui
import time

spaces = 0 
delay_speed = 0.1

def tabbing_mech(line):
    global spaces
    count_space = 0
    for char in line:
        if char == " ":
            count_space += 1
        else:
            break
    print(count_space, spaces, line)

    if spaces > count_space:
        back_tab = (spaces - count_space) // 4
        spaces = count_space
        print("tab back")
        for i in range(back_tab):
            pyautogui.keyDown('shift')
            pyautogui.press('tab')
            pyautogui.keyUp('shift')
        return line.lstrip()
    elif count_space == 0:
        return line
    elif spaces == count_space:
        return line
    elif spaces < count_space:
        print("indenting")
        spaces = count_space
        indent = " " * (count_space - spaces)
        return indent + line.lstrip()

for i in range(3):
    time.sleep(1)
    print(i)

with open("test.py", 'r') as f:
    for lines in f:
        type_me = tabbing_mech(lines)
        pyautogui.typewrite(type_me, delay_speed)
