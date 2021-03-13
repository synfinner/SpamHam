#!/usr/bin/env python3

import sys
import requests
import string
import secrets
# from time import sleep

proxies = {'http': "socks5://127.0.0.1:9150"}

def randmail():
    uname = ''.join(secrets.choice(string.ascii_lowercase + string.digits)
                    for i in range(10))
    dname = ''.join(secrets.choice(string.ascii_lowercase + string.digits)
                    for i in range(15))
    return uname + "@" + dname + ".com"

def main():
    target = sys.argv[1]
    try:
        while True:
            rmail = randmail()
            ip = requests.get(f'{target}/{rmail}', proxies=proxies)
            if ip.status_code == 200:
                print("Sent:",rmail)
                # sleep(1.5)
                continue
            else:
                print("Didn't get a 200 response. Exiting..")
                break
    except Exception as e:
        print(e)
        exit("Stuff broke and I'm dead")

if __name__ == '__main__':
    main()