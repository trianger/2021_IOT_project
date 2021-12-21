from flask import Flask
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
    return """
    <p>Hello, Flask</p>
    <a href="/led/red/on">RED LED ON</a>
    <a href="/led/red/off">RED LED OFF</a>
    <a href="/led/green/on">GREEN LED ON</a>
    <a href="/led/green/off">GREEN LED OFF</a>
    """

@app.route("/led/<color>/<op>")
def led_op(op, color):
    if op == "on" and color == "red":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        return"""
        <p>GREEN LED ON</p>
        <a href="/">Go Home</a>
        """
    elif op=="off" and color == "red":
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        return"""
        <p>GREEN LED OFF</p>
        <a href="/">Go Home</a>
        """
    elif op == "on" and color == "green":
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
        return"""
        <p>GREEN LED ON</p>
        <a href="/">Go Home</a>
        """
    elif op=="off" and color == "green":
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        return"""
        <p>GREEN LED OFF</p>
        <a href="/">Go Home</a>
        """

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
