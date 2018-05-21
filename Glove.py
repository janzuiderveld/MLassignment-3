import socket
from sense_hat import SenseHat
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()
sense = SenseHat()
GAIN = 2

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#client_socket.settimeout(1.0)
addr = ("X.X.X.X", 12001)

values = [0]*3

while True:
    for i in range(3):
        values[i] = (adc.read_adc(i+1, gain=GAIN))
   
   
    message = "%i %i %i" %(values[0], values[1], values[2])
    client_socket.sendto(message, addr)
