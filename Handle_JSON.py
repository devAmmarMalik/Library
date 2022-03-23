# Python 3
# coding: utf-8
# Read/Write and Update JSON - JavaScript Object Notation file.

__author__ = "Ammar S Malik"
__copyright__ = "Copyright 2022, Time calculations"
__credits__ = ["Ammar Malik"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"

from operator import index
import os
import json, datetime
from xmlrpc.client import DateTime
from datetime import date

oneRecord = {
    "VideoID" : "",
    "CustomerID" : "",
    "IssueDate" : "",
}

t = date.today()

os.system('clear')

filename = "Rental.json"
fileData = []
# Open data file and read its contents to the list above
# With will open the file and then it will close it also
with open(filename, "r+") as jsonFile:
    fileData = json.load(jsonFile)

# Now print all iterations of the records that we read from the load above
print("Showing a list of all outstanding video rentals")
print("Video\t|Customer\t|Issue Date")
for row in fileData:
    print(row['VideoID'] + "\t|\t" + row['CustomerID'] + "\t|\t" + row['VideoID'])


# So fileData has a collection of the entire file. Get the input from the user and save it to the 
# dictionary variable above
oneRecord["VideoID"] = input("Video ID to add : ")
oneRecord["CustomerID"] = input("Customer ID to add : ")
oneRecord["IssueDate"] = t.strftime('%m/%d/%Y')

# Append this record from the dictionary to a list of all records
fileData.append(oneRecord)

# Now print all iterations of the records that we read from the load above
#print("Showing a list of all outstanding video rentals along with new record")
#print("Video\t|Customer\t|Issue Date")
#for row in fileData:
#    print(row['VideoID'] + "\t|\t" + row['CustomerID'] + "\t|\t" + row['VideoID'])

# now serialize the output
NewFiletoWrite = json.dumps(fileData, indent=1)

# Since we have opened this file earlier, we do not need to open it again. Just write the information back
with open(filename, "r+") as jsonFile:
    jsonFile.write(NewFiletoWrite)