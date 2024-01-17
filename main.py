import sys
import requests
import os
from time import sleep
from platform import system
from datetime import datetime as dt
THEN = dt.now()
def target_manager():
    try:
        with open("monitor.txt", "r") as f:
            for x in f.readlines():
                host_check(x.strip())
    except Exception as e:
        if(system() == "Windows"):
            os.system("if not exist monitor.txt copy NUL monitor.txt")
        else:
            os.system("touch monitor.txt")
        print("We've built the file for you - \n Enter the hosts to monitor, separated by line.")
                
def host_check(host):
    headers = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)'
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/57.0.2987.110'
    'Safari/537.36'
    }
    r = requests.get(host,  headers=headers)
    now = dt.now()
    if r.status_code != 200:
        print("+| OUTPUT WINDOW  |+", end="\r")
        print("+| {} at status: DEATH! {} @ {} SINCE {} |+".format(host, r.status_code, now, THEN), end="\r")
    else:
        print("+| OUTPUT WINDOW  |+", end="\r")
        print("+| {} at status: LIFE! {} @ {} SINCE {} |+".format(host, r.status_code, now, THEN), end="\r")
        
def main():
    while 1:
        target_manager()    
        sleep(60)
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print("FAIL! {}".format(e))
        sys.exit()