# import Libraries
import threading
import time

# import users modules
from telegram_bot import send_telegram
from temperature import body_sensor
from bluetooth_adaptor_info import bluetooth_adaptor_info
from ultrasonic_distance_sensor import distance
from bluetooth_server_by_mac import StartBluetoothMacServer
from bluetooth_server_by_uuid import StartBluetoothUuidServer

# send_telegram("Start programm:  \n" + bluetooth_adaptor_info() + "\nTemperature: " + body_sensor() + "°C\nDistance: " + str(distance()) + "cm")

def getInfo():
    while 1:
        print ("\nStart programm:  \n" + bluetooth_adaptor_info() + "\nTemperature: " + body_sensor() + "°C\nDistance: " + str(distance()) + "cm")
        time.sleep(5)

bluetoothMacThread = threading.Thread(target=StartBluetoothMacServer)
bluetoothMacThread.start()
# bluetoothThread.join()

bluetoothUuidThread = threading.Thread(target=StartBluetoothUuidServer)
bluetoothUuidThread.start()
# bluetoothThread.join()

getInfoThread = threading.Thread(target=getInfo)
getInfoThread.start()
# bluetoothThread.join()
































print ("Start programm:  \n" + bluetooth_adaptor_info() + "\nTemperature: " + body_sensor() + "°C\nDistance: " + str(distance()) + "cm")



