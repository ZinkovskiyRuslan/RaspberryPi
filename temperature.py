import os
def body_sensor():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","").replace("'C","").replace("\n",""))