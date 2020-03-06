#assumption
# UART1: P9_26 and P9_24 device is /dev/tty01
#run "pip install pyserial"

#d:wqmport Adafruit_BBIO.UART as UART
import serial 
from datetime import datetime 

#UART.setup("UART1")

ser=serial.Serial(port = "/dev/tty", baudrate=9600)
ser.close()
ser.open()

f=open("example.csv","a+")
ser.write("hello")
data = ser.read() #Only get a byte for now
t = datetime.now()
writedata = strftime("%H:%M:%S") + "," + data
f.write(writedata)




#f = open("/dev/tty01","r")

#if ser.isOpen():
#	print("Serial is open!")
#	ser.write("message to init communication")



###############################################
#main plugin behavior
#For now just let it init pins, UART, and write to csv


