import spidev
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)          # GPIO.BCM or GPIO.BOARD
GPIO.setup(12, GPIO.OUT)  #GPIO.OUT OR GPIO.IN

# spi 인스턴트 생성
spi = spidev.SpiDev()

#SPI 통신시작
spi.open(0, 0) # bus: 0, dev: 0

#SPI 통신속도 설정
spi.max_speed_hz = 1000000

# 채널에서 SPI 데이터 읽기 (0~1023)
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_2: channel config(channel 0) 0000 1000(=8)
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    print(ret)
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        Idr_value = analog_read(0)
        if Idr_value<512:
            GPIO.output(12, GPIO.HIGH)
        else:
            GPIO.output(12, GPIO.LOW)
        #voltage = reading * 3.3 / 1023
        print("LDR Value: %d" % (Idr_value))
        time.sleep(0.5)
finally:
    spi.close()
    GPIO.cleanup()
    