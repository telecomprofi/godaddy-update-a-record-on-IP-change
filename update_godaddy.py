#!/usr/bin/env python
# @ not mine found it on github, thanks to the author!

# Import pif to get your public ip, sys and os.path
import pif, sys, os.path

# Partial imports
from godaddypy import Client, Account

# Remember to set your api key and secret
userAccount = Account(api_key='<put yor api_key_here>', api_secret='<put_your_godaddy_api_secret_here>')
userClient = Client(userAccount)
publicIP = pif.get_public_ip('ident.me')

# E.g.: to update your_record.yourdomain.com set domain and record to:
domain = '<put_your_domain_you_want_to_have_public_IP_of_your_VM_to_be_assigned_to_as_A_record>'
a_record = '@'

if os.path.isfile('godaddy_ip.txt'):
    try:
        ip_file = open('godaddy_ip.txt', 'r')
        read_ip = ip_file.read().strip('\n')
        ip_file.close()
    except:
        print("Cannot read IP file")
        sys.exit()
    if read_ip == publicIP:
        print("Read the IP file, no need to change IP")
        sys.exit()

# Try to retrieve the record and update it if necessary 
try:
    currentIP = userClient.get_records(domain, record_type='A', name=a_record)
    if (publicIP != currentIP[0]["data"]):
        updateResult = userClient.update_record_ip(publicIP, domain, a_record, 'A')
        if updateResult is True:
            ip_file = open('godaddy_ip.txt', 'w')
            ip_file.write(publicIP)
            ip_file.close()
            print('Updated DNS record and wrote IP file.')
    else:
        print('Checked the DNS record, no update needed.')
except:
    print(sys.exc_info()[1])
    sys.exit()
