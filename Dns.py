import socket
import dns.resolver
import dns.query
import dns.zone

import dns.resolver #import the module
myResolver = dns.resolver.Resolver() #create a new instance named 'myResolver'
web_site = raw_input("\nPlease enter a domain name that you wish to examinate   : ")

myAnswers = myResolver.query(web_site, "A") #Lookup the 'A' record(s) for ... .com
for rdata in myAnswers: #for each response
    print rdata #print the
    print "TTL: " + str(myAnswers.rrset.ttl)
    print("")

