from voice import speak
import webbrowser
import datetime
import wikipedia
import psutil
import subprocess
import os
import shutil
from pathlib import Path
import sys
import random
import pyautogui
import requests
import pyperclip
from pyautogui import press
import ctypes
import pandas as pd
from data_analysis import *

pending_action = None
apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe",
    "cmd": "cmd.exe"
}

folders = {
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents")
}

websites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chatgpt.com"
}

   
def execute_command(command,intent):
    global pending_action
    if "hello jarvis" in command:
        speak("Hello Bashu! How can I help you?")

    elif "what is the time" in command or "tell me the time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "who is" in command:
        person = command.replace("who is", "").strip()

        speak(f"Searching Wikipedia for {person}")

        try:
            info = wikipedia.summary(person, sentences=2)
            print(info)
            speak(info)

        except:
            speak("Sorry, I couldn't find information.")

    elif "battery percentage" in command:

        battery = psutil.sensors_battery()
        percent = battery.percent

        if percent <= 20:
            speak(f"Warning! Your battery is only {percent} percent. Please charge your laptop.")
        else:
            speak(f"Your battery is {percent} percent.")

    elif "is my laptop charging" in command or "charging status" in command:

        battery = psutil.sensors_battery()

        if battery.power_plugged:
            speak("Yes, your laptop is charging.")
        else:
            speak("No, your laptop is running on battery.")

    elif "create folder" in command:

        speak("Creating folder")

        folder = Path.home() / "Documents" / "New Folder"

        folder.mkdir(exist_ok=True)

        speak("Folder created successfully.")

    elif "delete folder" in command:

        folder = Path.home() / "Documents" / "New Folder"

        if folder.exists():
            shutil.rmtree(folder)
            speak("Folder deleted successfully.")
        else:
            speak("Folder does not exist.")
    elif "play music" in command:

        music_folder = os.path.join(os.path.expanduser("~"), "Music")

        songs = os.listdir(music_folder)

        if songs:
            song = random.choice(songs)
            speak("Playing music")
            os.startfile(os.path.join(music_folder, song))
        else:
            speak("No music found.")
    elif "take screenshot" in command:

        speak("Taking screenshot")

        screenshot = pyautogui.screenshot()

        screenshot.save("screenshot.png")

        speak("Screenshot saved successfully.")

    elif "what is today's date" in command or "tell me today's date" in command:

        now = datetime.datetime.now()

        date = now.strftime("%d %B %Y")
        day = now.strftime("%A")

        speak(f"Today is {day}, {date}")
    elif "create text file" in command:

        file = Path.home() / "Documents" / "Notes.txt"
        print(file)
        with open(file, "w") as f:
            f.write("This file was created by Jarvis.")

        speak("Text file created successfully.")   
    elif "read text file" in command:

        file = Path.home() / "Documents" / "Notes.txt"

        try:
            with open(file, "r") as f:
                content = f.read()

            speak(content)

        except FileNotFoundError:
            speak("The text file does not exist.")  
    elif "open text file" in command:

        file = Path.home() / "Documents" / "Notes.txt"

        if file.exists():
            speak("Opening text file.")
            os.startfile(file)
        else:
            speak("Text file does not exist.")  

    elif "rename text file" in command:

        old_file = Path.home() / "Documents" / "Notes.txt"
        new_file = Path.home() / "Documents" / "MyNotes.txt"

        if old_file.exists():
            old_file.rename(new_file)
            speak("File renamed successfully.")
        else:
            speak("Text file does not exist.")     

    elif "delete text file" in command:

        file = Path.home() / "Documents" / "MyNotes.txt"

        if file.exists():
            file.unlink()
            speak("Text file deleted successfully.")
        else:
            speak("Text file does not exist.")   
    elif command.startswith("search "):
    
            speak("Opening Windows Search.")
    
            pyautogui.press("win")
    elif "open task manager" in command:
    
            speak("Opening Task Manager.")
    
            subprocess.Popen("taskmgr.exe")     
    elif "open file explorer" in command:
    
            speak("Opening File Explorer.")
    
            subprocess.Popen("explorer.exe") 
    elif "open camera" in command:
    
            speak("Opening Camera.")
    
            os.system("start microsoft.windows.camera:")                      
    elif "open" in command:

        item = command.replace("open", "").strip()

        # Open Applications
        if item in apps:
            speak(f"Opening {item}")
            subprocess.Popen(apps[item])

        # Open Folders
        elif item in folders:
            speak(f"Opening {item}")
            os.startfile(folders[item])

        # Open Websites
        elif item in websites:
            speak(f"Opening {item}")
            webbrowser.open(websites[item])

        else:
            speak("Sorry, I don't know that application, folder or website.")

    
    elif "stop jarvis" in command or "exit jarvis" in command:

        speak("Goodbye Bashu. Have a nice day.")
        sys.exit()    
    
    elif "read clipboard" in command:

        text = pyperclip.paste()

        if text:
            speak(text)
        else:
            speak("Clipboard is empty.")

    elif command.startswith("type"):

        text = command.replace("type", "", 1).strip()

        if text:
            speak("Typing now.")
            pyautogui.write(text, interval=0.05)

        else:
            speak("Please tell me what to type.")

    elif "copy selected text" in command:

        speak("Copying selected text.")

        pyautogui.hotkey("ctrl", "c")
    elif "press enter" in command:

        speak("Pressing Enter.")

        pyautogui.press("enter")
    elif command.startswith("send"):

        text = command.replace("send", "", 1).strip()

        if text:
            speak("Sending message.")

            pyautogui.write(text, interval=0.05)
            pyautogui.press("enter")

        else:
            speak("Please tell me what to send.")    

    elif "volume up" in command:

        speak("Increasing volume.")

        for i in range(5):
            press("volumeup")


    elif "volume down" in command:

        speak("Decreasing volume.")

        for i in range(5):
            press("volumedown")


    elif "mute volume" in command or "mute" in command:

        speak("Muting volume.")

        press("volumemute")      
    elif "lock my computer" in command or "lock computer" in command:

        speak("Locking your computer.")

        ctypes.windll.user32.LockWorkStation()     
    elif "restart computer" in command:

        pending_action = "restart"

        speak("Are you sure? Say confrim to restart or cancel to cancel.")
    elif "shutdown computer" in command:

        pending_action = "shutdown"

        speak("Are you sure? Say confrim to shut down or cancel to cancel.")
    elif "comfrim" in command:

        if pending_action == "restart":

            speak("Restarting computer.")

            os.system("shutdown /r /t 0")

        elif pending_action == "shutdown":

            speak("Shutting down computer.")

            os.system("shutdown /s /t 0")

        pending_action = None
    elif  "cancel" in command:

        if pending_action:

            speak("Operation cancelled.")

            pending_action = None
    elif "show desktop" in command:

        speak("Showing desktop.")

        pyautogui.hotkey("win", "d")
    elif "switch window" in command or "switch application" in command:

        speak("Switching window.")

        pyautogui.hotkey("alt", "tab")   

    elif "analyze" in command or "analyse" in command:
        analyze_dataset()

    elif "average" in command or "mean" in command:
        statistics(command)

    elif "maximum" in command or "highest" in command or "max" in command:
        statistics(command)

    elif "minimum" in command or "lowest" in command or "min" in command:
        statistics(command)
    elif "bar chart" in command:
        create_chart("bar")

    elif "pie chart" in command:
        create_chart("pie")

    elif "line chart" in command:
        create_chart("line")

    elif "histogram" in command:
        create_chart("histogram")
    elif "students above" in command:
        students_above(20)

    elif "students below" in command:
        students_below(20)

    elif "show" in command and "student" in command:
        filter_course(command)

    elif "sort" in command:
        sort_dataset(command)

    elif "generate student report" in command or "generate report" in command:
        generate_report()

    elif "clean" in command and (
    "dataset" in command
    or "data set" in command
):
     clean_dataset()

    elif (
    "current dataset" in command
    or "current data set" in command
):
     current_dataset()
    elif "read excel" in command or "read excel file" in command:
        read_excel_file()

    elif "write excel" in command or "create excel" in command:
        write_excel_file()

    elif (
        "export report to excel" in command
        or "export report" in command
    ):
        export_report_to_excel()
    elif "load" in command:
     load_new_dataset(command)
    elif (
        "available datasets" in command
        or "available dataset" in command
        or "available data sets" in command
        or "available data set" in command
    ):
        available_datasets()
    elif (
        "how many" in command
        or "average" in command
        or "mean" in command
        or "highest" in command
        or "maximum" in command
        or "lowest" in command
        or "minimum" in command
        or "what columns" in command
        or "which columns" in command
        or "column names" in command
        or "unique values" in command
        or "different values" in command
        or "courses" in command
    ):
        dataset_question(command)
    else:
        speak("Sorry, I don't know that command yet.")
   