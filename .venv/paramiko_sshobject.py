import paramiko


ssh_client = paramiko.SSHClient()

print('Connecting to 10.15.57.241')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#0ssh_client.connect(hostname='10.15.57.241', port='22', username='xcg6761', password='nadine01',look_for_keys=False, allow_agent=False)
router={'hostname': '10.15.57.241', 'port' :'22','username':'xcg6761','password':'nadine01'}
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)
print(ssh_client.get_transport().is_active())

print('Close ssh to host')
ssh_client.close()