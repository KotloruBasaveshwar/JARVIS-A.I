
import numpy as np
import pyaudiowpatch as pyaudio
from openwakeword.model import Model


RATE = 16000
CHUNK = 1280

# Start lower for testing.
# We can increase it later if there are false detections.
WAKE_THRESHOLD = 0.25


def wait_for_wake_word():

    print("Jarvis is running in background.")
    print("Say: Hey Jarvis")

    model = Model(
        wakeword_models=["hey_jarvis_v0.1"],
        inference_framework="onnx"
    )

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

            predictions = model.predict(audio_frame)

            for wake_word, score in predictions.items():

                # Show score so we can diagnose detection.
                if score > 0.05:
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

        print("\nWake-word test stopped.")

        return False

    finally:

        stream.stop_stream()
        stream.close()
        audio.terminate()


if __name__ == "__main__":

    wait_for_wake_word()
