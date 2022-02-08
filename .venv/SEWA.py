import pandas as pd
from netmiko import ConnectHandler
from pandas.core.frame import DataFrame
import multiprocessing as mp
import getpass
import threading
import time

##import ios upgrade 


# Glonbal Variable
print("Data input")
# Get Time
StartTime=time.time
#hp_devices=DataFrame()
#todo delete
#//devices_ips_list=[]
#//cisco_devices_ips_list=()
# Global Variable
platform_cisco='cisco_ios'
platform_hp='hp_procurve'
# Userdata
username='xcg6761'
password = "admiral1"
# password=getpass.getpass('Passwort:')
# Vendor List
do_cisco = True
do_hp = True
#vendor_list=['cisco','hp']
file_cisco = "test_list1.csv"
file_hp = "test_list1.csv"

def config_cisco(device):
        #net_connect=ConnectHandler(device_type=platform, ip=devices_ips_list [i], username=username, password=password)
        print('functions aufruf')
        connection=ConnectHandler(**device)
        with open('cisco_config.txt') as CONFIG_LINES:
                CONFIG=CONFIG_LINES.read()
        output=connection.send_config_set(CONFIG)
        print(output)
        connection.disconnect()


def config_hp(device):
        connection_hp=ConnectHandler(**device)
        with open('hp_config.txt') as CONFIG_LINES:
                CONFIG=CONFIG_LINES.read()
        output=connection_hp.send_config_set(CONFIG)
        print(output)
        connection_hp.disconnect()


def process_vendor(vendor):
    # Define max treads into pool
    pool_hp = mp.Pool(mp.cpu_count())
    # Create Function Objects
    device_list = {}
    device_list["data"] = []
    platform=""
    file = ""
    # Check for Vendor
    if vendor == "cisco":
        platform = platform_cisco
        file = file_cisco
    if vendor == "hp":
        platform = platform_hp
        file = file_hp
    # Load Device list
    device_file_list= pd.read_csv(file, sep=';' , dtype=str,  usecols=['Hostname','IP-Adresse','Seriennr'])
    print(device_file_list)
    # define List Paremeter
    # Get Data Frames
    devices_ips_frame=DataFrame()
    devices=(device_file_list.loc[device_file_list['Seriennr'].str.startswith('F',na=False)]) # seperate df cisco
    devices_ips_frame=devices.drop(['Hostname','Seriennr'], axis=1) # create a list only with ips
    devices_ips_list=devices_ips_frame['IP-Adresse'].tolist() # write frame to a list 
    print(devices_ips_list) # Device IP List 
    # Process for each IP in the Device List with defined Threads
    for ip in range (len (devices_ips_list)):
        # Build Device dictbremen08
        device= {'device_type':platform,
            'host':devices_ips_list [ip],
            'username':username,
            'password':password,
            'port':22,
            'verbose':True}
        # Add it into our List
        device_list["data"].append(device)
    # Check again for Vendor
    if vendor == "cisco":
        platform = platform_cisco
        file = file_cisco
        # Define max treads into pool
        pool = mp.Pool(mp.cpu_count())
        # Process Config for Cisco in Multithread
        pool.map(config_cisco,[device for device in device_list["data"]])
    if vendor == "hp":
        pool = mp.Pool(mp.cpu_count())
        platform = platform_hp
        file = file_hp
        # Process Config for HP in Multithread
        pool.map(config_hp,[device for device in device_list["data"]])


def main():
    # Process for each enabled Vendor
    if do_cisco == True:
            vendor ="cisco"
            process_vendor(vendor)
    if do_hp == True:
            vendor ="hp"
            process_vendor(vendor)
# Start Main Function
main()

EndTime=time.time()
print(f'Total execution time:{EndTime-StartTime}')