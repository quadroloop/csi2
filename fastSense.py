import RPi.GPIO as GPIO
import os
import time

while 1==1:

      try:

         GPIO.setmode(GPIO.BOARD)

	# Light Sensor
	 ltSensor = 18
	 GPIO.setup(ltSensor,GPIO.IN)

	# Flame Sensor
	 flSensor = 22
	 GPIO.setup(flSensor,GPIO.IN)

	# Sound Sensing Sensor
	 soSensor = 32
	 GPIO.setup(soSensor,GPIO.IN)

	# Hall Effect Sensor
	 heSensor = 38
	 GPIO.setup(heSensor,GPIO.IN)

        # displaying sensor data:

         fastSensors = 'curl -s -G "http://192.168.43.54:3000/fastSensors/?light='+str(GPIO.input(ltSensor))+'&flame='+str(GPIO.input(flSensor))+'&sound='+str(GPIO.input(soSensor))+'&hall='+str(GPIO.input(heSensor))+'"'
         os.system(fastSensors);
         print "Sending data for fast sensors..."
      finally:
             GPIO.cleanup()
             time.sleep(0.2)
