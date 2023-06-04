import tkinter as tk
from tkinter import scrolledtext
from pynput.keyboard import Key, Listener
import clipboard

import time
import datetime as dt
import pyperclip

global c_counter
c_counter = 0
global last_pressed_keys
last_pressed_keys = []
global last_copied_text
last_copied_text = ""

def limit_entry():
    global last_pressed_keys
    global c_counter
    global last_copied_text
    time.sleep(0.1)
    
    
    looking_for_strg = r"Key.ctrl_l"
    looking_for_c = r"'\x03'"
    print(last_pressed_keys)
    last_copied_text = clipboard.paste()
    if len(last_pressed_keys) == 3:
        last_pressed_keys = []
        
    if len(last_pressed_keys) == 1:
        if looking_for_strg in last_pressed_keys:
            return
        else:
            last_pressed_keys = []
            
    if len(last_pressed_keys) == 2:
        last_copied_text = clipboard.paste()
        clipboard_data = clipboard.paste()
        timestamp = dt.datetime.now()
        formatted_time = str(timestamp).split()[1]
        clipboard_data_string = clipboard.paste()

        text_field6.insert("1.0", str(formatted_time) + "  " +f"{clipboard_data_string[0:35]}" + "\n")
        
        if looking_for_strg in last_pressed_keys[-2] and looking_for_c in last_pressed_keys[-1]:
            
            old_clipboard_text = text_list[c_counter-1].get("1.0", "end-1c")
            print(last_copied_text)
            print(old_clipboard_text)
            
            if clipboard_data == old_clipboard_text:
                last_pressed_keys = []
                print("lol")
                return
            
            text_list[c_counter].replace("1.0",tk.END, clipboard_data)
            last_pressed_keys = []
            
            print(f"old_cur:{c_counter}")
            if c_counter == 3:
                c_counter = 0
            elif c_counter < 3:
                c_counter += 1  
            print(f"new_cur:{c_counter}")
        last_pressed_keys = []
    
    if len(last_pressed_keys) == 3:
        last_pressed_keys = []

def on_press(key):
    global last_pressed_keys
    
    key_char = str(key)
    last_pressed_keys.append(key_char)
    limit_entry()
    text_field5.replace("1.0", "end-1c", key)
    

root = tk.Tk()
root.title("Copy and Paste")
screen_height = root.winfo_screenheight()
window_height = screen_height
root.geometry(f"600x{window_height}")
root.attributes("-topmost", True)

# Create scrollable text fields
text_field1 = scrolledtext.ScrolledText(root, height=10, width=60)
text_field2 = scrolledtext.ScrolledText(root, height=10, width=60)
text_field3 = scrolledtext.ScrolledText(root, height=10, width=60)
text_field4 = scrolledtext.ScrolledText(root, height=10, width=60)
text_field5 = tk.Text(root, height=10, width=60)
text_field6 = scrolledtext.ScrolledText(root, height=50, width=60)
text_list = [text_field1, text_field2, text_field3, text_field4]


def button1_click(button_num):
    print(button_num)
    pyperclip.copy(text_list[button_num].get("1.0", "end-1c"))


def button_clear_click(button_num):
    print(button_num)
    text_list[button_num].replace("1.0", "end-1c", "")

 
##
text1_button_frame = tk.Frame(root)
text1_button_frame.grid(row=0, column=1, padx=10, pady=10)
button1 = tk.Button(text1_button_frame, text="Copy", command=lambda: button1_click(0))
button1_2 = tk.Button(text1_button_frame, text="Clear",command=lambda: button_clear_click(0))
button1_3 = tk.Button(text1_button_frame, text="Button 1_3")
button1.pack(side=tk.TOP)
button1_3.pack(side=tk.BOTTOM)
button1_2.pack(side=tk.BOTTOM)

##
text2_button_frame = tk.Frame(root)
text2_button_frame.grid(row=1, column=1, padx=10, pady=10)
button2 = tk.Button(text2_button_frame, text="Copy", command=lambda: button1_click(1))
button2_2 = tk.Button(text2_button_frame, text="Button 1_2")
button2.pack(side=tk.TOP)
button2_2.pack(side=tk.BOTTOM)
##
text3_button_frame = tk.Frame(root)
text3_button_frame.grid(row=2, column=1, padx=10, pady=10)
button3 = tk.Button(text3_button_frame, text="Copy",command=lambda: button1_click(2))
button3_2 = tk.Button(text3_button_frame, text="Button 3_2")
button3.pack(side=tk.TOP)
button3_2.pack(side=tk.BOTTOM)
##
text4_button_frame = tk.Frame(root)
text4_button_frame.grid(row=3, column=1, padx=10, pady=10)
button4 = tk.Button(text4_button_frame, text="Copy",command=lambda: button1_click(3))
button4_2 = tk.Button(text4_button_frame, text="Button 3_2")
button4.pack(side=tk.TOP)
button4_2.pack(side=tk.BOTTOM)
##

text_field1.grid(row=0, column=0)
text_field2.grid(row=1, column=0)
text_field3.grid(row=2, column=0)
text_field4.grid(row=3, column=0)
text_field5.grid(row=4, column=0)
text_field6.grid(row=5, column=0)

with Listener(on_press=on_press) as listener:
    root.mainloop()
    listener.stop()
