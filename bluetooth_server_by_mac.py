#https://quares.ru/?id=527150
#https://scribles.net/setting-up-bluetooth-serial-port-profile-on-raspberry-pi/
"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""
import RPi.GPIO as GPIO
import socket
import sys
import time
import os


def StartBluetoothMacServer():
    LED1 = 21
    LED2 = 26
    LED3 = 20
    LED4 = 19
    LED5 = 16
    LED6 = 13

    LED3_STATUS = 0
    
    GPIO.setwarnings(False)
    
    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)

    def SetAllLedLow():
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.LOW)
        GPIO.output(LED3, GPIO.LOW)
        GPIO.output(LED4, GPIO.LOW)
        GPIO.output(LED5, GPIO.LOW)
        GPIO.output(LED6, GPIO.LOW)
        
    def CheckPinLed():
        print("CheckPinLed")
        SetAllLedLow()
        timeout = 0.1
        time.sleep(timeout)
        GPIO.output(LED1, GPIO.HIGH)
        time.sleep(timeout)
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(timeout)
        GPIO.output(LED2, GPIO.LOW)
        GPIO.output(LED3, GPIO.HIGH)
        time.sleep(timeout)
        GPIO.output(LED3, GPIO.LOW)
        GPIO.output(LED4, GPIO.HIGH)
        time.sleep(timeout)
        GPIO.output(LED4, GPIO.LOW)
        GPIO.output(LED5, GPIO.HIGH)        
        time.sleep(timeout)
        GPIO.output(LED5, GPIO.LOW)
        GPIO.output(LED6, GPIO.HIGH)
        time.sleep(timeout)
        GPIO.output(LED6, GPIO.LOW)

    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.setup(LED3, GPIO.OUT)
    GPIO.setup(LED4, GPIO.OUT)
    GPIO.setup(LED5, GPIO.OUT)
    GPIO.setup(LED6, GPIO.OUT)

    SetAllLedLow()

    hostMACAddress = 'DC:A6:32:9A:F6:FF' #hciconfig
    port = 0 
    backlog = 1
    size = 1024
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.bind((hostMACAddress,port))
    s.listen(backlog)
    while 1:
        try:
            print("try")
            GPIO.output(LED1, GPIO.HIGH)
            client, address = s.accept()
            while 1:
                print("while")
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.HIGH)
                data = client.recv(size)
                if data:
                    print(data)
                    if(data == b'0\r\n' or data == b'A'):
                        GPIO.output(LED3, GPIO.LOW)
                    if(data == b'1\r\n' or data == b'1'):
                        GPIO.output(LED3, GPIO.HIGH)
                    if(data == b'2\r\n' or data == b'B'):
                        for i in  range(1,10):
                            CheckPinLed()
                    if(data == b'3\r\n' or data == b'C'):
                        from subprocess import call
                        call("sudo shutdown -r now", shell=True)                    
                    if(data == b'4\r\n' or data == b'D'):    
                        from subprocess import call
                        call("sudo shutdown -h now", shell=True)
                    client.send(data)
        except Exception as e:
            print (e)
            print("Closing socket")
            GPIO.output(LED2, GPIO.LOW)
            GPIO.output(LED3, GPIO.LOW)
            client.close()
            #s.close()
            
if __name__ == '__main__':
  StartBluetoothMacServer()