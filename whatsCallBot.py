import pyautogui
import time
import os
from dotenv import load_dotenv

# Load data from the .env file
load_dotenv()

# Open WhatsApp
def open_whatsapp():
    os.system("start whatsapp:")  # Command to open WhatsApp
    time.sleep(10)  # Wait for WhatsApp to load (10 seconds)

# Press Ctrl + F
def press_ctrl_f():
    pyautogui.hotkey('ctrl', 'f')  # Press Ctrl + F to focus on the search bar
    time.sleep(1)

# Press Ctrl + A
def press_ctrl_a():
    pyautogui.hotkey('ctrl', 'a')  # Press Ctrl + A to select all text
    time.sleep(1)

# Press Backspace
def press_backspace():
    pyautogui.press('backspace')  # Press Backspace to delete text
    time.sleep(1)

# Type the user's name
def type_user_name(user_name):
    pyautogui.write(user_name, interval=0.1)  # Type the user's name
    time.sleep(2)

# Press down arrow to select the user
def press_down_arrow():
    pyautogui.press('down')  # Press the down arrow key
    time.sleep(1)

# Select the user
def select_user():
    pyautogui.press("enter")  # Press Enter to select the user
    time.sleep(1)

# Click the call button
def click_call_button():
    pyautogui.click(1845, 70)  # Click on the call button (coordinates)
    time.sleep(5)  # Wait for the call to start

# Close WhatsApp
def close_whatsapp():
    pyautogui.hotkey('alt', 'f4')  # Press Alt + F to close WhatsApp
    time.sleep(2)  # Wait for the app to close

if __name__ == "__main__":
    user_name = os.getenv("WHATSAPP_USER")  # Get the user's name from .env
    interval_seconds = int(os.getenv("INTERVAL", 165))  # Get the interval from .env (default to 165 seconds if not found)

    call_count = 0  # Initialize call counter

    while True:
        call_count += 1  # Increment the call count

        open_whatsapp()  # WhatsApp will open
        press_ctrl_f()  # Press Ctrl + F to focus on the search bar
        press_ctrl_a()  # Press Ctrl + A to select all text
        press_backspace()  # Press Backspace to delete the text
        type_user_name(user_name)  # Type the user's name
        press_down_arrow()  # Press the down arrow key
        select_user()  # Select the user
        click_call_button()  # Click the call button
        print(f"Call {call_count} has been made to {user_name}. Wait for {interval_seconds // 60} minutes and {interval_seconds % 60} seconds.")
        
        # close_whatsapp()  # WhatsApp will close after the call
        time.sleep(2)  # Wait for the app to close
        
        time.sleep(interval_seconds)  # Wait for the next call (based on the interval from .env)
