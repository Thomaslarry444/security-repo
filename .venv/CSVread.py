#import CSVread
import pandas as pd
import re
import numpy as np
from netmiko import ConnectHandler
from pandas.core.frame import DataFrame
import getpass
import os
import threading


#hp_devices=DataFrame()
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

for i in range (len (vendor_list)):
    vendor=vendor_list[i]
    df1= pd.read_csv('20211124_all_lan.csv', sep=';' , dtype=str,  usecols=['Hostname','IP-Adresse','Seriennr'])
    if vendor=='cisco':
        platform=platform_cisco
        devices=(df1.loc[df1['Seriennr'].str.startswith('F', na=False)]) ###seperate df cisco
        devices.to_csv('cisco.csv')
        devices_ips_frame=devices.drop(['Hostname','Seriennr'], axis=1)#####create a list only with ips
        devices_ips_list=devices_ips_frame['IP-Adresse'].tolist() ####write frame to a list 
        print(devices_ips_list)
    elif vendor=='hp':
        platform=platform_hp
        devices=(df1.loc[df1['Seriennr'].str.startswith('C', na=False)]) ###seperate df in hp list
        devices.to_csv('hp.csv') 
        devices_ip_frame=devices.drop(['Hostname','Seriennr'], axis=1)
        devices_ips_list=devices_ip_frame['IP-Adresse'].tolist()
        print(devices_ips_list)

    

    for i in range (len (devices_ips_list)):
        used_device = ConnectHandler(device_type=platform, ip=devices_ips_list [i], username=username, password=password)
        config_commands = ['sh version']
        print(used_device.send_config_set(config_commands))

        used_device.disconnect()  
    







