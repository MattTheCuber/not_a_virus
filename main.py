import os
import sys
import signal
import time
import colorama
import keyboard
import ctypes
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk
import random

original_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
import pygame
sys.stdout.close()
sys.stdout = original_stdout

def signal_handler(sig, frame):
    pass

def resource_path(relative_path):
    """ Get absolute path to resource, for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def fake_delete():
    send_messages()
    time.sleep(1)

    home = os.path.expanduser("~")
    directories = ["Documents", "Downloads", "Desktop", "Pictures", "Videos"]

    for dir in directories:
        delete_dir(os.path.join(home, dir))

    delete_dir("C:\\Windows\\System32")

    print("\nAll files deleted. System will shut down now.")
    time.sleep(0.5)

    print("\nGet pranked, nerd")

    max_volume()
    play_mp3(resource_path('res/rroll.mp3'))

    open_fullscreen_image(resource_path('res/Bsos.png'))

def send_messages():
    prank_messages = [
        "Initializing virus...",
        "Establishing connection to remote server...",
        "Transmitting sensitive data...",
        "Transmitting account data and passwords data...",
        "Compromising system security...",
        "Uploading user data...",
        "Disabling security protocols...",
        "Initiating virus spread to network...",
        "Deleting all backups...",
        "Overwriting critical system files...",
        "\nInitiating system wipe...",
    ]

    for message in prank_messages:
        print(message)
        time.sleep(random.uniform(0.2, 0.8))

    time.sleep(0.5)
    
def delete_dir(dir):
    count = 0
    stop = False

    for root, dirs, files in os.walk(dir):
        if stop:
            break
        for file in files:
            if count > 25000:
                stop = True
                break
            print(f"\033[91mDeleting\033[0m {os.path.join(root, file)}...")
            count += 1

def max_volume():
    try:
        user32 = ctypes.WinDLL("user32")

        for _ in range(50):
            user32.keybd_event(0xAF, 0, 0, 0)
            user32.keybd_event(0xAF, 0, 2, 0)
    except:
        pass

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
def open_fullscreen_image(image_path):
    root = Tk()
    root.attributes('-fullscreen', True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    image = Image.open(image_path)
    image = image.resize((screen_width, screen_height), Image.NEAREST)
    photo_image = ImageTk.PhotoImage(image)

    canvas = Canvas(root, width=screen_width, height=screen_height, bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor=NW, image=photo_image)

    root.focus_force()
    root.lift()
    root.mainloop()

if __name__ == "__main__":
    try:
        colorama.init()
    except:
        pass    
    try:
        keyboard.press('f11')
    except:
        pass
    try:
        signal.signal(signal.SIGINT, signal_handler)
    except:
        pass
    try:
        fake_delete()
    except:
        pass
