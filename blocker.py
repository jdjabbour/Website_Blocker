import time
from datetime import datetime as dt
import platform
import os

if platform.system() == 'Linux' or platform.system() == 'Darwin':
    if os.path.isfile('/etc/hosts'):
        hosts_path = "/etc/hosts"
elif platform.system() == 'Windows':
    if os.path.isfile(r"C:\windows\System32\drivers\etc\hosts"):
        hosts_path = r"C:\windows\System32\drivers\etc\hosts"
else:
    print("This app doesn't support homebrews...")

hosts_temp = 'hosts'
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print('Working hours.')
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            #print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines() # Converts each line in file as a list item
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        
        print('Work hours are over.')

    time.sleep(5)


