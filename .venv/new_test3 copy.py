#from curses import flash
from multiprocessing import Pool
from multiprocessing.sharedctypes import Value
from unittest import result
import pandas as pd
from netmiko import ConnectHandler
#from argparse import ArgumentParser
from pandas.core.frame import DataFrame
import getpass
#import os.path
from netmiko import ConnectHandler, file_transfer
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException
from paramiko.ssh_exception import AuthenticationException
import time
from concurrent.futures import ProcessPoolExecutor, wait

USERNAME = 'xcg6761'
MAX_THREADS = 10
print('Starting initilization.')
StartTime = time.time
hp_devices = DataFrame()
hp_devices_ip = DataFrame()
hp_devices_ip_frame = DataFrame()
hp_devices_ip_list = []
df1 = DataFrame()
devices = []
cisco_devices = DataFrame()
devices_ips_Model = DataFrame()
devices_ips_list = []
cisco_devices_ips_list = ()
platform_cisco = 'cisco_ios'
platform_hp = 'hp_procurve'
password = getpass.getpass('Enter your Passwort:')
netdevice = []
vendor_list = ['cisco', 'hp']
device_details=[]

df1 = pd.read_csv(r'C:\Users\XCG6761\Documents\python\Mappe1.csv', sep=';',dtype=str, usecols=['Hostname', 'IP-Adresse', 'Modell', 'Seriennr'])
    
# Generate a list of dictionary-items, one item per line with additional keywords
for i, row in df1.iterrows():
    d = row.to_dict()
    print(d)
    print('next')
    devices.append(d)

def ciscoconfig(device):
    #net_connect=ConnectHandler(device_type=platform, ip=devices_ips_list [i], username=username, password=password)
    print('functions aufruf')
    connection = ConnectHandler(**device)
    with open('cisco_config.txt') as CONFIG_LINES:
        CONFIG = CONFIG_LINES.read()
    output = connection.send_config_set(CONFIG)
    print(output)
    connection.disconnect()


def hpconfig(device):
    connection_hp = ConnectHandler(**device)
    with open('hp_config.txt') as CONFIG_LINES:
        CONFIG = CONFIG_LINES.read()
    output = connection_hp.send_config_set(CONFIG)
    print(output)
    connection_hp.disconnect()

# --- Upload Netmiko function


def upload_nemiko(netdevice):
    print("starte thread")
    print("Upload on:", netdevice[0])
    # Create the Netmiko SSH connection
    device_details= netdevice[0]
    with ConnectHandler(**device_details) as ssh_conn:
        print("start connect")
        #ssh_conn = ConnectHandler(**netdevice[0])
        
        
        transfer_dict = {}
        print("start transfeer")
        transfer_dict = file_transfer(ssh_conn, source_file=netdevice[1], dest_file=netdevice[1],file_system='flash:',direction='put',overwrite_file=True)
        print(80*"=")
        print('Results for', netdevice[0]+':')
        print('File exists already: ',transfer_dict['file_exists'])
        print('File transferred: ',transfer_dict['file_transferred'])
        print('MD5 verified :',transfer_dict['file_verified'])
    # except NetMikoTimeoutException:
    #     print(80*"=")
    #     print('Results for', netdevice[0]+':')
    #     print('Skipped: SSH Timed out')
    #      #continue
    # except (AuthenticationException, NetMikoAuthenticationException):
    #     print(80*"=")
    #     print('Results for', netdevice[0]+':')
    #     print('Skipped: Authentication failed')
    #      #continue

#  # --- Confirmation function


def main():
    # --- Set the number of threads
    pool = ProcessPoolExecutor(MAX_THREADS)
    Future_List_cisco = []
    # Future_List_hp=[]
    for ip in (devices):
        if ip['Seriennr'].startswith('F'):
            if (ip["Modell"] == "Cisco Catalyst 9500 Switch"):
                source_file = (r'X:\_RZ-WAN\agree21LAN\Software\LAN-Switches\cat9k_lite_iosxe.17.03.04b.SPA.bin')
            elif (ip["Modell"] == "Cisco Catalyst 9300L Switch"):
                source_file = (r'X:\_RZ-WAN\agree21LAN\Software\LAN-Switches\cat9k_lite_iosxe.17.03.04b.SPA.bin')
            elif (ip["Modell"] == "Cisco Catalyst 9200L Switch"):
                source_file = (r'X:\_RZ-WAN\agree21LAN\Software\LAN-Switches\cat9k_lite_iosxe.17.03.04b.SPA.bin')
            elif (ip["Modell"] == "Cisco Catalyst 9200L Switch"):
                source_file = ''           
            netdevice = {'device_type': platform_cisco,
                        'Host': ip['IP-Adresse'],
                        'username': USERNAME,
                        'password': password,
                        'port': 22,
                        'verbose': True
                        }
            args=[netdevice,source_file]  
            Future = pool.submit(upload_nemiko, args)
            Future_List_cisco.append(Future)
    wait(Future_List_cisco)

if (__name__ == '__main__'):
    main()

