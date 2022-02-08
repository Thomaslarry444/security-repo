from contextlib import closing
from csv import DictReader
from email.headerregistry import Address 
from pprint import pprint
import pandas from pd
import netmiko
import time
import getpass 

# from pyparsing import col 
# username='xcg6761'
# password=getpass.getpass('Passwort:')

# router_dict={'device_type': '', 'Model': '',  'username':username, 'password': password,'port':22, 'verbose':True}
# with open (r"C:\Users\XCG6761\Documents\GitHub\Uniteststore\.venv\test_list1.csv") as csv_file:
#     csv_content=DictReader(csv_file)
#     for row in csv_content:
    
#             if  == 'Model':
#                 router_dict[column_name]=[]
#                 router_dict[column_name].append(row|column_name)
#                 print(router_dict)
           
def loadDevices(devicefile, netaccess):
    """Read the file, which contains the devices to operate with and generate a pandas structure.

    The file must be a ".cvs"-file, containing at least the columns customer, loopback, hostname.
    If column netaccess is available and varialbe netaccess is set, use only matching items.
    If the columns status and checked are not available, they are generated.
    If there are IP addresses formatted as numbers, correct this.
    Generate a list of dictionary-items, one item per line, with additional keywords commands and result.
    """
    global df
    global devices
    global sep

    df=pd.read_csv(devicefile, dtype=str, sep=sep)              # preserve leading zero's using string format
    # Tests
    # print(df)
    col_headers = df.columns.values.tolist()                    # read the column header names
    if "netaccess" not in col_headers and netaccess != "":
        usage(f'option -a set but not available in {devicefile}')
        sys.exit(2)
    if "status" not in col_headers:
        df["status"] = ""                                       # add column status if not available
    if "checked" not in col_headers:
        df["checked"] = ""                                      # add column checked if not available

    # check for IP Adresses, imported as numbers
    # these always have the form 10133106129, but we need 10.133.106.129
    for i, row in df.iterrows():
        if re.search(r'^\d+$', df.at[i,"loopback"]):
            df.at[i,"loopback"] = "{0}.{1}.{2}.{3}".format(df.at[i,"loopback"][0:2], df.at[i,"loopback"][2:5],
                                                           df.at[i,"loopback"][5:8], df.at[i,"loopback"][8:11])
            # Tests
            # print(f'{df.at[i,"loopback"]}')

    # only work with rows matching netaccess
    if "netaccess" in col_headers and netaccess != "":
        df_local = df[df.netaccess == netaccess]
        # Tests
        # print(df_local)
    else:
        df_local = df
    # only work with rows which are not done yet: they are empty (NaN or "") or "OFFLINE"
    done = []
    for i, row in df_local.iterrows():
        status_str = str(df_local.at[i,"status"])
        if status_str != "nan" and status_str != "" and status_str != "OFFLINE":
            done.append(i)
    if len(done) != 0:
        df_local = df_local.drop(done)
    # Tests
    # print(df)
    # print(df_local)

    # check whether there are devices to work with
    if df_local.empty == True:
        print("nothing to do - we are done")
        sys.exit(0)

    # Generate a list of dictionary-items, one item per line with additional keywords
    for i, row in df_local.iterrows():
        d=row.to_dict()
        d.update({"commands": commands})
        d.update({"result": None})
        devices.append(d)
