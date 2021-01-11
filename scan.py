from dns import *
import dns.zone
import dns.resolver

file = open("tld.txt", "r");
content = file.read();
cl = content.splitlines();
file.close();

for domain in cl:
    #domain = 'google.com'
    domain += "."
    try:
        answers = dns.resolver.query(domain,'NS')
        for server in answers:
            server = str(server);
            server = server[:-1]
            try:
                d = dns.resolver.query(server,'A')
                for a in d:
                    try:
                        z = dns.zone.from_xfr(dns.query.xfr(str(a), domain))
                        names = z.nodes.keys()
                        for n in names:
                            with open("tld/"+domain+"txt", "w+") as myfile:
                                myfile.write(z[n].to_text(n));
                                myfile.close();
#                    print(z[n].to_text(n);
                        print("[OC.GY AXFR SCAN] Got zone: "+domain+" from server: "+server);
                    except dns.query.TransferError as error:
                        print("[OC.GY AXFR SCAN] Caught error: "+str(error)+" from server: "+server+" finding "+domain);
                    except dns.exception.FormError as error:
                        print("[OC.GY AXFR SCAN] Caught error: "+str(error)+" from server: "+server+" finding "+domain);
                    except:
                        print("[OC.GY AXFR SCAN] Caught unknow error from server: "+server+" finding "+domain);
            except:
                print("[OC.GY AXFR SCAN] Caught unknown error when attempting to get nameserver's IP ("+server+")");
    except:
        print("[OC.GY AXFR SCAN] Caught unknown error when attempting to get zone's IP ("+domain+")");
