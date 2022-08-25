from ctypes.wintypes import RGB
from itertools import count
import serial
import winsound
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
# print to see if there are different voices installed
#for v in voices:
#    print(v)

serialPort = serial.Serial(port = "COM61", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

while(1):
    if(serialPort.in_waiting > 0):            
        s = serialPort.readline()
        print(s) # print the incoming strings
        if b'PSM ERROR' in s:
            engine.say("PSM ERROR PSM ERROR PSM ERROR")
            engine.runAndWait()
            # optional beeping sounds
            frequency = 2500  # Set Frequency To 2500 Hertz 
            duration = 10000  # Set Duration To 1000 ms == 1 second
            for i in range(1, 20):           
                winsound.Beep(i * 100, 200)
            for i in range(1, 20):           
                winsound.Beep(i * 100, 200)
        if b'PSM OK' in s:
            engine.say("PSM OK")
            engine.runAndWait()
