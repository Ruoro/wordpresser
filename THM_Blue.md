# BLUE 
_______________________________________________________________________________________________________________________________
#
Steps in Attacking a machine 

### Step:1
1.  Scan and learn what exploit this machine is vulnerable to:
nmap 
Zendesk
Enum shares 
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.149.24

inspect shares 
smbclient //10.10.149.24/anonymous

Download an smb share 
smbget -R smb://10.10.102.244/anonymous

use nmap to enumerate this.
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.102.244

