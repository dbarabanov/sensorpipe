import serial
from datetime import datetime

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)
serialFromArduino.flushInput()
now = datetime.now()
filename = "sensor_read_"+now.strftime("%Y_%m_%d_%H_%M_%S")
with open(filename, 'w') as writer:
	while True:
	    if (serialFromArduino.inWaiting() > 0):
		now = datetime.now().strftime("%H:%M:%S")
		input = serialFromArduino.readline()
		line = now+'\t'+input
		print(line)
		writer.write(line)
