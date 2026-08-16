from voice import speak, take_command
from commands import execute_command
from utils import preprocess_command
from wake_word import wait_for_wake_word

from jarvis_gui import JarvisGUI
from gui_bridge import JarvisGUIBridge

import tkinter as tk
import threading
import sys


# ======================================================
# JARVIS ENGINE
# ======================================================

def jarvis_engine(bridge, stop_event):

    print("Jarvis is starting...")

    speak(
        "Hello Boss. I am ready."
    )

    bridge.ready()


    while not stop_event.is_set():

        # ==========================================
        # BACKGROUND MODE
        # ==========================================

        print(
            "\nJarvis is running in background."
        )

        print(
            "Say 'Hey Jarvis' to wake me."
        )

        wait_for_wake_word()


        if stop_event.is_set():

            break


        # ==========================================
        # ACTIVE MODE
        # ==========================================

        bridge.speaking(
            "Yes Boss, I'm listening."
        )

        speak(
            "Yes Boss, I'm listening."
        )

        bridge.ready()


        while not stop_event.is_set():

            # ======================================
            # LISTEN
            # ======================================

            bridge.listening()

            command = take_command()


            if not command:

                bridge.ready()

                continue


            # ======================================
            # PROCESS
            # ======================================

            command = preprocess_command(
                command
            )

            print(
                "DEBUG:",
                command
            )

            bridge.processing(
                command
            )


            # ======================================
            # STOP COMPLETELY
            # ======================================

            if (
                "stop jarvis" in command
                or "exit jarvis" in command
                or "shutdown jarvis" in command
            ):

                bridge.speaking(
                    "Goodbye Bashu. Have a nice day."
                )

                speak(
                    "Goodbye Bashu. Have a nice day."
                )

                stop_event.set()

                bridge.shutdown()

                return


            # ======================================
            # RETURN TO BACKGROUND
            # ======================================

            if (
                "thank you" in command
                or "thank u" in command
                or "thanks" in command
                or "thank" in command
                or "okay thanks" in command
                or "ok thanks" in command
                or "that's all" in command
                or "thats all" in command
                or "done" in command
                or "go to sleep" in command
                or "sleep jarvis" in command
            ):

                bridge.speaking(
                    "You're welcome, Boss. "
                    "I'll wait for you."
                )

                speak(
                    "You're welcome, Boss. "
                    "I'll wait for you."
                )

                bridge.ready()

                break


            # ======================================
            # EXISTING JARVIS COMMANDS
            # ======================================

            execute_command(
                command,
                None
            )

            bridge.ready()


# ======================================================
# START APPLICATION
# ======================================================
def main():

    root = tk.Tk()

    # Create GUI first
    gui = JarvisGUI(root)

    bridge = JarvisGUIBridge(gui)

    stop_event = threading.Event()


    # ==========================================
    # START JARVIS AFTER GUI IS VISIBLE
    # ==========================================

    def start_jarvis():

        jarvis_thread = threading.Thread(
            target=jarvis_engine,
            args=(
                bridge,
                stop_event
            ),
            daemon=True
        )

        jarvis_thread.start()


    # ==========================================
    # SHOW GUI FIRST
    # ==========================================

    root.after(100, start_jarvis)


    # ==========================================
    # FULLSCREEN PRESENTATION
    # ==========================================

    root.attributes("-fullscreen", True)

    root.bind("<Escape>", lambda event: root.destroy())
    

    # ==========================================
    # START GUI
    # ==========================================

    root.mainloop()

# ======================================================
# RUN
# ======================================================

if __name__ == "__main__":

    main()