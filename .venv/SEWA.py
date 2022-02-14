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
devices=[]

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
def upload_nemiko(netdevice):
    print("Upload on:", device)
        # Create the Netmiko SSH connection
    try:
        ssh_conn = ConnectHandler(**netdevice)
        transfer_dict = {}
        transfer_dict = file_transfer(ssh_conn,
                            source_file=SOURCE_FILE,
                            dest_file=SOURCE_FILE,
                            )
        print(80*"=")
        print('Results for', device+':')
        print('File exists already: ',transfer_dict['file_exists'])
        print('File transferred: ',transfer_dict['file_transferred'])
        print('MD5 verified :',transfer_dict['file_verified'])
    except NetMikoTimeoutException:
        print(80*"=")
        print('Results for', device+':')
        print('Skipped: SSH Timed out')
        #continue
    except (AuthenticationException, NetMikoAuthenticationException):
        print(80*"=")
        print('Results for', device+':')
        print('Skipped: Authentication failed')
        #continue


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
    # device_file_list= pd.read_csv(file, sep=';' , dtype=str,  usecols=['Hostname','IP-Adresse','Seriennr'])
    # print(device_file_list)
    # # define List Paremeter
    # # Get Data Frames
    # devices_ips_frame=DataFrame()
    # devices=(device_file_list.loc[device_file_list['Seriennr'].str.startswith('F',na=False)]) # seperate df cisco
    # devices_ips_frame=devices.drop(['Hostname','Seriennr'], axis=1) # create a list only with ips
    # devices_ips_list=devices_ips_frame['IP-Adresse'].tolist() # write frame to a list 
    # print(devices_ips_list) # Device IP List 
    # Process for each IP in the Device List with defined Threads
    df1= pd.read_csv(r'C:\Users\XCG6761\Documents\python\Mappe1.csv', sep=';' , dtype=str,  usecols=['Hostname','IP-Adresse','Modell','Seriennr'])
# Generate a list of dictionary-items, one item per line with additional keywords
    for i, row in df1.iterrows():
            d=row.to_dict()
            print(d)
            print('next')
            devices.append(d)


    if (i for i in devices if i ["Modell"]=="Cisco Catalyst 9500 Switch" or ['Model']=='Cisco Catalyst 9300L Switch'):
        SOURCE_FILE=(r'X:\_RZ-WAN\agree21LAN\Software\LAN-Switches\cat9k_lite_iosxe.17.03.04b.SPA.bin')
    elif(i for i in devices if i ["Model"]=="Cisco Catalyst 9200L Switch"):
        SOURCE_FILE=(r'X:\_RZ-WAN\agree21LAN\Software\LAN-Switches\cat9k_lite_iosxe.17.03.04b.SPA.bin')
    elif (i for i in devices if i ["Model"]=="Cisco Catalyst 9200L Switch"):
        SOURCE_FILE=''
        
    for ip in range (len (devices)):
        # Build Device dictbremen08
        netdevice= {'device_type':platform,
            'host':devices [i],
            'username':username,
            'password':password,
            'port':22,
            'verbose':True}
        # Add it into our List
        device_list["data"].append(devices[i])
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