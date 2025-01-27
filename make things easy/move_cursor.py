#works on windows  OS only 
#hmmmm i wonder what else i can use this code for
import ctypes
import time

# Windows API func
user32 = ctypes.windll.user32

# Constants for keypresses
Press_key = 0x0000
LetGo_key = 0x0002
ENTER = 0x0D    #enter
SPACE = 0x20     #space
Left_Window = 0x5B      # Left Windows key
Up_arrow = 0x26        # Up


# Move cursor
def move_cursor(x, y):
    user32.SetCursorPos(x, y)

# keyboard of user
def press_key(key_code):
    user32.keybd_event(key_code, 0, Press_key, 0)
    user32.keybd_event(key_code, 0, LetGo_key, 0)

# Type something
def type_text(text):
    for char in text:
        if char == ' ':
            press_key(SPACE)
        else:
            press_key(ord(char))  # ASCII 
        time.sleep(0.1)
# mouse click
def Click(x, y):
    move_cursor(x, y)
    user32.mouse_event(0x02, 0, 0, 0, 0) 
    user32.mouse_event(0x04, 0, 0, 0, 0)  

#press enter
def press_enter():
    user32.keybd_event(ENTER, 0, Press_key, 0)  
    user32.keybd_event(ENTER, 0, LetGo_key, 0)    
#go full screen = window key + up arrow
def fullscreen():
    ctypes.windll.user32.keybd_event(Left_Window, 0, Press_key, 0)  
    ctypes.windll.user32.keybd_event(Up_arrow, 0, Press_key, 0)  
    ctypes.windll.user32.keybd_event(Up_arrow, 0, LetGo_key, 0)    
    ctypes.windll.user32.keybd_event(Left_Window, 0, LetGo_key, 0) 

#open file appplic
time.sleep(3) 
Click(20, 1060)
time.sleep(1)
type_text("FILES")
press_enter()

#go fullscreen
time.sleep(1)
fullscreen()
move_cursor(1070,153)

#type txt or whatever file your looking for 
time.sleep(1)
Click(1079, 153)
type_text("TXT")
move_cursor(1070,200)

#double click top file
time.sleep(1)
Click(1079,200)
Click(1079,200)


