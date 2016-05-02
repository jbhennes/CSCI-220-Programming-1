## CompanyName.py
## Inputs an internet domain name in the form "www.xyz.com"
## and outputs the company name, "xyz".

import string

domainName = raw_input("Enter an internet domain name (www.xyz.com): ")

firstDotPos = string.find(domainName, ".")

modifiedName = domainName[firstDotPos+1:]

secondDotPos = string.find(modifiedName, ".")

company = modifiedName[:secondDotPos]

print "The company name is", company
