import serial
import time

ser = serial.Serial(port='/dev/cu.usbserial-AB0KI669',baudrate=9600,)

def serial_output(send):
    ser.write(send.encode())