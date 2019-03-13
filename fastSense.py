import RPi.GPIO as GPIO
import time

while 1==1:
      # Special csi2 Script for reading data from faster sensor

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

         print "Light Sensor:",GPIO.input(ltSensor)
         print "Flame Sensor:",GPIO.input(flSensor)
         print "Sound Sensor:",GPIO.input(soSensor)
         print "Hall Effect Sensor:",GPIO.input(heSensor)

      finally:
             GPIO.cleanup()
             time.sleep(0.2)
