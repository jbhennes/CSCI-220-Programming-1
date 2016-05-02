## FileExtension.py
## Inputs a file name in the form "name.extension" and outputs
## the extension.

import string

fileName = raw_input("Enter a file name (name.ext): ")

dotPosition = string.find(fileName, ".")

extension = fileName[dotPosition+1:]

print "The file extension is", extension
