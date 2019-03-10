import Adafruit_DHT
import RPi.GPIO as GPIO
import time
sensor = Adafruit_DHT.DHT22


while 1==1:
     # For DHT 11 Humidity + Temperature Sensor
     # sensor pin = 4 (GPIO)--> pin 7
     pinDHT22 = 4
     humidity, temperature = Adafruit_DHT.read_retry(sensor, pinDHT22)


     print "Temperature: ",temperature," Celcius"
     print "Humidity: ",humidity,"%"
     try:
        GPIO.setmode(GPIO.BOARD)

        # for Ultrasonic sensor
        # trigger = pin 11 (number NOT GPIO)
        # echo = pin 13 (number NOT GPIO)
        PIN_TRIGGER = 11
        PIN_ECHO = 13
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        # Capacitive Touch sensor
        touchSensor = 15
        GPIO.setup(touchSensor,GPIO.IN)

        # Calculate and display Distance, using ultrasonic sensor
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print "Ultrasonic Distance:",distance,"cm"


        # Display Touch sensor Value
        print "Capacitive Touch Sensor:",GPIO.input(touchSensor)



     finally:
            GPIO.cleanup()
            time.sleep(2)
