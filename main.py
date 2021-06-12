from telegram_bot import send_telegram
from temperature import body_sensor

send_telegram("Start " + body_sensor() + "°C")

