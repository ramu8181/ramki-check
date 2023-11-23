#!/usr/bin/python
from netmiko import ConnectHandler
import re
from datetime import datetime
from time import sleep


"""
####

Input to the Router:

1) Use a Do Parallel method to login to the SSH method.
2) Take the snapshot of the Current configs in the Routers.
3) Ftp the configs to the Remote server where the cerdentials is provided.
4)

Output to the Router:
1) Use a Do Parallel method to login to the SSH method.
2) Ftp the configs to the Router from the Remote server where the cerdentials is provided.
3) Config name can be found based on the router name in specified 
4)

"""


def ssh_connect(ip_list):

  ssh_connect_hand = {}
  for ip in ip_list:
     cisco = {
    'device_type':'cisco_ios',
    'ip':ip,
    'username':'admin',     #ssh username
    'password':'cisco!123', 
    'secret':'cisco!123' #ssh password
    }
     net_connect = ConnectHandler(**cisco)
     print(f"Default prompt: {net_connect.find_prompt()}")
     if (">" in net_connect.find_prompt() ):
        net_connect.enable()
        print(f"Enable command: {net_connect.find_prompt()}")
     #output = net_connect.send_command("show version ")   
     #print (output)
     output = net_connect.send_command('sh run | i host')
     print (output)
     host_name = output.split()
     print (host_name[1])
     ssh_connect_hand[host_name[1]] = net_connect
   
  return ssh_connect_hand
  
   
def copy_running_config_on_disk(net_connect):
  
  now = str(datetime.now()).split(".")
  print (str(datetime.now))
  now[0] = now[0].replace( ":", "")
  now[0] = now[0].replace( "-", "")
  now[0] = now[0].replace( " ", "-")
  identifier=str(input("Enter the Unique_name of the configs in 6 characters"))
  for key in net_connect:
     #running_config_name = "copy running-config flash:" + key + now[0] + ".txt"
     running_config_name = "copy running-config flash:" + key.replace( "-", "") + now[0] + " " + identifier + ".txt"    
     output = net_connect[key].send_command_timing(running_config_name)
     print (output)
     if 'Destination filename' in output:
       output += net_connect[key].send_command_timing('\n')
       print (output)
     if "Do you want to over write? [confirm]" in output:
       output += net_connect[key].send_command_timing('\n')
       print (output)
    
     return True

def copy_running_config_on_tftp(net_connect):

  now = str(datetime.now()).split(".")
  print (str(datetime.now))
  now[0] = now[0].replace( ":", "")
  now[0] = now[0].replace( "-", "")
  now[0] = now[0].replace( " ", "-")
  identifier=str(input("Enter the Unique_name of the configs in 6 characters:   "))
  for key in net_connect:
     #running_config_name = "copy running-config tftp:" + key + now[0] + ".txt"
     running_config_name = "copy running-config tftp" 
     identified_value = "tftp/ramki" +key.replace( "-", "") + now[0] + " " + identifier + ".txt"    
     output = net_connect[key].send_command_timing(running_config_name)
     print (output)
     if 'Address or name of remote host' in output:
       output += net_connect[key].send_command_timing("1.1.1.1")
       print (output)
     if "Destination filename" in output:
       output += net_connect[key].send_command_timing("identified_value")
       print (output)

  return True  

def apply_running_config_on_disk(net_connect):
  
  now = str(datetime.now()).split(".")
  print (str(datetime.now))
  now[0] = now[0].replace( ":", "")
  now[0] = now[0].replace( "-", "")
  now[0] = now[0].replace( " ", "-")
  identifier=str(input("Enter the Unique_name of the configs in 6 characters"))
  for key in net_connect:
     #running_config_name = "copy running-config flash:" + key + now[0] + ".txt"
     running_config_name = "copy running-config flash:" + key.replace( "-", "") + now[0] + " " + identifier + ".txt"    
     output = net_connect[key].send_command_timing(running_config_name)
     print (output)
     if 'Destination filename' in output:
       output += net_connect[key].send_command_timing('\n')
       print (output)
     if "Do you want to over write? [confirm]" in output:
       output += net_connect[key].send_command_timing('\n')
       print (output)
    
  return True

def apply_running_config_on_tftp(net_connect):

  now = str(datetime.now()).split(".")
  print (str(datetime.now))
  now[0] = now[0].replace( ":", "")
  now[0] = now[0].replace( "-", "")
  now[0] = now[0].replace( " ", "-")
  identifier=str(input("Enter the Unique_name of the configs in 6 characters:   "))
  for key in net_connect:
     #running_config_name = "copy running-config tftp:" + key + now[0] + ".txt"
     running_config_name = "copy running-config flash:" + key.replace( "-", "") + now[0] + " " + identifier + ".txt"    
     output = net_connect[key].send_command_timing(running_config_name)
     print (output)
     if 'Destination filename' in output:
       output += net_connect[key].send_command_timing('\n')
       print (output)
     if "Do you want to over write? [confirm]" in output:
       output += net_connect[key].send_command_timing('\n')
       print (output)

  return True  


if __name__=='__main__':

    #here is list of cisco routers ip addresses
    #ip_list = ['10.76.5.8']
    #ip_list = ['10.197.201.73','10.197.201.71','10.197.201.72']
    ip_list = ['10.197.201.73']
    #list where informations will be stored
    devices = []
    #tftp = raw_input('Enter TFTP server IP addr: ')

    net_connect = ssh_connect(ip_list)
    #copy_running_config_on_disk(net_connect)
    copy_running_config_on_tftp(net_connect)
  

  