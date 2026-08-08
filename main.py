from voice import speak, take_command
from commands import execute_command
from utils import preprocess_command
from wake_word import wait_for_wake_word

import sys


print("Jarvis is starting...")

speak("Hello Boss. I am ready.")


while True:

    # ==========================================
    # BACKGROUND MODE
    # ==========================================

    print("\nJarvis is running in background.")
    print("Say 'Hey Jarvis' to wake me.")

    wait_for_wake_word()


    # ==========================================
    # ACTIVE MODE
    # ==========================================

    speak("Yes Boss, I'm listening.")

    while True:

        command = take_command()

        if not command:
            continue

        command = preprocess_command(command)

        print("DEBUG:", command)


        # ======================================
        # STOP COMPLETELY
        # ======================================

        if (
            "stop jarvis" in command
            or "exit jarvis" in command
            or "shutdown jarvis" in command
        ):

            speak("Goodbye Bashu. Have a nice day.")

            sys.exit()


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

            speak(
                "You're welcome, Boss. "
                "I'll wait for you."
            )

            break


        # ======================================
        # EXISTING JARVIS COMMANDS
        # ======================================

        execute_command(command, None)