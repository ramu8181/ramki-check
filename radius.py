
#user1@airtel.com Cleartext-Password:="Cisco"
#    Auth-Type := Accept,
#    Service-Type=Framed-User,
#    Framed-IP-Address = 172.16.0.1,
#    cisco-avpair += "ip:vrf-id=vrf1",
#    cisco-avpair="ip:ip-unnumbered=loopback1"


if __name__=='__main__':
    increment = 0
    user = 0
    with open('file100.txt',mode="w") as file_1: 
     for f in range (16,20): 
        for i in range ( 0,254):
           increment = increment +1 
           for j in range (1,20+1):
             user = user + 1
             file_1.write("user"+ str(user) + "@airtel.com Cleartext-Password:=\"Cisco\"")
             file_1.write("\n")
             file_1.write("    Auth-Type :=Accept,")
             file_1.write("\n")
             file_1.write("    Service-Type=Framed-User,")
             file_1.write("\n")
             file_1.write("    Framed-IP-Address = " + "172." + str(f) + "." + str(i) + "." + str(j) + ",")
             file_1.write("\n")
             file_1.write("    cisco-avpair +=\"ip:vrf-id=vrf" + str(increment) + "\",")
             file_1.write("\n")
             file_1.write("    cisco-avpair=\"ip:ip-unnumbered=loopback" + str(increment) + "\"")
             file_1.write("\n")
             file_1.write("\n")
             if ( user == 6000):
                exit()
        
