# axfr-scan
This program attempts to grab an AXFR dump of a zone file, It queries all nameservers of a TLD and requests an AXFR dump, It will not grab the whole dump, it only graps a few lines, so when the program is finished, go into the 'tld' folder and you'll see something like TLD.txt, this indicates a dump was successful. 

Use at your own risk, etc, No resale of caught zones, I disclaim all responsibility.
# How to work it?
Run the following commands:
```
git clone https://github.com/hng4/axfr-scan.git
cd axfr-scan
mkdir tld
pip3 install dnspython
python3 scan.py
```
Do note tld.txt is just the IANA list of TLD's, But when updating it, ensure you remove the top commented line.

# What has it done?
So far, It has grabed the zones of:
- .cv
- .gp
- .kg
- .mr
- .pg
- .sl
- .tk
- .xn--mix891f
- .xn--ygbi2ammx
- .bn
- .er
- .hk
- .mo
- .mw
- .ph
- .rw
- .sy
- .xn--lgbbat1ad8j
- .xn--0gbpf8fl

And it continues to run every day, If you have a legitimate reason for these zone files, please contact dnsadmin@oc.gy
