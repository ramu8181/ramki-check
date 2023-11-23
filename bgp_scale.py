
#user1@airtel.com Cleartext-Password:="Cisco"
#    Auth-Type := Accept,
#    Service-Type=Framed-User,
#    Framed-IP-Address = 172.16.0.1,
#    cisco-avpair += "ip:vrf-id=vrf1",
#    cisco-avpair="ip:ip-unnumbered=loopback1"
# address-family ipv4 vrf vrf1
#  redistribute connected
# redistribute static
#  neighbor 172.16.0.1 remote-as 101
#  neighbor 172.16.0.1 update-source Loopback1
#  neighbor 172.16.0.1 activate
# exit-address-family

if __name__=='__main__':
    increment = 0
    user = 0
    asno = 100
    with open('file101.txt',mode="w") as file_1: 
     for f in range (16,20): 
        for i in range ( 0,254):
           increment = increment +1 
           asno = asno + 1
           for j in range (1,20+1):
             user = user + 1
             file_1.write("address-family ipv4 vrf vrf" + str(increment) + "\n")
             file_1.write("redistribute connected\n")
             file_1.write("neighbor 172."+ str(f) + "." + str(i) + "." + str(j) + " remote-as "+ str(asno) + "\n")
             file_1.write("neighbor 172."+ str(f) + "." + str(i) + "." + str(j)  + " update-source Loopback" + str(increment) +"\n")
             file_1.write("neighbor 172."+ str(f) + "." + str(i) + "." + str(j)  + " activate\n")
             file_1.write("exit-address-family\n") 
             if ( user == 6000):
                exit()
        
