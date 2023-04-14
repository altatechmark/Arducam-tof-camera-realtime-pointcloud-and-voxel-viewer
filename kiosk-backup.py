# import subprocess
# import threading
# from app import app

# def run_flask():
    # app.run(port=5000, host="0.0.0.0")

# if __name__ == "__main__":
    # threading.Thread(target=run_flask).start()
    # subprocess.run(["chromium-browser", "--kiosk", "--disable-restore-session-state", "--noerrdialogs", "--disk-cache-dir=/dev/null", "http://localhost:5000"])


import subprocess
import threading
import uinput
import RPi.GPIO as GPIO
import time

from app import app

button1 = 23
button2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def run_flask():
    app.run(port=5000, host="0.0.0.0")

# def button_callback(channel):
    # with uinput.Device([uinput.KEY_F1, uinput.KEY_F2]) as device:
        # if channel == button1:
            # device.emit_click(uinput.KEY_F1)
        # elif channel == button2:
            # device.emit_click(uinput.KEY_F2)
# def button_callback(channel):
    # print("Button pressed")
    # try:
        # with uinput.Device([uinput.KEY_F1, uinput.KEY_F2]) as device:
            # if channel == button1_pin:
                # print("Sending KEY_F1")
                # device.emit_click(uinput.KEY_F1)
            # elif channel == button2_pin:
                # print("Sending KEY_F2")
                # device.emit_click(uinput.KEY_F2)
    # except Exception as e:
        # print("Error:", e)
        
def button_callback(channel):
    print("Button pressed")
    try:
        with uinput.Device([uinput.KEY_F1, uinput.KEY_F2]) as device:
            if channel == button1:  # Change this line
                print("Sending KEY_F1")
                device.emit_click(uinput.KEY_F1)
            elif channel == button2:  # Change this line
                print("Sending KEY_F2")
                device.emit_click(uinput.KEY_F2)
    except Exception as e:
        print("Error:", e)


GPIO.add_event_detect(button1, GPIO.FALLING, callback=button_callback, bouncetime=300)
GPIO.add_event_detect(button2, GPIO.FALLING, callback=button_callback, bouncetime=300)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    time.sleep(2)  # Give Flask some time to start

    # Configure the Chromium browser to navigate pages using F1 and F2 keys
    kiosk_command = [
        "chromium-browser",
        "--kiosk",
        "--no-sandbox",
        "--disable-restore-session-state",
        "--noerrdialogs",
        "--disk-cache-dir=/dev/null",
        "--app=http://localhost:5000/voxel",
        "--extensions-on-chrome-urls",
        "--test-type",
        "--load-extension=/home/pi/3dview/button_navigation_extension/manifest.json"
    ]

    subprocess.run(kiosk_command)
