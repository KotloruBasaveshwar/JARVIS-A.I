import numpy as np
import pyaudiowpatch as pyaudio
from openwakeword.model import Model


# ==========================================================
# SETTINGS
# ==========================================================

RATE = 16000
CHUNK = 1280

WAKE_THRESHOLD = 0.22

MODEL_NAME = "hey_jarvis_v0.1"


# ==========================================================
# LOAD MODEL ONLY ONCE
# ==========================================================

_model = None


def get_model():

    global _model

    if _model is None:

        print("Loading wake-word model...")

        _model = Model(
            wakeword_models=[MODEL_NAME],
            inference_framework="onnx"
        )

        print("Wake-word model ready.")

    return _model


# ==========================================================
# WAKE WORD DETECTION
# ==========================================================

def wait_for_wake_word():

    print("Jarvis is running in background.")
    print("Say: Hey Jarvis")

    model = get_model()

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    try:

        while True:

            audio_data = stream.read(
                CHUNK,
                exception_on_overflow=False
            )

            audio_frame = np.frombuffer(
                audio_data,
                dtype=np.int16
            )

            predictions = model.predict(
                audio_frame
            )

            for wake_word, score in predictions.items():

                # Only show useful scores
                if score > 0.10:

                    print(
                        f"{wake_word}: {score:.3f}"
                    )

                if score >= WAKE_THRESHOLD:

                    print(
                        f"Wake word detected: "
                        f"{wake_word}"
                    )

                    return True

    except KeyboardInterrupt:

        print(
            "\nWake-word test stopped."
        )

        return False


    finally:

        try:
            stream.stop_stream()
        except Exception:
            pass

        try:
            stream.close()
        except Exception:
            pass

        try:
            audio.terminate()
        except Exception:
            pass

        # Give Windows audio device time to release
        import time
        time.sleep(0.3)

# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    wait_for_wake_word()