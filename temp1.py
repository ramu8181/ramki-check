import ipaddress

is_dnx1 = input('DNX1 platform? (y/n - default: y): ' or 'y')
if is_dnx1 in 'yY':
    is_dnx1 = True
else:
    is_dnx1 = False
print(f'DNX1 platform?: {"yes" if is_dnx1 else "no"}')
