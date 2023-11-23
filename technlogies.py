

import re

#Read the file and Form the interest in the dicitionary.

if __name__=='__main__':
    dict1 = {"Srv6":[],"NSO/CNC":[],"OpenRAN":[],"CnBng":[],"SR-CS":[],"Clocking":[],"Security":[]}
    list1 = []
    with open ( "interested.txt","r") as f:
      for each in f:
        list1  = [x.strip('Tech:') for x in list1]
        list1 = re.split("\s+|\b",each)
        remove_spaces  = [x.strip(' ') for x in list1]
        print (remove_spaces)
        for  key,value in dict1.items():
          if len(list1) >= 2:
            if key in list1[1]:
               temp1 = dict1[key]
               temp1.append(list1[0])
    for key,value in dict1.items():
      print (str(key) + "Resource who is interested" + str(value.join(" "))
