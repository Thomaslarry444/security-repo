from netmiko import ConnectHandler

device= ConnectHandler(host=, port='22,' username='xcg6761', password='cisco', device_type='cisco_ios')
output = connection.send.commmand('sh version')
print(output)

print('closing connection')
connection.disconnect()