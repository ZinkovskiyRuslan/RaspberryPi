import os
def bluetooth_adaptor_info():
        temp = os.popen("sudo hciconfig hci0 name").read()
        mac = temp.replace("\n","").replace("\n","").split("	")[2].split("  ACL")[0]
        name = temp.replace("\n","").replace("\n","").split("Name:")[1] 
        return (mac + " Name:" + name)
    
if __name__ == '__main__':
  res = bluetooth_adaptor_info()
  print(res)