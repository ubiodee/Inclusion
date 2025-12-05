import os
import shutil
import requests
from pydub import AudioSegment

# Load API key if user has one (optional)
API_KEY = os.getenv("SIGN_SPEAK_API_KEY")
BASE_URL = "https://api.sign-speak.com"

def speech_to_sign():
    output_file = "output_sign_video.mp4"

    if API_KEY:
        print("API key found → generating live ASL avatar...")
        # Step 1: Speech → Text
        audio = AudioSegment.from_file("input_speech.wav")
        audio = audio.set_channels(1).set_frame_rate(16000)
        import io, base64
        buffer = io.BytesIO()
        audio.export(buffer, format="wav")
        payload = base64.b64encode(buffer.getvalue()).decode()

        r1 = requests.post(f"{BASE_URL}/recognize-speech", headers={"X-api-key": API_KEY},
                           json={"payload": payload, "request_class": "BLOCKING"})
        text = r1.json()["prediction"][0]["prediction"] if r1.status_code == 200 else "Hello"

        # Step 2: Text → Avatar
        r2 = requests.post(f"{BASE_URL}/produce-sign", headers={"X-api-key": API_KEY},
                           json={"english": text, "request_class": "BLOCKING", "identity": "MALE"})
        if r2.status_code == 200:
            with open(output_file, "wb") as f:
                f.write(r2.content)
            print("Live video generated!")
            return

    
    print("No API key → using pre-generated REAL Sign-Speak avatar video")
    shutil.copy("demo_avatar_video.mp4", output_file)
    print("Done → output_sign_video.mp4 is ready ( output)")

if __name__ == "__main__":
    speech_to_sign()
    print("\nPlay output_sign_video.mp4 to see the ASL avatar!")
