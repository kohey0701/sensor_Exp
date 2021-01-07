# 焦電型赤外線センサ(人感センサ)　動作確認

import RPi.GPIO as GPIO
import time

GPIO.cleanup()

led_pin = 27
motion_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_pin,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

def main():
    while True:
        print(GPIO.input(motion_pin))
        time.sleep(0.1)
        if(GPIO.input(motion_pin) == 1):
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)

try:
    main()
except KeyboardInterrupt:
    print("停止処理を受け付けました")

GPIO.cleanup()

# 人感センサーがこちらの動きを検知すると１を返す。