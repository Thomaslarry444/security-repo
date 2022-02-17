

from netmiko import ConnectHandler, file_transfer


device={'device_type': 'cisco_ios',
        'IP':'10:51:162:50',
        'username':'xcg6761',
        'password': 'markus01',
        'port':22,
         'verbose':True}

sshconn=ConnectHandler(**device)
tranfer_output=file_transfer(sshconn,source_file='test.txt', dest_file='test.txt', file_system='flash:',direction='put')

print(tranfer_output)

sshconn.disconnect