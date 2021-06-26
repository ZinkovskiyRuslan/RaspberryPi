#!!!terminal sudo hciconfig hci0 piscan


import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *

# GPIO.setwarnings(False)
# 
# from subprocess import call
# call("sudo hciconfig hci0 piscan", shell=True)
#                     
# os.system('modprobe w1-gpio')
# os.system('modprobe w1-therm')
# 
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, GPIO.OUT)
# 
# base_dir = '/sys/bus/w1/devices/'
# device_folder = '/sys/bus/w1/devices/'#glob.glob(base_dir + '28*')[0]
# device_file = '/sys/bus/w1/devices/'#device_folder + '/w1_slave'
def StartBluetoothUuidServer():
    def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c

    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

    advertise_service( server_sock, "AquaPiServer",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ], 
    #                   protocols = [ OBEX_UUID ] 
                        )
    while True:          
        print ("Waiting for connection on RFCOMM channel %d" % port)

        client_sock, client_info = server_sock.accept()
        print ("Accepted connection from ", client_info)

        try:
            while True:
                data = client_sock.recv(1024)
                if len(data) == 0: break
                print ("received [%s]" % data)

                if data == 'temp':
                    data = str(read_temp())+'!'
                elif data == 'lightOn':
                    GPIO.output(17,False)
                    data = 'light on!'
                elif data == 'lightOff':
                    GPIO.output(17,True)
                    data = 'light off!'
                else:
                    data = 'WTF!' 
                    client_sock.send(data)
                print ("sending [%s]" % data)
        except IOError:
            pass

        except KeyboardInterrupt:

            print ("disconnected")

            client_sock.close()
            server_sock.close()
            print ("all done")

            break

if __name__ == '__main__':
  StartBluetoothUuidServer()