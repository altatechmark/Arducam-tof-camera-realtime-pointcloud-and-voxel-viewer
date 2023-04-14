import subprocess
import threading
import uinput
import RPi.GPIO as GPIO
import time
import os
from app import app

button1 = 23
button2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def run_flask():
    app.run(port=5000, host="0.0.0.0")

def run_viz2():
    os.system("python viz2.py")

        
def button_callback(channel):
    print("Button pressed")
    try:
        if channel == button1:
            print("Navigating to http://localhost:5000")
            start_chromium("http://localhost:5000")
        elif channel == button2:
            print("Navigating to http://localhost:5000/voxel")
            start_chromium("http://localhost:5000/voxel")
    except Exception as e:
        print("Error:", e)
        
import os
import signal

def start_chromium(url):
    # Kill any existing chromium-browser processes
    os.system("sudo pkill -f chromium-browser")

    # Start a new chromium-browser process with the given URL
    kiosk_command = [
        "chromium-browser",
        "--kiosk",
        "--no-sandbox",
        "--disable-restore-session-state",
        "--noerrdialogs",
        "--disk-cache-dir=/dev/null",
        f"--app={url}",
        "--extensions-on-chrome-urls",
        "--test-type",
        "--load-extension=/home/pi/3dview/button_navigation_extension/manifest.json"
    ]

    subprocess.Popen(kiosk_command, preexec_fn=os.setsid)


GPIO.add_event_detect(button1, GPIO.FALLING, callback=button_callback, bouncetime=300)
GPIO.add_event_detect(button2, GPIO.FALLING, callback=button_callback, bouncetime=300)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    time.sleep(2)  # Give Flask some time to start

    threading.Thread(target=run_viz2).start()
    time.sleep(10)
    start_chromium("http://localhost:5000")
