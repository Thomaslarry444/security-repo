
from multiprocessing import Pool
from multiprocessing.sharedctypes import Value
from unittest import result
import pandas as pd
from netmiko import ConnectHandler
from argparse import ArgumentParser
from pandas.core.frame import DataFrame
import getpass 
import os.path 
from netmiko import ConnectHandler, file_transfer
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException
from paramiko.ssh_exception import AuthenticationException
import time 
from concurrent.futures import ProcessPoolExecutor, wait

print('hello test')
StartTime=time.time
hp_devices=DataFrame()
hp_devices_ip=DataFrame()
hp_devices_ip_frame=DataFrame()
hp_devices_ip_list=[]
df1=DataFrame()
devices=[]
cisco_devices=DataFrame()
devices_ips_Model=DataFrame()
devices_ips_list=[]
cisco_devices_ips_list=()
platform_cisco='cisco_ios'
platform_hp='hp_procurve'
username='xcg6761'
#password=getpass.getpass('Passwort:')
vendor_list=['cisco','hp']
MAX_THREADS = 10

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

# --- Upload Netmiko function
def upload_nemiko(device):
    print("Upload on:", device)
        # Create the Netmiko SSH connection
    try:
        ssh_conn = ConnectHandler(**device)
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
# --- Check file exists function
def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return(arg)


# # --- Confirmation function
# def confirm(prompt=None, resp=False):

#     if prompt is None:
#         prompt = 'Confirm'

#     if resp:
#         prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
#     else:
#         prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')

#     while True:
#         ans = input(prompt)
#         if not ans:
#             return resp
#         if ans not in ['y', 'Y', 'n', 'N']:
#             print ('please enter y or n.')
#             continue
#         if ans == 'y' or ans == 'Y':
#             return True
#         if ans == 'n' or ans == 'N':
#             return False

# --- Init argparse
#parser = ArgumentParser()
#parser.add_argument("filename", help="The file to upload", metavar='FILE', type=lambda x: is_valid_file(parser, x))
#args = parser.parse_args()

df1= pd.read_csv(r'C:\Users\XCG6761\Documents\python\Mappe1.csv', sep=';' , dtype=str,  usecols=['Hostname','IP-Adresse','Modell','Seriennr'])
# Generate a list of dictionary-items, one item per line with additional keywords
for i, row in df1.iterrows():
        d=row.to_dict()
        print(d)
        print('next')
        devices.append(d)

Source_list_=next(i for i in devices if i ["Modell"]=="Cisco Catalyst 9500 Switch")
print(Source_list_)
        

quit() 

for i in range (len (vendor_list)):
        vendor=vendor_list[i]
       
        
        
        if  vendor=='cisco':
                 platform=platform_cisco
                 devices=(df1.loc[df1['Seriennr'].str.startswith('F',na=False)]) ###seperate df cisco
                 devices_ips_Model=devices.drop(['Hostname','Seriennr'], axis=1)#####create a list only with ips
                 devices_ips_list=devices_ips_Model['IP-Adresse'].tolist() ####write frame to a list 
                 print(devices_ips_list)
        elif vendor=='hp':
                 platform=platform_hp
                 devices=(df1.loc[df1['Seriennr'].str.startswith('C', na=False) & df1['Modell'=='Cisco Catalyst 9500 Switch', 'Cisco Catalyst 9200L Switch' ]]) ###seperate df in hp list 
                 devices_ip_Model=devices.drop(['Hostname','Seriennr'], axis=1)
                 devices_ips_list=devices_ips_Model['IP-Adresse', 'Modell'].tolist()
                 print(devices_ips_list)###CiscoFile 
# --- Define the OS file to upload
        # if  devices_ips_Model.loc[devices_ips_Model['Modell']] == "Cisco Catalyst 9500 Switch" or devices_ips_Model.loc[devices_ips_Model['Modell']] =="Cisco Catalyst 9300L Switch":
        #                 SOURCE_FILE = 'X:\_RZ-WAN\agree21LAN\Software\LAN-Switches\cat9k_iosxe.16.12.04.SPA.bin'
        # elif  devices_ips_Model.loc[devices_ips_Model['Modell']] == "HP J9772A 2530-48G-PoEP Switch":
        #                 SOURCE_FILE = 'X:\_RZ-WAN\agree21LAN\Software\LAN-Switches\RA_16_04_0022.swi'

# ## --- Ask confirmation
# print(80*"=")
# print('Please, confirm the upload of',SOURCE_FILE+' on: ')
# print(*devices_ips_list, sep ='\n')
# rompt = str("Proceed?")

# if confirm(prompt=prompt, resp=False) == True:
#         # --- Get credentials
#         print(80*"-")
#         USERNAME = input('Please insert your username: ')
#         print("And your password")
#         PASSWORD = getpass()
#         print(80*"-")

# # --- Get the time for timing
#         start_time = time()

#     # --- Set the number of threads
#         pool = ProcessPoolExecutor(MAX_THREADS)
        
#         Future_List_cisco= []
#         Future_List_hp=[]
#         for ip in range (len (devices_ips_list)):
#                 print('hello test 2')
#                 device= {'device_type':
#                          devices_ips_list [ip] ,
#                         'username':USERNAME,
#                         'password':PASSWORD,
#                         'port':22,
#                         'verbose':True}
       
#                 if vendor=='cisco':
#                         print('hello test 3')
#                         Future=pool.submit(target=upload_nemiko, args=(device,))
#                         Future_List_cisco.append(Future_List_cisco)
#                 elif vendor=='hp':
#                         Future = pool.submit(target=upload_nemiko, args=(device,))
#                         Future_List_hp(Future_List_hp)###threads liste beachten 
        
#                         if vendor=='cisco':
#                                 wait(Future_List_cisco)
            
#                         if vendor=='hp':
#                                 wait(Future_List_hp)
                
        
#         ##Alles gemacht 
#                         print(80*"=")
#                         print("Uploads done in {} seconds".format(time() - start_time))
#                         print(80*"=")
# else:
#                         print("Failed")       