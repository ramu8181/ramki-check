 output to STDOUT

https://docs.python.org/3/library/re.html


import re
vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"
pattern1 = "(?<=([qwrtypsdfghjklzxcvbnm])([aeiou]{2,}))"
list1 = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]',input(), flags = re.I)
#list1 = re.findall(pattern1,input(), flags = re.I)

if len(list1) > 0:
    [print(x) for x in list1]
else:
    print ("-1")
