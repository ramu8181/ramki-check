import re
string1 = input()
matcher= re.compile(r'([a-z0-9])\1+')
#print (matcher.match(string1))
list1 = [ match.group() for match in matcher.finditer(string1)]
#m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
#print(m.group(1) if m else -1)
#print (list(map(int,' '.join(str(list1[0])).split()))[0])
if len(list1) > 0:
    print (' '.join(str(list1[0]))[0])
else:
    print ("-1")
