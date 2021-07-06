import time
from datetime import datetime as dt

hostPath = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'

websites_to_block = ['www.youtube.com', 'www.facebook.com']

while 1:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Acces to site not allowed...!")
        with open(hostPath, 'r+') as file:
            content = file.read()
            for site in websites_to_block:
                if site in content:
                    pass
                else:
                    file.write(redirect+' '+site+'\n')
    else:
        with open(hostPath, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites_to_block):
                    file.write(line)
                file.truncate()
            print('Allowed to access the site')
    time.sleep(10)
