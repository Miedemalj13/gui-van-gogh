from tkinter import *
import RPi.GPIO as GPIO
import time
import math
from gpiozero import LED

GPIO.setmode(GPIO.BCM)

led0 = LED(7)
led1 = LED(8)
led2 = LED(25)
led3 = LED(24)
led4 = LED(23)
led5 = LED(18)
led6 = LED(15)
led7 = LED(14)

leds = [led7, led6, led5, led4, led3, led2, led1, led0]

def toggle():
    try:
        led0.on()
        time.sleep(0.5)
        led1.on()
        time.sleep(0.5)

        led0.off()
        time.sleep(0.1)
        led2.on()
        time.sleep(0.5)

        led1.off()
        time.sleep(0.1)
        led3.on()
        time.sleep(0.5)

        led2.off()
        time.sleep(0.1)
        led4.on()
        time.sleep(0.5)

        led3.off()
        time.sleep(0.1)
        led5.on()
        time.sleep(0.5)

        led4.off()
        time.sleep(0.1)
        led5.off()
        time.sleep(0.1)

        led6.on()
        time.sleep(0.5)
        led7.on()
        time.sleep(0.5)

        led6.off()
        time.sleep(0.1)
        led7.off()
        time.sleep(0.1)

        toggleButton["text"] = "Turn LEDs on"

    except:
        toggleButton["text"] = "Turn LEDs off"

window=Tk()
window.title("Toggler")

toggleButton = Button(window, text = "Turn LEDs on", command = toggle)
toggleButton.pack(side=LEFT)

quitButton = Button(window, text="Quit", command=exit)
quitButton.pack(side=LEFT)

window.mainloop()
