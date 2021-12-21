from flask import Flask, render_template
import RPi.GPIO as GPIO

RED_LED_PIN = 4
GREEN_LED_PIN = 3

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

@app.route("/")
def hello():
    #return "<p>Hello, Flask!</p>"
    return render_template('led.html')

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if op == "on" and color == "red":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        print("11")
        return "RED LED ON"
    elif op=="off" and color == "red":
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        print("22")
        return "RED LED OFF"
    if op == "on" and color == "green":
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
        print(333)
        return "GREEN LED ON"
    elif op=="off" and color == "green":
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        return "GREEN LED OFF"
    else :
        return "Error"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
    