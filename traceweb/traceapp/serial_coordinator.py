import time
import sys
import serial

port = "/dev/hidraw0"
ser = serial.Serial(port, 9600, timeout=1, writeTimeout=0)
start_time = time.time()

# Beginning of registration, send message to coordinator
ser.write("@@")

timeout = False
asterisks = 0
read_mac_address = False
mac_address = ""
text_output = open("macAddress.txt", "w")

while True:
	print "wait"
	if time.time() - start_time >= 60:
		timeout = True
		break

    # Read data from the coordinator
	received = ser.read(1)

	if not read_mac_address:
		if received == "*":
			asterisks += 1
			if asterisks == 3:
				read_mac_address = True
			else:
				asterisks = 0
	else:
		mac_address += received
		if len(mac_address) == 16:
			print mac_address
			text_output.write(mac_address)
			text_output.close()
			break

# End of registration, send message to coordinator
ser.write("&&")

if timeout:
	print "Timeout"
	sys.exit(1)
else:
	sys.exit(0)
