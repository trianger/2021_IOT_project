from flask import Flask, render_template
import RPi.GPIO as GPIO

RED_LED_PIN = 4
#GREEN_LED_PIN = 3

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
#GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

@app.route("/")
def hello():
    #return "<p>Hello, Flask!</p>"
    return render_template('led.html')

@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif op=="off":
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        return "LED OFF"
    else :
        return "Error"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
