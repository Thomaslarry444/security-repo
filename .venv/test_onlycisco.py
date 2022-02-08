
import pandas as pd
import re
import numpy as np
from netmiko import ConnectHandler
from pandas.core.frame import DataFrame
import getpass
import os
import threading
import time

hp_devices_ip=DataFrame()
hp_devices_ip_frame=DataFrame()
hp_devices_ip_list=[]
df1=DataFrame()
cisco_devices=DataFrame()
devices_ips_frame=DataFrame()
devices_ips_list=[]
cisco_devices_ips_list=()
platform_cisco='cisco_ios'
platform_hp='hp_procurve'
username='xcg6761'
password=getpass.getpass('Passwort:')
vendor_list=['cisco','hp']

def ciscoconfig(device):
            #net_connect=ConnectHandler(device_type=platform, ip=devices_ips_list [i], username=username, password=password)
            print('functions aufruf')
            connection=ConnectHandler(**device)
            with open('cisco_config.txt') as CONFIG_LINES:
                CONFIG=CONFIG_LINES.read()
            output=connection.send_config_set(CONFIG)
            print(output)

df1= pd.read_csv('test_list1.csv', sep=';' , dtype=str,  usecols=['Hostname','IP-Adresse','Seriennr'])
devices=(df1.loc[df1['Seriennr'].str.startswith('F',na=False)]) ###seperate df cisco
devices_ips_frame=devices.drop(['Hostname','Seriennr'], axis=1)#####create a list only with ips
devices_ips_list=devices_ips_frame['IP-Adresse'].tolist() ####write frame to a list 
print(devices_ips_list)

threads_cisco=list()
for ip in range (len (devices_ips_list)):
    print('hello test 2')
    device= {'device_type':platform_cisco,
                'host':devices_ips_list [ip] ,
                'username':username,
                'password':password,
                'port':22,
                'verbose':True}
    th_cisco=threading.Thread(target=ciscoconfig, args=(device,))
    threads_cisco.append(th_cisco)
for th_cisco in threads_cisco:
        print(threads_cisco)	
        th_cisco.start()
for th_cisco in threads_cisco:
        th_cisco.join()