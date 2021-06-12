from telegram_bot import send_telegram
from temperature import body_sensor
from bluetooth_adaptor_info import bluetooth_adaptor_info

send_telegram("Start programm:  \n" + bluetooth_adaptor_info() + "\nTemperature: " + body_sensor() + "°C")

