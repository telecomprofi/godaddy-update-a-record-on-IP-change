#### python 3 script that updatws A record after reboot/stopping of VM instance & change of public IP address

* Script checks public IP of your Cloud VM and if its different from A record of your DNS updates it with newly asigned IP address.
 place files into your home dir @ VM with non-eleastic/permanent Public IP address and automate update of DNS A record @ Godaddy.
```
    #tree ~/ | grep 'godaddy'
    ├── godaddy_ip.txt
    ├── update_godaddy.py
```

* to make it autorun:
```    
    #echo 'python3 ~/update_godaddy.py' >> ~/.bashrc
```


Checks:
* 1. check whats your VM's current public IP address manually:
```   
 #curl ifconfig.me
```   
* 2. check what IP address is currently in your doamin A-record at Godaddy:
</br>
a) with dig in shell
</br>


    #dig @8.8.8.8 +short NS <domain.com>


</br>
or
</br>
b)
</br>
got to https://www.whatsmydns.net/ and search for NS record of your domain < type 'example.com' into search text filed and select NS from drop-down list. press search button. 

* 3. Then copy one of ns' addresses and dig against it: 
  
```
    #dig @<one-of-your-domain's NS'es> +short <your-domain-name->
```

