import pandas as pd
import re
import numpy as np
from netmiko import ConnectHandler
from pandas.core.frame import DataFrame
import getpass
import os
import threading
import time


print('hello test')
#StartTime=time.time



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

def ciscoconfig(device):
            #net_connect=ConnectHandler(device_type=platform, ip=devices_ips_list [i], username=username, password=password)
            print('functions aufruf')
            connection=ConnectHandler(**device)
            with open('cisco_config.txt') as CONFIG_LINES:
                CONFIG=CONFIG_LINES.read()
            output=connection.send_config_set(CONFIG)
            print(output)

            connection.disconnect()
def hpconfig(device):
            connection_hp=ConnectHandler(**device)
            with open('hp_config.txt') as CONFIG_LINES:
                CONFIG=CONFIG_LINES.read()
            output=connection_hp.send_config_set(CONFIG)
            print(output)
            connection_hp.disconnect()

for i in range (len (vendor_list)):
    vendor=vendor_list[i]
    df1= pd.read_csv('test_list1.csv', sep=';' , dtype=str,  usecols=['Hostname','IP-Adresse','Seriennr'])
    print(df1)
    if vendor=='cisco':
        platform=platform_cisco
        devices=(df1.loc[df1['Seriennr'].str.startswith('F',na=False)]) ###seperate df cisco
        devices_ips_frame=devices.drop(['Hostname','Seriennr'], axis=1)#####create a list only with ips
        devices_ips_list=devices_ips_frame['IP-Adresse'].tolist() ####write frame to a list 
        print(devices_ips_list)
    elif vendor=='hp':
        platform=platform_hp
        devices=(df1.loc[df1['Seriennr'].str.startswith('C', na=False)]) ###seperate df in hp list 
        devices_ip_frame=devices.drop(['Hostname','Seriennr'], axis=1)
        devices_ips_list=devices_ip_frame['IP-Adresse'].tolist()
        print(devices_ips_list)###CiscoFile 

    threads_cisco=list()
    threads_hp=list()
    for ip in range (len (devices_ips_list)):
        print('hello test 2')
        device= {'device_type':platform,
                'host':devices_ips_list [ip] ,
                'username':username,
                'password':password,
                'port':22,
                'verbose':True}

       
        if vendor=='cisco':
            print('hello test 3')
            th_cisco=threading.Thread(target=ciscoconfig, args=(device,))
            threads_cisco.append(th_cisco)
        elif vendor=='hp':
                th_hp=threading.Thread(target=hpconfig, args=(device,))
                threads_hp.append(th_hp)###threads liste beachten 
for th_cisco in threads_cisco:
        print(threads_cisco)	
        th_cisco.start()
for th_cisco in threads_cisco:
        th_cisco.join()
for th_hp in threads_hp:
        print(threads_hp)
        th_hp.start()
for th_hp in threads_hp:
        th_hp.join()           
#EndTime=time.time()
    
#print(f'Total execution time:{EndTime-StartTime}')
