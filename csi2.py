import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import os
sensor = Adafruit_DHT.DHT22


while 1==1:
     # For DHT 11 Humidity + Temperature Sensor
     # sensor pin = 4 (GPIO)--> pin 7
     pinDHT22 = 4
     humidity, temperature = Adafruit_DHT.read_retry(sensor, pinDHT22)


     #print "Temperature: ",temperature," Celcius"
     #print "Humidity: ",humidity,"%"
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

	# Rain Drop Sensor
	rdSensor = 16
	GPIO.setup(rdSensor,GPIO.IN)

        # Gas Sensor
        gsSensor = 36
        GPIO.setup(gsSensor,GPIO.IN)


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

        req = 'curl -s -G "http://192.168.43.54:3000/slowData/?hum='+str(humidity)+'&temp='+str(temperature)+'&ultrasonic='+str(distance)+'&raindrop='+str(GPIO.input(rdSensor))+'&gas='+str(GPIO.input(gsSensor))+'&touch='+str(GPIO.input(touchSensor))+'"'


        # Send data to server
        os.system(req)

        # Display Touch sensor Value
        #print "Capacitive Touch Sensor:",GPIO.input(touchSensor)

        # Display Rain Drop Sensor Value
        #print "Rain Drop Sensor:",GPIO.input(rdSensor)

        # Display Light Sensor Value
        # print "Light Sensor:",GPIO.input(ltSensor) // too fast for 2s

        # Display Flame Sensor Value
        # print "Flame Sensor:",GPIO.input(flSensor) // too fast for 2s

        # Display Sound Sensing Sensor Value
        # print "Sound Sensing Sensor:",GPIO.input(soSensor) // too fast for 2s

        # Display Gas Sensor Value
        #print "Gas Sensor:",GPIO.input(gsSensor)

        # Display Hall Effect Sensor Value
        #  print "Hall Effect Sensor:",GPIO.input(heSensor) // too fast for 2s

     finally:
            GPIO.cleanup()
            time.sleep(2)
