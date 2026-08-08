import pyttsx3
import speech_recognition as sr


# ==========================================
# VOICE OUTPUT
# ==========================================

def speak(text):

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    if voices:
        engine.setProperty("voice", voices[0].id)

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    print("Jarvis:", text)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


# ==========================================
# SPEECH RECOGNITION
# ==========================================

recognizer = sr.Recognizer()

recognizer.pause_threshold = 1.0
recognizer.non_speaking_duration = 0.4
recognizer.dynamic_energy_threshold = True

LISTEN_TIMEOUT = 5
PHRASE_TIME_LIMIT = 8


# ==========================================
# LISTEN
# ==========================================

def listen():

    try:

        with sr.Microphone() as source:

            print("Listening...")

            audio = recognizer.listen(
                source,
                timeout=LISTEN_TIMEOUT,
                phrase_time_limit=PHRASE_TIME_LIMIT
            )

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        command = command.lower().strip()

        print("You said:", command)
        print("DEBUG:", command)

        return command

    except sr.WaitTimeoutError:

        return ""

    except sr.UnknownValueError:

        print("Sorry, I didn't understand.")

        return ""

    except sr.RequestError:

        print("Speech recognition service is unavailable.")

        speak(
            "Speech recognition is currently unavailable."
        )

        return ""

    except Exception as e:

        print("Voice error:", e)

        return ""


# ==========================================
# COMPATIBILITY
# ==========================================

def take_command():

    return listen()


# ==========================================
# WAKE WORD
# ==========================================

def is_wake_word(command):

    wake_words = [
        "jarvis",
        "hey jarvis",
        "okay jarvis",
        "ok jarvis"
    ]

    command = command.lower().strip()

    return any(
        word in command
        for word in wake_words
    )


# ==========================================
# SLEEP COMMAND
# ==========================================

def is_sleep_command(command):

    sleep_words = [
        "thank you",
        "thanks jarvis",
        "thank you jarvis",
        "go to sleep",
        "sleep jarvis"
    ]

    command = command.lower().strip()

    return any(
        word in command
        for word in sleep_words
    )


# ==========================================
# STOP COMMAND
# ==========================================

def is_stop_command(command):

    stop_words = [
        "stop jarvis",
        "exit jarvis",
        "shutdown jarvis"
    ]

    command = command.lower().strip()

    return any(
        word in command
        for word in stop_words
    )

